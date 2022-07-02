from huey.contrib.djhuey import periodic_task
from huey import crontab
from medina_test.apps.product.services import WeatherService

@periodic_task(crontab(minute="*/1"))
def task_fetch_weather_condition():

    try:
        service_obj =  WeatherService()
        service_obj.fetch_weather_data()
    except Exception as e:
        print(e)
