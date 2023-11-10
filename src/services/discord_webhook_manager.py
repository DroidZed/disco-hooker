from typing import Optional
from discord_webhook import (
    AsyncDiscordWebhook,
    DiscordEmbed,
)
from src.models import ErrorResponse

from src.utils.consts import Consts
from src.utils.singleton import Singleton

from ..config import Env


class DiscordWebHookManager(metaclass=Singleton):
    """A simple webhook management class containing all the necessary methods to send webhooks."""

    def __init__(self) -> None:
        super().__init__()

    def create_embed(
        self,
        embed_title: str,
        embed_desc: str,
        color: str,
        author_name: str,
        footer: str,
        embed_image: Optional[str],
        embed_thumbnail: Optional[str],
        fields: Optional[list[dict[str, str]]] = None,
    ) -> DiscordEmbed:
        _embed = DiscordEmbed(
            title=embed_title,
            description=embed_desc,
            color=color,
        )

        _embed.set_author(
            name=author_name,
            url="https://github.com/DroidZed/discord-webhook-manager",
            icon_url="https://avatars.githubusercontent.com/u/41507665",
        )

        _embed.set_thumbnail(
            "https://www.jenkins.io/images/logos/nerd/nerd.png"
        )

        _embed.set_timestamp()

        _embed.set_footer(text=footer)

        if embed_image:
            _embed.set_image(embed_image)

        if embed_thumbnail:
            _embed.set_thumbnail(embed_thumbnail)

        if fields:
            for field in fields:
                _embed.add_embed_field(
                    field["name"],
                    field["value"],
                    inline=False,
                )

        return _embed

    async def notify_channel(
        self,
        title: str,
        message: str,
        fields: Optional[list[dict[str, str]]] = None,
        color: Optional[int] = 0,
        author_name: Optional[str] = "DroidZed",
        footer: Optional[str] = "Get hooked!",
    ) -> Optional[ErrorResponse]:
        webhook = AsyncDiscordWebhook(url=Env().WEBHOOK_URL)

        embed_c = (
            Consts.FAIL_COLOR
            if color == 0
            else Consts.SUCCESS_COLOR
        )

        _embed = self.create_embed(
            title,
            message,
            embed_c,
            f"{author_name}",
            f"{footer}",
            None,
            None,
            fields,
        )

        webhook.add_embed(_embed)

        resp = await webhook.execute()

        if resp.status_code != 200:
            return ErrorResponse(error="Unauthorized")

        self.last_embed = _embed

        return None
