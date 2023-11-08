from dataclasses import dataclass
from typing import Optional

from src.models.serializable import Serializable
from src.models.webhook_response import WebhookResponse


@dataclass
class Result(Serializable):
    data: Optional[WebhookResponse] = None
    error: Optional[str] = None

    def serialize(self):
        return {
            "data": self.data.serialize(),  # type: ignore
            "error": self.error,
        }
