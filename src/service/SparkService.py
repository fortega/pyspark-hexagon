from model.Config import Config
from pyspark.sql import DataFrame, SparkSession


def create_session(config: Config) -> SparkSession:
    if config.spark_master != None:
        return SparkSession.builder.master(config.spark_master).getOrCreate()
    else:
        return SparkSession.builder.getOrCreate()


def countValues(data: DataFrame, column_name: str = "value") -> DataFrame:
    return data.groupBy(column_name).count().orderBy(f"count")
