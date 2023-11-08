from dataclasses import dataclass
from decouple import config


@dataclass
class Env:
    WEBHOOK_URL = f"{config('WEBHOOK_URL')}"
    PORT = int(f"{config('PORT', cast=int)}")
