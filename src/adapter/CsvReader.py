from pyspark.sql import DataFrame, SparkSession
from src.port.ReaderPort import ReadPort


class CsvReader(ReadPort):
    def read(self, spark: SparkSession, path: str) -> DataFrame:
        return spark.read.csv(path=path)
