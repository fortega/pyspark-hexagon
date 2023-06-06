from model.Config import Config
from os import environ as env


def test() -> Config:
    return Config(read_path="main.py",
                  write_path="out.csv",
                  spark_master="local[*]")


def env() -> Config:
    spark_master = "local[*]"
    if env["SPARK_ENV_LOADED"] == "1":
        spark_master = None
    return Config(read_path=env["IN"],
                  write_path=env["OUT"],
                  spark_master=spark_master)
