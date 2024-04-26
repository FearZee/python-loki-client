from enum import Enum


class ServiceStateEnum(str, Enum):
    FAILED = "Failed"
    NEW = "New"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPING = "Stopping"
    TERMINATED = "Terminated"

    def __str__(self) -> str:
        return str(self.value)
