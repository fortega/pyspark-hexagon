from src.model.Config import Config
from pyspark.sql import SparkSession


def create_session(config: Config) -> SparkSession:
    if config.spark_master != None:
        return SparkSession.builder.master(config.spark_master).getOrCreate()
    else:
        return SparkSession.builder.getOrCreate()
