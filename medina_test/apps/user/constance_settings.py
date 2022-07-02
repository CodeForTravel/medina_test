import environ


env = environ.Env()
env.read_env(".env")


CONSTANCE_BACKEND = "constance.backends.redisd.RedisBackend"
CONSTANCE_REDIS_CONNECTION = "redis://127.0.0.1:6379/1"


CONSTANCE_CONFIG = {
    "WEATHER_DATA":(
    '{\
    "main": "Clouds",\
    "temp": 307.18,\
    "temp_min": 307.18,\
    "temp_max": 307.18, \
    }',
    "Weather Condition",
    str,
    ),
}
