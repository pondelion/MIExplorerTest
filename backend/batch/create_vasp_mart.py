import sys
import time
import os
from pyspark.sql import SparkSession
sys.path.append('..')
from mi_explorer.data_store.s3 import S3Helper
from mi_explorer.utils.logger import Logger
from mi_explorer.utils.config_reader import AWSConfig


def main():
    merge_data_basedirs = [
        'materials_project/material_list',
        # 'materials_project/vasp/basic_properties'
    ]

    s3_helper = S3Helper(
        bucket_name=AWSConfig.S3_BUCKET_NAME
    )

    pdfs = [
        s3_helper.read(basedir) for basedir in merge_data_basedirs
    ]

    spark = SparkSession.builder.master('local').getOrCreate()
    sdfs = map(lambda pdf: spark.createDataFrame(pdf), pdfs)

    table_names = [
        basedir.replace('/', '_') for basedir in merge_data_basedirs
    ]
    map(
        lambda sdf, table_name: sdf.registerTempTable(table_name),
        zip(sdfs, table_names)
    )
    print(spark.sql('show tables').toPandas())

    s3_savedir = s3_helper.to_s3path(
        os.path.join(
            'materials_project/vasp_mart',
            f'{time.strftime("%Y/%m/%d/%H_%M_%S")}'
        )
    )

    query = f"""
      CREATE TABLE IF NOT EXISTS vasp_mart
        ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
        STORED AS TEXTFILE
        LOCATION '{s3_savedir}'
      AS SELECT
        t1.* {' '.join([f't{i+2}.*' for i in range(len(table_names[1:]))])}
      FROM {table_names[0]} t1
      {' '.join([f'LEFT JOIN {tbl_name} t{i+2} on t1.material_id = t{i+2}.materia_id' for i, tbl_name in enumerate(table_names[1:])])}
    """

    spark.sql(query)


if __name__ == '__main__':
    main()
