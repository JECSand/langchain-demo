from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain_openai.chat_models import ChatOpenAI


class Agent:
    def __init__(self, config_json, provider, model_name, agent_type, verbose=True, agent_tools=None):
        self.providers = ["openai", "databricks"]
        if agent_tools is None:
            agent_tools = []
        self.agent_tools = agent_tools
        self.config = config_json
        if provider not in self.providers:
            raise Exception("invalid provider '{}'".format(provider))
        self.provider = provider
        self.model_name = model_name
        if self.provider == "openai":
            ChatOpenAI.api_key = self.config.get("OPENAI_API_KEY")
            llm = ChatOpenAI(model=model_name, temperature=0)
            tools = load_tools(self.agent_tools, llm=llm)
            self.agent = initialize_agent(tools, llm, agent=agent_type, verbose=verbose)

    def run_prompt(self, prompt):
        if self.agent:
            self.agent.run(prompt)
            return
        raise Exception("Agent is not initialized")
