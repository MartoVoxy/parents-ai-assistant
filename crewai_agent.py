

import json
from config import Config
from ai_gemini import AIModelGemini
from ai_anthropic import AIModelAnthropic
from typing import Dict, Type
import logging
logging.basicConfig(level=logging.INFO)

class AIModelRegistry:
    registry: Dict[str, Type] = {
        "gemini": AIModelGemini,
        "claude": AIModelAnthropic,
    }

    @classmethod
    def register(cls, name: str, model_cls: Type):
        cls.registry[name] = model_cls
        logging.info(f"Registered AI model: {name}")

    @classmethod
    def get_model(cls, name: str):
        return cls.registry.get(name)

def run_agent(weather_json, model_type=None, model_name=None):
    """
    Genera il prompt per l'AI e invia la richiesta al modello Gemini, Claude o altri modelli registrati.
    Restituisce la risposta formattata.
    """
    prompt = f"{Config.get_prompt()}\n\nDati meteo:\n{json.dumps(weather_json, ensure_ascii=False)}"
    model_type = model_type or Config.GEMINI_MODEL or "gemini"
    model_name = model_name or None
    model_cls = AIModelRegistry.get_model(model_type)
    if not model_cls:
        return f"[ERRORE] Modello AI '{model_type}' non configurato."
    ai = model_cls(model_name)
    return ai.generate(prompt)