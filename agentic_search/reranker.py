from pathlib import Path
from typing import Any

from loguru import logger

from agentic_search.constants import WORKSPACE_PATH

DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-base"
DEFAULT_RERANKER_CACHE_DIR = WORKSPACE_PATH / "models" / "huggingface"


class Reranker:
    def __init__(
        self,
        model_name: str = DEFAULT_RERANKER_MODEL,
        cache_dir: Path = DEFAULT_RERANKER_CACHE_DIR,
    ) -> None:
        self._model: Any | None = None
        self.model_name = model_name
        self.cache_dir = cache_dir

        try:
            from FlagEmbedding import FlagReranker

            self.cache_dir.mkdir(parents=True, exist_ok=True)
            self._model = FlagReranker(
                self.model_name,
                use_fp16=True,
                cache_dir=str(self.cache_dir),
            )
        except Exception as exc:
            logger.warning(
                f"Failed to load reranker model {self.model_name}; "
                f"falling back to hybrid retrieval without reranking: {exc}"
            )

    @property
    def model(self) -> Any | None:
        return self._model
