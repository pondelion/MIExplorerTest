import pandas as pd
import numpy as np
import boto3
from .base_datastore_helper import BaseDatastoreHelper
from ..utils.config_reader import AWSConfig


class S3Helper(BaseDatastoreHelper):

    def __init__(self):
        super(S3Helper, self).__init__()

    def save(
        self,
        df: pd.DataFrame,
        s3_path: str,
    ):
        if not isinstance(df, pd.DataFrame):
            raise TypeError('Only Pandas dataframe format are supported for now')

        df.to_csv(s3_path, header=True, index=False)

    def to_s3path(
        self,
        filepath: str
    ):
        s3_prefix = f's3://{AWSConfig.S3_BUCKET_NAME}/'
        s3_path = s3_prefix + (filepath[1:] if filepath[0] == '/' else filepath)
        return s3_path

    def read(
        self,
        tag: str,
    ):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(f'{AWSConfig.S3_BUCKET_NAME}')
        objs = bucket.meta.client.list_objects_v2(
            Bucket=bucket.name,
            Prefix=tag if tag[-1] == '/' else tag + '/'
        )

        files = {
            o.get('Key'): o.get('LastModified') for o in objs.get('Contents')
        }
        latest_file = list(files.keys())[np.argsort(list(files.values()))[-1]]

        s3_prefix = f's3://{AWSConfig.S3_BUCKET_NAME}/'
        s3_path = s3_prefix + latest_file
        df = pd.read_csv(s3_path)

        return df
