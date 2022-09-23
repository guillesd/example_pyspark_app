from pyspark.sql import SparkSession, DataFrame

def read_some_file(path: str, spark: SparkSession) -> DataFrame:
    return spark.read.options(header=True).csv(path=path)