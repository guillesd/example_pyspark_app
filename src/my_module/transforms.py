from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def filter_logic(df: DataFrame) -> DataFrame:
    """
    Given a DataFrame with salary information, this function returns filtered salaries
    bellow 100000$ a year.

    Parameters
    ----------
    df : pyspark.sql.DataFrame
        DataFrame with annual salary information of a company

    Returns
    -------
    pyspark.sql.DataFrame
        A DataFrame without the filtered records
    """
    return df.filter(col("annual_salary") > 100000)


def increase_salary(df: DataFrame) -> DataFrame:
    """
    Given a DataFrame with salary information, this function adds a column with
    the salary increases by summing 100000$ to the current salary.

    Parameters
    ----------
    df : pyspark.sql.DataFrame
        DataFrame with annual salary information of a company

    Returns
    -------
    pyspark.sql.DataFrame
        A DataFrame without added column new_annual_salary
    """
    return df.withColumn(colName="new_annual_salary", col=col("annual_salary") + 100000)
