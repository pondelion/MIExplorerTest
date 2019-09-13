import pandas as pd
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import SparkSession
from .base_datastore_helper import BaseDatastoreHelper
from ..utils.config_reader import AWSConfig


spark = SparkSession.builder.master('local').getOrCreate()
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", AWSConfig.S3_ACCESS_KEY)
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", AWSConfig.S3_SECRET_KEY)


class S3Helper(BaseDatastoreHelper):

    def __init__(self):
        super.__init__()

    def save(
        self,
        df: pd.DataFrame,
        s3_path: str,
    ):
        if not isinstance(df, pd.DataFrame) and  \
                not isinstance(df, SparkDataFrame):
            raise TypeError('Only Pandas/Spark dataframe format are supported for now')

        if isinstance(df, pd.DataFrame):
            df = spark.createDataFrame(df)

        df.write.mode('overwrite').parquet(s3_path, header=True)
