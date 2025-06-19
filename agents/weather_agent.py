from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path("../.env"))
api_key = os.getenv("OPENWEATHER_API_KEY")
# We’ll import the singleton `mcp` instance from main later
# so here we just define a function that takes an MCP instance:
mcp=FastMCP("Weather")
@mcp.tool()
def get_weather(city: str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            description = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            return f"Weather in {city}: {description}, {temperature}°C"
        else:
            return f"Could not retrieve weather for {city}. Reason: {data.get('message', 'Unknown error')}."
    except Exception as e:
        return f"Error occurred while fetching weather data: {str(e)}"
@mcp.tool()
def get_forecast(city: str, days: int) -> str:
    return f"Weather Forecast: {city} for the next {days} days: Sunny with occasional clouds."

if __name__ == "__main__":
    mcp.run(
        transport="stdio"
    )