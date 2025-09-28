
import os
import time
import schedule
import logging
from dotenv import load_dotenv
from crewai_agent import run_agent
from weather_api import get_weather_data
from telegram_bot import send_telegram_message

# Configura logging su console e file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("crewai_meteo.log", encoding="utf-8")
    ]
)
TELEGRAM_CHAT_IDS = os.getenv('TELEGRAM_CHAT_IDS', '').split(',')
LATITUDE = os.getenv('LOCATION_LATITUDE', '45.333333')
LONGITUDE = os.getenv('LOCATION_LONGITUDE', '7.65')

def job():
    try:
        logging.info("Avvio job giornaliero CrewAI Meteo.")
        weather_json = get_weather_data(LATITUDE, LONGITUDE)
        logging.info(f"Dati meteo ricevuti: {weather_json}")
        advice = run_agent(weather_json)
        for chat_id in TELEGRAM_CHAT_IDS:
            try:
                send_telegram_message(chat_id, advice)
                logging.info(f"Messaggio Telegram inviato a chat_id {chat_id}.")
            except Exception as e:
                logging.error(f"Errore invio Telegram a {chat_id}: {e}")
    except Exception as e:
        logging.error(f"Errore nel job giornaliero: {e}")

schedule.every().day.at("07:00").do(job)

if __name__ == "__main__":
    logging.info("CrewAI Meteo Assistant avviato.")
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)
        except Exception as e:
            logging.error(f"Errore nel ciclo principale: {e}")
