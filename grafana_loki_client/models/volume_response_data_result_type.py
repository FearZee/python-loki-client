from enum import Enum


class VolumeResponseDataResultType(str, Enum):
    STREAMS = "streams"
    VECTOR = "vector"

    def __str__(self) -> str:
        return str(self.value)
