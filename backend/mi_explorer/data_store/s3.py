import pandas as pd
import numpy as np
import boto3
from .base_datastore_helper import BaseDatastoreHelper
from ..utils.config_reader import AWSConfig


class S3Helper(BaseDatastoreHelper):

    def __init__(
        self,
        bucket_name: str=AWSConfig.S3_BUCKET_NAME,
    ):
        super(S3Helper, self).__init__()
        self._bucket_name = bucket_name

    def save(
        self,
        df: pd.DataFrame,
        s3_path: str,
    ) -> None:
        if not isinstance(df, pd.DataFrame):
            raise TypeError('Only Pandas dataframe format are supported for now')

        df.to_csv(s3_path, header=True, index=False)

    def to_s3path(
        self,
        filepath: str
    ) -> str:
        s3_prefix = f's3://{self._bucket_name}/'
        s3_path = s3_prefix + (filepath[1:] if filepath[0] == '/' else filepath)
        return s3_path

    def read(
        self,
        base_dir: str,
    ) -> pd.DataFrame:
        latest_file = self.get_latest_file(base_dir)

        df = pd.read_csv(latest_file)

        return df

    def get_latest_file(
        self,
        base_dir: str,
    ) -> str:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(f'{self._bucket_name}')
        objs = bucket.meta.client.list_objects_v2(
            Bucket=bucket.name,
            Prefix=base_dir if base_dir[-1] == '/' else base_dir + '/'
        )

        if 'Contents' not in objs:
            raise RuntimeError(f'No file found in specified path : {base_dir}')

        files = {
            o.get('Key'): o.get('LastModified') for o in objs.get('Contents')
        }
        latest_file = list(files.keys())[np.argsort(list(files.values()))[-1]]

        s3_prefix = f's3://{self._bucket_name}/'
        s3_path = s3_prefix + latest_file

        return s3_path
