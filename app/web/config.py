from dataclasses import dataclass
from typing import TYPE_CHECKING

from yaml import safe_load

if TYPE_CHECKING:
    from app.web.app import Application


@dataclass
class Config:
    username: str
    password: str


def setup_config(app: 'Application') -> None:
    with open('config/config.yaml', 'r') as config:
        raw_config = safe_load(config)

    app.config = Config(
        username=raw_config['credentials']['username'],
        password=raw_config['credentials']['password']
    )

