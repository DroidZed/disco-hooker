from dataclasses import dataclass
from src.models.serializable import Serializable


@dataclass
class ErrorResponse(Serializable):
    error: str

    def serialize(self):
        return {
            "error": self.error,
        }
