from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None):
    env = Env()
    env.read_env(path=path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))


def load_pay(path: str = None):
    env = Env()
    env.read_env(path=path)
    return env("YTOKEN")