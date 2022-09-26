import pytest

from typing import Any
from pyspark.sql import SparkSession, DataFrame
from delta import configure_spark_with_delta_pip


@pytest.fixture
def spark() -> SparkSession:
    builder = (
        SparkSession.builder.appName("simpleETL")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )

    return configure_spark_with_delta_pip(builder).getOrCreate()


@pytest.fixture
def sample_df(spark: SparkSession) -> DataFrame:
    return spark.createDataFrame(
        [
            {"worker_id": 8, "worker_name": "Guillermo Sanchez", "anual_salary": 80000},
            {"worker_id": 9, "worker_name": "Jeff Bezos", "anual_salary": 50000000000},
        ]
    )
