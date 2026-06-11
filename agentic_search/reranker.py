from FlagEmbedding import FlagReranker


class Reranker:
    def __init__(self):
        self._model = FlagReranker(
            "BAAI/bge-reranker-large",
            use_fp16=True,
        )

    @property
    def model(self) -> FlagReranker:
        return self._model
