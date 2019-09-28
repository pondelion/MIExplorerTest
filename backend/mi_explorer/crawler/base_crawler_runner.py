from abc import ABCMeta, abstractmethod
from typing import List, Dict, Union
from .base_crawler import BaseCrawler
from ..utils.exception import throws


class BaseCrawlerRunner(metaclass=ABCMeta):

    def __init__(
        self,
        crawler: Union[BaseCrawler, List[BaseCrawler]]
    ):
        self._validate_crawler(crawler)

        if not isinstance(crawler, list):
            crawler = [crawler]

        self._crawlers = crawler

    @throws(Exception)
    def add_crawler(
        self,
        crawler: Union[BaseCrawler, List[BaseCrawler]]
    ):
        self._validate_crawler(crawler)

        if not isinstance(crawler, list):
            crawler = [crawler]

        self._crawlers += crawler

    @abstractmethod
    def run(self):
        raise NotImplementedError

    def _validate_crawler(
        self,
        crawler: Union[BaseCrawler, List[BaseCrawler]]
    ):
        if not isinstance(crawler, list):
            crawler = [crawler]

        for c in crawler:
            if not isinstance(crawler, BaseCrawler):
                raise TypeError('Only BaseCrawler based crawler can be abbed.')
