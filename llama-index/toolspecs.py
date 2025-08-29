# -----------
# Basic usage
# depends on:
# pip install llama-index-tools-google
# ------------------------------------
from llama_index.tools.google import GmailToolSpec

tool = GmailToolSpec()
tool_list = tool.to_tool_list()

# -----------------------------------
# to take a detailed veiw on the tool
# -----------------------------------
[(tool.metadata.name, tool.metadata.description) for tool in tool_spec_list]
