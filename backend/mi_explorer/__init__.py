import os
from .utils.config_reader import AWSConfig


os.environ["AWS_ACCESS_KEY_ID"] = AWSConfig.S3_ACCESS_KEY
os.environ["AWS_SECRET_ACCESS_KEY"] = AWSConfig.S3_SECERET_KEY
