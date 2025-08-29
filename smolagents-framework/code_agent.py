# ------------------------------------
# Coding Agent builded with smolagents
# ------------------------------------
from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, tool, InferenceClientModel
import numpy as np
import time
import datetime

# ------------------------------
# Added a parto to test langufse
# ------------------------------

import os

os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-something-here-goes-public-key"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-something-hre-goes-secret-key"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"

from langfuse import get_client

langfuse = get_client()

if langfuse.auth_check():
    print("Langfuse is ready and working!")
else:
    print("Auth failed, something is wrong")

from openinference.instrumentation.smolagents import SmolagentsInstrumentor

SmolagentsInstrumentor().instrument()

# ----------------------------
# Setup for lanfuse ends here
# ----------------------------

from smolagents import CodeAgent, InferenceClientModel

login()

# Tool to suggest a menut based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
            - "casual": menu suited for casual party
            - "formal": menu suited for formal party
            - "superhero": menu suited for superhero party
            - "custom": its a custom menu for things outside other categories
    """
    if occasion == "casual":
        return "Pizza, pancakes and sodas"
    elif occasion == "formal":
        return "3-course dinner with all the possible additions"
    elif occasion == "superhero":
        return "Buffet where everything is extra spicy"
    else:
        return "Custom menu thats made by head chief and butler" 

#agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=InferenceClientModel())
agent = CodeAgent(tools=[], model=InferenceClientModel(), 
                  additional_authorized_imports=['datetime'])

#agent.run("Search for the best music recommendations for a party at the Wayne's mansion")
#agent.run("Preapre a formal menu for the party")
agent.run(
        """
        Alfred needs to prepare for the party. Here are the tasks and their time:
        1. Making pancakes - 20 hours
        2. Counting Rasberries - 3000 hours
        3. Set up the menu and tables - 10000 hours
        4. Prepare music and playlist

        if we start right now, at what time will it be ready?
        """
        )
# Change to your username and repo name
#agent.push_to_hub('Thopterek/AlfredAgent')
