from ..base_crawler import BaseCrawler


class VaspCrawler(BaseCrawler):

    def __init__(self, max_id=40000):
        super(VaspCrawler, self).__init__()
        self._MAX_ID = max_id

    def _crawl(self):
