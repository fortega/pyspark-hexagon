from pyspark.sql import DataFrame, SparkSession
from port.WritePort import WritePort


class CsvWriter(WritePort):
    def write(spark: SparkSession, data: DataFrame, path: str) -> None:
        return data.write.mode("overwrite").csv(path=path)
