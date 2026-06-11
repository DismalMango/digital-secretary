from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agentic_search.diary import DiaryStore
    from agentic_search.indexing import ChromaDB, Chunker, Retriever, Vectorizer

__all__ = ["DiaryStore", "Chunker", "Vectorizer", "ChromaDB", "Retriever"]


def __getattr__(name: str):
    if name == "DiaryStore":
        from agentic_search.diary import DiaryStore

        return DiaryStore

    if name in {"Chunker", "Vectorizer", "ChromaDB", "Retriever"}:
        indexing = import_module("agentic_search.indexing")
        return getattr(indexing, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
