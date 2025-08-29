# -----------------------------------
# Model Context Protocol, depends on:
# pip install llama-index-tools-mcp
# -----------------------------------
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

# considering there is MCP server running
mcp_client = BasicMCPClient("https address")
mcp_tool = McpToolSpec(client=mcp_client)

agent = await get_agent(mcp_tool)
agent_context = Context(agent)
