from my_module.transforms import filter_logic, increase_salary

from pyspark.sql import DataFrame, SparkSession
from pyspark_test import assert_pyspark_df_equal


def test_filter_logic(sample_df: DataFrame, spark: SparkSession):
    filtered_df = filter_logic(sample_df)
    expected_output = spark.createDataFrame(
        [{"worker_id": 9, "worker_name": "Jeff Bezos", "anual_salary": 50000000000}]
    )

    assert_pyspark_df_equal(filtered_df, expected_output)


def test_increase_salary(sample_df: DataFrame, spark: SparkSession):
    increased_df = increase_salary(sample_df)
    expected_output = spark.createDataFrame(
        [
            {
                "worker_id": 8,
                "worker_name": "Guillermo Sanchez",
                "anual_salary": 80000,
                "new_anual_salary": 180000,
            },
            {
                "worker_id": 9,
                "worker_name": "Jeff Bezos",
                "anual_salary": 50000000000,
                "new_anual_salary": 50000100000,
            },
        ]
    )

    assert_pyspark_df_equal(increased_df, expected_output)


# Test whole transformation block


def test_e2e_transform(sample_df: DataFrame, spark: SparkSession):
    actual_output = increase_salary(filter_logic(sample_df))
    expected_output = spark.createDataFrame(
        [
            {
                "worker_id": 9,
                "worker_name": "Jeff Bezos",
                "anual_salary": 50000000000,
                "new_anual_salary": 50000100000,
            }
        ]
    )
    assert_pyspark_df_equal(actual_output, expected_output)
