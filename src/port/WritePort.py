from pyspark.sql import DataFrame, SparkSession


class WritePort:
    def write(spark: SparkSession, data: DataFrame, path: str) -> None:
        pass
