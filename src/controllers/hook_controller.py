from typing import Any
from src.utils.singleton import Singleton

from src.services import DiscordWebHookManager


class HookController(metaclass=Singleton):
    async def send_hook(self, body: dict[str, Any]):
        result = (
            await DiscordWebHookManager().notify_channel(
                title=body["title"],
                message=body["msg"],
                color=body["status"],
                fields=body["jobs"],
            )
        )

        if result.data:
            return result.data

        else:
            return result.error

    async def update_embed(
        self, title: str, id: str, body: dict[str, Any]
    ):
        result = (
            await DiscordWebHookManager().update_channel(
                by_id=id,
                for_title=title,
                with_fields=body["new_jobs"],
            )
        )

        if result.data:
            return result.data

        else:
            return result.error
