from abc import ABCMeta, abstractmethod
from typing import Callable, Dict
import threading


class BaseCrawler(metaclass=ABCMeta):

    def __init__(self):
        self._data = None

    def _crawl_worker(
        self,
        on_finish_callback: Callable[[Dict], None]=None,
        on_fail_callback: Callable[[str], None]=None,
    ):
        try:
            self._data = self._crawl()
        except Exception as e:
            if on_fail_callback is not None:
                on_fail_callback(e)
            return
        if on_finish_callback is not None:
            on_finish_callback(self._data)

    def crawl(
        self,
        async: bool=False,
        on_finish_callback: Callable[[Dict], None]=None,
        on_fail_callback: Callable[[str], None]=None,
    ):
        if async:
            threading.Thread(
                target=self._crawl_worker,
                args=([on_finish_callback, on_fail_callback])
            )
        else:
            self._data = self._crawl()

    @abstractmethod
    def _crawl(self):
        raise NotImplementedError
