from .base_crawler_runner import BaseCrawlerRunner


class ParallelCrawlerRunner(BaseCrawlerRunner):

    def __init__(self):
        super(ParallelCrawlerRunner, self).__init__()

    def run(self):
