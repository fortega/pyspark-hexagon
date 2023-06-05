from src.adapter.CsvReader import CsvReader
from src.service import ConfigService
from src.service import SparkService


def run():
    config = ConfigService.local()
    spark = SparkService.create_session(config)
    data = CsvReader().read(spark=spark, path=config.path)
    data.show(truncate=False)


if __name__ == "__main__":
    run()
