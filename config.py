import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    # Model names
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.0-pro")
    CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")
    # Prompt files per lingua
    PROMPT_PATH_IT = os.getenv("PROMPT_PATH_IT", "prompt_it.txt")
    PROMPT_PATH_EN = os.getenv("PROMPT_PATH_EN", "prompt_en.txt")
    # Lingua
    LANG = os.getenv("PROMPT_LANG", "it")
    # Other config
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    @staticmethod
    def get_prompt():
        path = Config.PROMPT_PATH_IT if Config.LANG == "it" else Config.PROMPT_PATH_EN
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return ""
