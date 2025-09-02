# ---------------------------
# First realy LangGraph Agent
# depending on the packages:
# %pip install langgraph langchain_openai
# ---------------------------------------
import os
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# defining the State
# its important to make it non bloated
class EmailState(TypedDict):
    # The email being processed
    email: Dict[str, Any] # Containing subject, sender, etc.
    # Category of the email
    email_category: Optional[str]
    # Reason why the email was marked as spam
    spam_reason: Optional[str]
    # Analysis and decision
    is_spam: Optional[bool]
    # Response generation
    email_draft: Optional[str]
    # Processing metadata
    messages: List[Dict[str, Any]] # Tracking the conversation with LLM

# ------------------
# Defining the nodes
# and model init
# --------------
model = ChatOpenAI(temperature=0) # temperature as a way to refine options

def read_email(state: EmailState):
    """
    Alfred reads and logs the incoming emails
    """
    email = state["email"]
    # initial pre Processing
    print(f"Alfred is processing an email from {email['sender']}"
          "with subject: {email['subject']}")
    # No state changes
    return {}

def classify_email(state: EmailState):
    """
    Alfred uses an LLM to determine if the email is spam or not
    """
    email = state["email"]
    # Preparing the prompt
    prompt = f"""
    As Alfred the butler, analyze this email and determine if its spam or not
    Email:
    From: {email['sender']}
    Subject: {email['subject']}
    Body: {email['body']}
    First, determine if this email is spam, if not explain why.
    If not: categorize it (inquiry, complaint, thank you, etc.)
    """
    # LLM call
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    # Logic to parse the response (should be more robust this is a test)
    response_text = response.content.lower()
    is_spam = "spam" in response_text and "not spam" not in response_text
    # Extract a reason if its a spam
    spam_reason = None
    if is_spam and "reason" in response_text:
        spam_reason = response_text("reason:")[1].strip()
    # Determine the category
    email_category = None
    if not is_spam:
        categories = ["inquiry", "complaint", "thank you", "request", "information"]
        for category in categories:
            if category in response_text:
                email_category = category
                break
    # Update the messages for tracking
    new_messages = state.get("messages", []) + [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": response.content}
            ]
    # Return the updated state
    return {
            "is_spam": is_spam,
            "spam_reason": spam_reason,
            "email_category": email_category,
            "messages": new_messages
            }

def handle_spam(state: EmailState):
    """
    Alfred discards spam emails with a note
    """
    print(f"Alfred has marked the email as spam. Reason: {state['spam_reason']}")
    print("The email has been moved to the spam folder")
    # the end of processing of said email
    return {}

def draft_response(state: EmailState):
    """
    Alfred drafts a preliminary response for non spam email
    """
    email = state["email"]
    category = state["email_category"] or "general"
    # prepare for the prompt
    prompt = f"""
    As Alfred the butler, draft a polite preliminary response to this email
    Email:
    From: {email['sender']}
    Subject: {email['subject']}
    Body: {email['body']}
    This email has been categorized as: {category}
    Draft a brief, professional response that Mr. Hugg can review and personlize
    """
    # calling the LLM
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    # update the message for tracking
    new_messages = state.get("messages", []) + [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": response.content}
            ]
    # return the updated state
    return {
            "email_draft": response.content,
            "messages": new_messages
            }

def notify_mr_hugg(state: EmailState):
    """
    Alfred notifies Mr. Hugg about the email and presents the draft response
    """
    email = state["email"]
    print("\n" + "="*50)
    print(f"Sir, you have received an email from {email['sender']}")
    print(f"Subject: {email['subject']}")
    print(f"Category: {state['email_category']}")
    print("\nI've prepared a draft response for your review:")
    print("-"*50)
    print(state["email_draft"])
    print("="*50 + "\n")
    # We are done processing the email
    return {}

# --------------------------
# Defining The Routine Logic
# Called by LangGraph to determine which edge to follow
# -----------------------------------------------------
def route_email(state: EmailState) -> str:
    """
    Determine the next step based on spam classification
    """
    if state["is_spam"]:
        return "spam"
    else:
        return "legitimate"

# ----------------------------------------------
# Creating the StateGraph and Defining the Edges
# ----------------------------------------------
email_graph = StateGraph(EmailState)
# Addition of nodes
email_graph.add_node("read_email", read_email)
email_graph.add_node("classify_email", classify_email)
email_graph.add_node("handle_spam", handle_spam)
email_graph.add_node("draft_response", draft_response)
email_graph.add_node("notify_mr_hugg", notify_mr_hugg)
# start the edges
email_graph.add_edge(START, "read_email")
# defining the flow
email_graph.add_edge("read_email", "classify_email")
# conditional branching
email_graph.add_conditional_edges(
        "classify_email",
        route_email,
        {
            "spam": "handle_spam",
            "legitimate": "draft_response"
            }
        )
# the final edges
email_graph.add_edge("handle_spam", END)
email_graph.add_edge("draft_response", "notify_mr_hugg")
email_graph.add_edge("notify_mr_hugg", END)
# compile the graph
compiled_graph = email_graph.compile()

# ---------------------------------------
# Running the application with test email
# ---------------------------------------
legit_email = {
        "sender": "john.smith@something.com",
        "subject": "Question about your service",
        "body": "Dear Mr Hugg I would like to talk about possible cooperation"
        }

spam_email = {
        "sender": "asdada@lotter.com",
        "subject": "YOU WON THE LOTTER",
        "body": "Click the link and receive you price right now! Don't wait till it dissapears"
        }

# processing of the emails:
print("\nProcessing the legit email")
legit_result = compiled_graph.invoke({
    "email": legit_email,
    "is_spam": None,
    "spam_reason": None,
    "email_category": None,
    "email_draft": None,
    "messages": []
    })

print("\nProcessing the spam email")
spam_result = compiled_graph.invoke({
    "email": spam_email,
    "is_spam": None,
    "spam_reason": None,
    "email_category": None,
    "email_draft": None,
    "messages": []
    })

# --------------------------------------
# Inspeciting the Workflow with Langfuse
# below configuration depends on:
# %pip install -q langfuse
# %pip install langchain
# getting the keys from project settings
# and the Langfuse callback handler
# --------------------------------------
from langfuse.langchain import CallbackHandler
import os

os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-some-actual-public-key"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-and-the-secret-key"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"

langfuse_handler = CallbackHandler()

# processing the legit email
legit_result = compiled_graph.invoke(
        input={"email": legit_email,
        "is_spam": None,
        "spam_reason": None,
        "email_category": None,
        "draft_response": None,
        "messages": []},
        config={"callbacks": [langfuse_handler]}
        )
# now visualize the graph
compiled_graph.get_graph().draw_mermaid_png()

