from enum import Enum


class Direction(str, Enum):
    BACKWARD = "backward"
    FORWARD = "forward"

    def __str__(self) -> str:
        return str(self.value)
