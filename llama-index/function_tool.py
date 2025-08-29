# --------------------------------------
# Basic function tool in llama framework
# --------------------------------------
from llama_index.core.tools import FunctionTool

def get_weather(location: str) -> str:
    """
    Useful for getting the weather from a given location
    """
    print(f"Getting weather from {location}")
    return (f"The weather in {location} is as you can see")

tool = FunctionTool.from_defaults(
        get_weather,
        name="my_weather_tool",
        description="completly useless tool to gaslight user about weather"
        )
tool.call("Heilbronn")
