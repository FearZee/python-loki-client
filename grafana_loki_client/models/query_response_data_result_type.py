from enum import Enum


class QueryResponseDataResultType(str, Enum):
    STREAMS = "streams"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
