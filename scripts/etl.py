from my_module.read import read_some_file
from my_module.transforms import increase_salary, filter_logic
from my_module.write import write_results

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder.appName("simpleETL") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()


if __name__=="__main__":
    spark = SparkSession.builder.getOrCreate() # here you can configure spark as you wish
    
    # read files or load any configs
    df = read_some_file("/Users/guillermosanchez/company-info/example_pyspark_app/data/sample.csv", spark)

    # apply your business logic
    df = filter_logic(df)
    df = increase_salary(df)

    # write your results to a permanent storage like BQ
    write_results(df, "my_dataset.my_table")
