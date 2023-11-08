from typing import Any, Optional
from discord_webhook import (
    AsyncDiscordWebhook,
    DiscordEmbed,
)
from src.models.result import Result
from src.models.webhook_response import WebhookResponse

from src.utils.consts import Consts
from src.utils.singleton import Singleton

from ..config import Env


class DiscordWebHookManager(metaclass=Singleton):
    """A simple webhook management class containing all the necessary methods to send webhooks."""

    def __init__(self) -> None:
        super().__init__()
        self.last_embed: DiscordEmbed = DiscordEmbed()
        self.hooks: list[
            tuple[AsyncDiscordWebhook, str]
        ] = []

    def create_embed(
        self,
        embed_title: str,
        embed_desc: str,
        color: str,
        author_name: str,
        footer: str,
        embed_image: Optional[str],
        embed_thumbnail: Optional[str],
        fields: list[dict[str, str]],
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

        for field in fields:
            _embed.add_embed_field(
                field["name"], field["value"], inline=False
            )

        return _embed

    async def notify_channel(
        self,
        title: str,
        message: str,
        fields: list[dict[str, str]],
        color: Optional[int] = 0,
        author_name: Optional[str] = "DroidZed",
        footer: Optional[str] = "Get hooked!",
    ) -> Result:
        webhook = AsyncDiscordWebhook(url=Env().WEBHOOK_URL)

        self.hooks.append((webhook, f"{webhook.id}"))

        it_exists = self._get_embed(webhook, title)

        if it_exists is not None:
            return Result(error="Already defined!")

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
            return Result(error="Unauthorized")

        self.last_embed = _embed

        return Result(
            data=WebhookResponse(
                status_code=resp.status_code,
                webhook_id=f"{webhook.id}",
            )
        )

    async def update_channel(
        self,
        by_id: str,
        for_title: str,
        with_fields: list[dict[str, str]],
    ) -> Result:
        webhook = AsyncDiscordWebhook(
            url=Env().WEBHOOK_URL, id=by_id
        )

        embed = self._get_embed(webhook, for_title)

        if embed is None:
            return Result(error="Not found.")

        for field in with_fields:
            embed.update(field)

        webhook.remove_embeds()

        webhook.add_embed(embed)

        resp = await webhook.edit()

        if resp.status_code != 200:
            return Result(error="Unauthorized")

        return Result(
            data=WebhookResponse(
                status_code=resp.status_code,
                webhook_id=f"{webhook.id}",
            )
        )

    def _get_embed(
        self, webhook: AsyncDiscordWebhook, title: str
    ) -> Optional[dict[str, Any]]:
        return next(
            filter(
                lambda e: e["title"] == title,
                webhook.get_embeds(),
            ),
            None,
        )