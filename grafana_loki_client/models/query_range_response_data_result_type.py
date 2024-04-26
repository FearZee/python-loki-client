from enum import Enum


class QueryRangeResponseDataResultType(str, Enum):
    MATRIX = "matrix"
    STREAMS = "streams"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
