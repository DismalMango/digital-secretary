from indexing import *
from pathlib import Path
import os
from nanobot.utils.helpers import ensure_dir, today_date
from threading import Lock

class DiaryStore:
    def __init__(self, workspace: Path):
        self.diary_dir = ensure_dir(workspace / "diary")
        self.chunker = Chunker()
        self.chroma_db = ChromaDB()
        self.lock = Lock()
        self.build_index()
        
    def query(self, query: str, n_results: int = 2) -> list[str]:
        return self.retriever.hybrid_query(query, n_results)
    
    def get_all_markdown_texts(self) -> list[str]:
        return [doc.read_text(encoding="utf-8") for doc in self.diary_dir.glob("*.md")]
    
    def convert_docs_to_corpus(self) -> None:
        self.corpus = self.chunker.chunk_markdown_texts(self.all_markdown_texts)
        
    def build_index(self) -> None:
        self.all_markdown_texts = self.get_all_markdown_texts()
        self.convert_docs_to_corpus()
        self.chroma_db.add_documents(self.corpus)
        self.vectorizer = Vectorizer(corpus=[doc.page_content for doc in self.corpus])
        self.bm25 = self.vectorizer.get_bm25(corpus=[doc.page_content for doc in self.corpus])
        self.retriever = Retriever(vectorizer=self.vectorizer, chroma_db=self.chroma_db)