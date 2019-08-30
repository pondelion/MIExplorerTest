import yaml
from .logger import Logger


def _load_mp_config(filepath: str='config/material_project.yml'):
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
