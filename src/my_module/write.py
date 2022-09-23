from pyspark.sql import SparkSession, DataFrame

def write_results(df: DataFrame, output_table: str) -> None:
    df.write.format("delta") \
        .saveAsTable("anual_increases")