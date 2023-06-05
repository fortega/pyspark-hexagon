from pyspark.sql import DataFrame, SparkSession
from port.ReaderPort import ReadPort

class TextReader(ReadPort):
    def read(self, spark: SparkSession, path: str) -> DataFrame:
        return spark.read.text(paths=path, lineSep=" ")