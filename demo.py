from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain_openai.chat_models import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "<OPENAI_KEY>"
os.environ["SERPAPI_API_KEY"] = "<SERPA_KEY>" # get your Serp API key here: https://serpapi.com/

ChatOpenAI.api_key = "<OPENAI_KEY>"
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("How much energy did wind turbines produce worldwide in 2022?")