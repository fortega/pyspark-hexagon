from src.model.Config import Config

def local() -> Config:
    config = Config("local[*]")
    return config
        