import os

os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-here-goes-your-public-key"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-here-goes-your-secret-key"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"

from langfuse import get_client

langfuse = get_client()

if langfuse.auth_check():
    print("Langfuse is ready and working!")
else:
    print("Auth failed, something is wrong")

from openinference.instrumentation.smolagents import SmolagentsInstrumentor

SmolagentsInstrumentor().instrument()

from smolagents import CodeAgent, InferenceClientModel

agent = CodeAgent(tools=[], model=InferenceClientModel())
alfred_agent = agent.from_hub('sergiopaniego/AlfredAgent', trust_remote_code=True)
alfred_agent.run("Give me the best playlist for a party at Wayne's mansion. The party idea is a 'villain masquerade' theme")

#Langfuse is ready and working!
#Traceback (most recent call last):
    #  File "/home/ndziadzi/aaa/hf_playground/trying_langfuse.py", line 20, in <module>
#    from smolagents import CodeAgent, InferenceClientModel, HfApiModel
#ImportError: cannot import name 'HfApiModel' from 'smolagents' (/home/ndziadzi/.local/lib/python3.10/site-packages/smolagents/__init__.py)
#3-F-8% python3 trying_langfuse.py
#Langfuse is ready and working!
#Fetching 14 files: 100%|█████████████████████████████████████████| 14/14 [00:00<00:00, 63550.06it/s]
#Traceback (most recent call last):
    #  File "/home/ndziadzi/aaa/hf_playground/trying_langfuse.py", line 23, in <module>
#    alfred_agent = agent.from_hub('sergiopaniego/AlfredAgent', trust_remote_code=True)
#  File "/home/ndziadzi/.local/lib/python3.10/site-packages/smolagents/agents.py", line 1064, in from_hub
#    return cls.from_folder(download_folder, **kwargs)
# File "/home/ndziadzi/.local/lib/python3.10/site-packages/smolagents/agents.py", line 1096, in from_folder
#    return cls.from_dict(agent_dict, **kwargs)
#  File "/home/ndziadzi/.local/lib/python3.10/site-packages/smolagents/agents.py", line 1741, in from_dict
#   return super().from_dict(agent_dict, **code_agent_kwargs)
# File "/home/ndziadzi/.local/lib/python3.10/site-packages/smolagents/agents.py", line 981, in from_dict
#    model_class = getattr(importlib.import_module("smolagents.models"), model_info["class"])
# AttributeError: module 'smolagents.models' has no attribute 'HfApiModel'. Did you mean: 'ApiModel'?

# -------------------------------------
# in short update your course on Agents
# -------------------------------------
# HfApiModel got replaced with HfApiModel
# ---------------------------------------
