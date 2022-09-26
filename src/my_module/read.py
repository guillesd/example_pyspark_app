from pyspark.sql import SparkSession, DataFrame

def read_some_file(path: str, spark: SparkSession) -> DataFrame:
    """
    Given a path it reads a csv file with a specific set of options.

    Parameters
    ----------
    path : str
        Path to the file (either local or s3)
    spark : pyspark.sql.SparkSession
        Spark session (either local or remote) 

    Returns
    -------
    pyspark.sql.DataFrame
        A DataFrame with the contents of the file read
    """
    return spark.read.options(header=True).csv(path=path)