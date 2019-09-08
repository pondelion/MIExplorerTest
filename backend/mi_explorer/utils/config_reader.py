import yaml
import os
from .logger import Logger


DEFAULT_FILEPATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..',
    'config/materials_project.yml'
)


def _load_mp_config(filepath: str=DEFAULT_FILEPATH):
    return yaml.load(open(filepath))


class _MPConfig(type):
    config = _load_mp_config()

    def __getattr__(cls, key: str):
        try:
            return cls.config[key]
        except Exception as e:
            Logger.e(__class__, f'No config value found for {key}')
            raise e


class MPConfig(metaclass=_MPConfig):
    pass
