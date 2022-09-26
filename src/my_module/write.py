from pyspark.sql import SparkSession, DataFrame


def write_results(df: DataFrame, output_table: str) -> None:
    """
    Write the input DataFrame to a table in Delta format. The mode use is overwrite, meaning
    that previous results won't be kept.

    Parameters
    ----------
    df : pyspark.sql.DataFrame
    output_table : str
        Name of the output table to write the data to.
        If the table does not exist it will be created
    """
    df.write.format("delta").mode("overwrite").saveAsTable("annual_increases")
