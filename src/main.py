from adapter.TextReader import TextReader
from adapter.CsvWriter import CsvWriter
from service import ConfigService
from service import SparkService


def run():
    config = ConfigService.test()
    spark = SparkService.create_session(config)

    reader = TextReader()
    raw = reader.read(spark=spark, path=config.read_path)

    count = SparkService.countValues(data=raw)
    count.show()
    
    writer = CsvWriter()
    writer.write(data=count, path=config.write_path)
    
    spark.stop()


if __name__ == "__main__":
    run()
