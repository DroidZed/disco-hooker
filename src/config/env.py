from dataclasses import dataclass
from decouple import config


@dataclass
class Env:
    WEBHOOK_URL = f"{config('WEBHOOK_URL')}"
    PORT = int(f"{config('PORT', cast=int)}")
    REDIS_HOST = f"{config('REDIS_HOST')}"
    REDIS_PORT = int(f"{config('REDIS_PORT', cast=int)}")
