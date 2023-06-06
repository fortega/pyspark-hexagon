from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import explode, split
from port.ReaderPort import ReadPort


class TextReader(ReadPort):
    def read(self, spark: SparkSession, path: str) -> DataFrame:
        text = spark.read.text(paths=path)
        return text.withColumn(colName="value", col=explode(split(text.value, " ")))
