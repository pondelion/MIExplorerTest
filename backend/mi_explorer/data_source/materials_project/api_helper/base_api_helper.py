from abc import ABCMeta, abstractmethod
from typing import Dict, List
import requests
import os
from ....utils.config_reader import MPConfig
from ....utils.logger import Logger


class BaseApiHelper(metaclass=ABCMeta):

    def __init__(self):
        self._API_URL_FMT = self._get_api_url_fmt()
        self._API_KEY = MPConfig.API_KEY
        self._API_URL_FMT += f'?API_KEY={self._API_KEY}'

    @abstractmethod
    def _get_api_url_fmt(self):
        raise NotImplementedError

    def fetch(
        self,
        kwargs: Dict[str, str]
    ) -> Dict:
        try:
            api_url = self._API_URL_FMT.format(**kwargs)
        except Exception as e:
            Logger.e(__class__, 'Failed to construct API url string.')
            raise e

        # Logger.d(api_url)

        try:
            res = requests.get(api_url)
        except Exception as e:
            Logger.e(__class__, f'Failed to call api : f{api_url}')
            raise e

        try:
            res = res.json()['response']
        except Exception as e:
            err_msg = 'Failed to parse response.\n'
            err_msg += res if isinstance(res, dict) else res.json()
            Logger.e(__class__, err_msg)
            raise e

        return res

    @abstractmethod
    def get_required_keywards(self) -> List[str]:
        pass
