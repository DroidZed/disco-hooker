from typing import Any
from src.utils.singleton import Singleton

from src.services import DiscordWebHookManager


class HookController(metaclass=Singleton):
    async def send_hook(self, body: dict[str, Any]):
        return await DiscordWebHookManager().notify_channel(
            title=body["title"],
            message=body["msg"],
            color=body["status"],
            fields=body["jobs"],
        )
