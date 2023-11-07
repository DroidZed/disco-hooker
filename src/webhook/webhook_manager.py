from typing import Optional
from src.utils.singleton import Singleton


class WebHookManager(metaclass=Singleton):
    def __init__(self) -> None:
        pass

    async def notify_channel(
        self,
        title: str,
        message: str,
        color: Optional[str],
        author_name: Optional[str],
        footer: Optional[str],
        **fields: dict[str, str],
    ):
        pass
