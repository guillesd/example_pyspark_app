from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def filter_logic(df: DataFrame) -> DataFrame:
    return df.filter(col('anual_salary') > 100000)

def increase_salary(df: DataFrame) -> DataFrame:
    return df.withColumn(colName='new_anual_salary', col=col('anual_salary')+100000)