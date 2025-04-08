# import os

# Import the load_dotenv function
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_openai import ChatOpenAI

load_dotenv()



llm = ChatOpenAI(model="gpt-4o", temperature=0.0)


class State(MessagesState):
    pass


def assistant(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": response}


workflow = StateGraph(State)

workflow.add_node("assistant", assistant)

workflow.add_edge(START, "assistant")
workflow.add_edge("assistant", END)

graph = workflow.compile()
