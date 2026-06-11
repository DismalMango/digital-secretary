from langgraph.graph import END, START, StateGraph

from agentic_search.rag_node import rag_node
from agentic_search.rag_router_func import needs_rag
from agentic_search.rag_state import GraphState

rag_flow = StateGraph(GraphState)

# add nodes
rag_flow.add_node("rag_node", rag_node)

# add conditional edges
rag_flow.add_conditional_edges(START, needs_rag, {True: "rag_node", False: END})

# add edges
rag_flow.add_edge("rag_node", END)

# compile
rag_graph = rag_flow.compile()
