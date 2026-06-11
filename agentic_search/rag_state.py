from typing import TypedDict


class GraphState(TypedDict):
    user_query: str
    retrieved_documents: list[str]
