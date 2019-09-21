import pandas as pd
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
