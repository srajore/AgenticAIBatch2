#import nest_asyncio
#nest_asyncio.apply()

import nest_asyncio
nest_asyncio.apply()

from typing import TypedDict
#from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from IPython.display import Image, display
from langgraph_util import show_graph


class RecipeState(TypedDict):
    cousine: str
    ingredients: str
    recipe: str

llm = ChatOllama(
    model="llama3.2:latest"
)

def list_ingredients(state:RecipeState):
    prompt= f"Give me a list of ingredients for a {state['cousine']} dish"
    state['ingredients']= llm.invoke(prompt).content
    return state

def write_recipe(state:RecipeState):
    prompt= f"Write a recipe for a {state['cousine']} dish using the following ingredients: {state['ingredients']}"
    state['recipe']= llm.invoke(prompt).content
    return state


graph = StateGraph(RecipeState)

graph.add_node("list_ingredients",list_ingredients)
graph.add_node("write_recipe",write_recipe)

#graph.add_edge(START, "list_ingredients")

graph.set_entry_point("list_ingredients")
graph.add_edge("list_ingredients","write_recipe")
graph.add_edge("write_recipe", END)

workflow = graph.compile()
#show_graph(workflow)

display(Image(workflow.get_graph().draw_mermaid_png()))