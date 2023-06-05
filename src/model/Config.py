class Config:
    def __init__(self, read_path: str, write_path: str, spark_master: None | str):
        self.read_path = read_path
        self.write_path = write_path
        self.spark_master = spark_master

        assert(read_path is not None)
        assert(write_path is not None)