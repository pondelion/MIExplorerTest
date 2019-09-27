from .base_crawler_runner import BaseCrawlerRunner


class SequentialCrawlerRunner(BaseCrawlerRunner):

    def __init__(self):
        super(SequentialCrawlerRunner, self).__init__()

    def run(self):
