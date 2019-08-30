import yaml


def _load_config(filepath: str='config/config.yml'):
    return yaml.load(open(filepath))


class _Config(type):
    config = _load_config()

    def __getattr__(cls, key: str):
        try:
            return cls.config[key]
        raise KeyError(f'No config value found for {key}')


class Config(metaclass=_Config):
    pass
