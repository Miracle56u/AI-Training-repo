import os
import requests

from dotenv import load_dotenv

load_dotenv()


def weather_tool(state):

    city = state["question"].replace(
        "weather in",
        ""
    ).strip()

    api_key = os.getenv("WEATHER_API_KEY")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={api_key}"
        f"&units=metric"
    )

    response = requests.get(url)

    data = response.json()

    if response.status_code != 200:
        return {
            "answer": f"Could not retrieve weather for {city}"
        }

    return {
        "answer":
            f"{city.title()}: "
            f"{data['main']['temp']}°C, "
            f"{data['weather'][0]['description']}"
    }