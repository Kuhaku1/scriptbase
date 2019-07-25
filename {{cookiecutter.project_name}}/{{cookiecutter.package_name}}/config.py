from .helpers import env


config = {
    "REDIS_URL": env("REDIS_URL", cast=str)
}
