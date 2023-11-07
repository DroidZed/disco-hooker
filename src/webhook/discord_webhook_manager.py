from typing import Optional
from discord_webhook import (
    AsyncDiscordWebhook,
    DiscordEmbed,
)

from src.utils.consts import Consts
from src.webhook.webhook_manager import WebHookManager

from ..config import Env


class DiscordWebHookManager(WebHookManager):
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
        **fields: dict[str, str],
    ):
        _embed = DiscordEmbed(
            title=embed_title,
            description=embed_desc,
            color=color,
        )
        _embed.set_author(
            name=author_name,
            url="https://github.com/DroidZed",
            icon_url="https://avatars.githubusercontent.com/u/41507665",
        )
        _embed.set_timestamp()
        _embed.set_footer(
            text=footer,
            icon_url="https://www.jenkins.io/images/logos/nerd/nerd.png",
        )
        if embed_image:
            _embed.set_image(embed_image)
        if embed_thumbnail:
            _embed.set_thumbnail(embed_thumbnail)
        for name, value in fields.items():
            _embed.add_embed_field(
                name, value[name], inline=False
            )
        return _embed

    async def notify_channel(
        self,
        title: str,
        message: str,
        color: Optional[int] = 0,
        author_name: Optional[str] = "Captain Hook",
        footer: Optional[str] = "Get hooked!",
        **fields: dict[str, str],
    ):
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
            **fields,
        )

        webhook = AsyncDiscordWebhook(url=Env().WEBHOOK_URL)

        webhook.add_embed(_embed)

        return await webhook.execute()
