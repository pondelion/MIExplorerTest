import sys
sys.path.append('..')
import time
from threading import Lock
from mi_explorer.crawler import MaterialListCrawler
from mi_explorer.data_store.s3 import S3Helper
from mi_explorer.utils.logger import Logger


def main():
    mlc = MaterialListCrawler(max_id=4)

    def finish_callback(data):
        try:
            Logger.d('material_crawl', data)
            s3_helper = S3Helper()
            s3_helper.save(
                df=data,
                s3_path=s3_helper.to_s3path(
                    f'materials_project/material_list/{time.strftime("%Y%m%d_%H%M%S")}.csv'
                )
            )
        except Exception as e:
            Logger.e('material_crawl', f'Failed to save crawled data to s3 : {e}')

    def fail_callback(e):
        Logger.e('material_crawl', e)

    mlc.crawl(
        async_=True,
        on_finish_callback=finish_callback,
        on_fail_callback=fail_callback,
    ).join()

    Logger.i('material_crawl', 'finished')


if __name__ == '__main__':
    main()
