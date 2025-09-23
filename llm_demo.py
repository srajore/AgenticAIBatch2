#! pip install langchain_community duckduckgo-search ddgs langchain_openai langchain-tavily
 
#from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
 
from langchain_openai import ChatOpenAI
 
from langchain.agents import create_openai_functions_agent, AgentExecutor
 
from langchain_community.tools import DuckDuckGoSearchRun
 
from langchain import hub

from dotenv import load_dotenv

load_dotenv(override=True)
 
search = DuckDuckGoSearchRun()
 
tavilySearch = TavilySearch(
    max_results=2,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)
 
tools=[search,tavilySearch]
 
llm =ChatOpenAI(model="gpt-4.1-mini")
 
#llm_with_tools = llm.bind_tools(tools)
 
#response = llm_with_tools.invoke("what is the current wether in Pune?")
 
 
 
#print(response)
 
# Pull a default functions agent prompt from the hub
prompt = hub.pull("hwchase17/openai-functions-agent")
 
agent = create_openai_functions_agent(llm, tools,prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
 
# Ask
response = agent_executor.invoke({"input": "who won Ind vs PAK  match on 21/09/2025?"})
print(response["output"])
 
 
 
#print(search.invoke("what is the current wether in Pune?"))
 
 
#llm = ChatOllama(model="llama3.2:latest")
 
#response = llm.invoke("what is the current wether in Pune?")
 
#print(response.content)
 