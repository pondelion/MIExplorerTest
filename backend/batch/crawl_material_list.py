import time
import argparse
import os
import sys
sys.path.append('..')
from mi_explorer.crawler import MaterialListCrawler
from mi_explorer.data_store.s3 import S3Helper
from mi_explorer.utils.logger import Logger
from mi_explorer.utils.config_reader import AWSConfig


def main(args):
    mlc = MaterialListCrawler(max_id=4)

    def finish_callback(data):
        try:
            Logger.d('material_crawl', data)
            s3_helper = S3Helper(
                bucket_name=AWSConfig.S3_BUCKET_NAME
            )
            s3_helper.save(
                df=data,
                s3_path=s3_helper.to_s3path(
                    os.path.join(
                        args.s3_savedir,
                        f'{time.strftime("%Y/%m/%d/%H/%M/%S/%Y%m%d_%H%M%S")}.csv'
                    )
                )
            )
            latest_file = s3_helper.get_latest_file(
                base_dir=args.s3_savedir
            )
            Logger.d('material_crawl', f'Saved data to {latest_file}')
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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--s3_savedir',
        help='S3 directory to save crawled data.',
        default='materials_project/material_list'
    )
    args = parser.parse_args()
    main(args)
