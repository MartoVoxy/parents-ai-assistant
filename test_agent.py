

from crewai_agent import run_agent
from weather_api import get_weather_data
import os

LATITUDE = os.getenv('LOCATION_LATITUDE', '45.333333')
LONGITUDE = os.getenv('LOCATION_LONGITUDE', '7.65')

print("Richiesta dati meteo reali...")
weather_json = get_weather_data(LATITUDE, LONGITUDE)
print("Dati meteo ricevuti:\n", weather_json)

print("\n---\nRisposta Gemini:\n")
result_gemini = run_agent(weather_json, model_type="gemini", model_name=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"))
print(result_gemini)

print("\n---\nRisposta Claude:\n")
result_claude = run_agent(weather_json, model_type="claude", model_name=os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229"))
print(result_claude)
