from langchain_ollama.llms import OllamaLLM

class OllamaAdapter:
    """
    Adapter to make OllamaLLM compatible with LangGraph's create_react_agent.
    """
    def __init__(self, model="llama2", verbose=True):
        self.llm = OllamaLLM(model=model, verbose=verbose)

    def __call__(self, *args, **kwargs):
        if not args:
            raise ValueError("No prompt provided to LLM")
        prompt = args[0]

        # OllamaLLM expects a list of prompts
        result = self.llm.generate([prompt], **kwargs)
        # result.generations is a list of lists (one per prompt)
        return result.generations[0][0].text

    def bind_tools(self, tools, **kwargs):
        """
        Fake bind_tools for LangGraph.
        LangGraph calls this to attach tools; we just store them.
        """
        self.tools = tools
        return self