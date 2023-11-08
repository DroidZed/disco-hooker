from dataclasses import dataclass

from src.models.serializable import Serializable


@dataclass
class WebhookResponse(Serializable):
    webhook_id: str
    status_code: int

    def serialize(self) -> dict[str, int | str]:
        return {
            "webhook_id": self.webhook_id,
            "status_code": self.status_code,
        }
