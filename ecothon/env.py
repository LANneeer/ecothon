import environ

env = environ.Env(
    DEBUG=(bool, True),
)
environ.Env.read_env('.env')

__all__ = [env]
