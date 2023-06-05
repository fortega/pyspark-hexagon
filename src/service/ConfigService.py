from model.Config import Config


def test() -> Config:
    config = Config(read_path="main.py",
                    write_path="out.csv",
                    spark_master="local[*]")
    return config
