import speaker
import os
from termcolor import colored
from pyowm import OWM
from dotenv import load_dotenv

load_dotenv()


def get_weather_info():
    weather_api_key = os.getenv("WEATHER_API_KEY")
    open_weather_map = OWM(weather_api_key)

    weather_manager = open_weather_map.weather_manager()
    observation = weather_manager.weather_at_place(os.getenv("CITY"))
    weather = observation.weather
    print(weather)

    status = weather.detailed_status
    temperature = weather.temperature('celsius')["temp"]
    temperature_feels_like = weather.temperature('celsius')["feels_like"]
    wind_speed = weather.wind()["speed"]
    pressure = int(weather.pressure["press"] / 1.333)

    # вывод логов
    print(colored("Weather in " + os.getenv("CITY") +
                  ":\n * Status: " + status +
                  "\n * Wind speed (m/sec): " + str(wind_speed) +
                  "\n * Temperature (Celsius): " + str(temperature) +
                  "\n * Pressure (mm Hg): " + str(pressure), "yellow"))

    speaker.speak(
        "Температура воздуха в городе " + os.getenv("CITY_RUS") + str(round(temperature)) + " градусов Цельсия")
    speaker.speak("Ощущается как " + str(round(temperature_feels_like)) + " градусов Цельсия")
    speaker.speak("Скорость ветра " + str(round(wind_speed)) + " метров в секунду")
    speaker.speak("Давление " + str(pressure) + " миллиметра ртутного столба")
