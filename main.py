import os
from langchain.agents import AgentType

from agents import Agent
from utils import get_configs

# os.environ["OPENAI_API_KEY"] = "<OPENAI_KEY>"
# os.environ["SERPAPI_API_KEY"] = "<SERPA_KEY>"  # get your Serp API key here: https://serpapi.com/

if __name__ == "__main__":
    conf = get_configs()
    for k, v in conf.items():
        os.environ[k] = v
    demo_agent = Agent(
        conf,
        "openai",
        "gpt-3.5-turbo",
        AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        True,
        ["serpapi", "llm-math"])
    demo_agent.run_prompt("How much energy did wind turbines produce worldwide in 2022?")
