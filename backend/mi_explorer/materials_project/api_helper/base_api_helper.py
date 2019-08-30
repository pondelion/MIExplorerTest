from abc import ABCMeta, abstractmethod
from typing import Dict
import requests
from ...utils.config_reader import Config
from ...utils.logger import Logger


class BaseApiHelper(ABCMeta):

    def __init__(self):
        self._API_URL_FMT = self._get_api_url_fmt()
        self._API_KEY = Config.API_KEY
        self._API_URL_FMT += f'?{self._API_KEY}'

    @abstractmethod
    def _get_api_url_fmt(self):
        raise NotImplementedError

    def api_call(
        self,
        kwargs: Dict[str, str]
    ) -> Dict:
        try:
            api_url = self._API_URL_FMT.format(**kwargs)
        except Exception as e:
            Logger.e(__class__, 'Failed to construct API url string.')
            raise e

        try:
            res = requests.get(api_url)
            res = res['response']
        except Exception as e:
            Logger.e(__class__, f'Failed to call api : f{api_url}')
            raise e

        return res
