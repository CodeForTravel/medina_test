import environ


env = environ.Env()
env.read_env(".env")


CONSTANCE_BACKEND = "constance.backends.redisd.RedisBackend"
CONSTANCE_REDIS_CONNECTION = "redis://127.0.0.1:6379/1"


CONSTANCE_CONFIG = {
    "WEATHER_DATA":(
    '{\
    "main": "Clouds",\
    "temp": 34,\
    "temp_min": 30,\
    "temp_max": 40, \
    }',
    "Weather Condition",
    str,
    ),
}
