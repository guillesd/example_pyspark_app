from my_module.read import read_some_file
from my_module.transforms import increase_salary, filter_logic
from my_module.write import write_results

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from argparse import ArgumentParser

BUILDER = (
    SparkSession.builder.appName("simpleETL")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)


def main(input_path: str):
    """
    Runs the simple end-to-end ETL

    Parameters
    ----------
    input_path : str
        Input path of data file to read
    """
    spark = configure_spark_with_delta_pip(
        BUILDER
    ).getOrCreate()  # here you can configure spark as you wish

    # read files or load any configs
    df = read_some_file(input_path, spark)

    # apply your business logic
    df = filter_logic(df)
    df = increase_salary(df)

    # write your results to Delta
    write_results(df, "annual_increases")


if __name__ == "__main__":
    parser = ArgumentParser(description="Provide input for the ETL application")
    parser.add_argument(
        "--input-path", dest="input_path", help="input path of the data file"
    )
    args = parser.parse_args()
    main(args.input_path)
