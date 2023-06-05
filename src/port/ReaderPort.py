from pyspark.sql import SparkSession, DataFrame


class ReadPort:
    def read(self, spark: SparkSession, path: str) -> DataFrame:
        pass
