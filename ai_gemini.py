import os
from google import genai

class AIModelGemini:
    def __init__(self, model_name=None):
        self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("[ERRORE] Configura GEMINI_API_KEY nel file .env.")
        try:
            self.genai = genai
        except ImportError:
            raise ImportError("google-generativeai non installato o versione errata.")

    def generate(self, prompt):
        try:
            client = self.genai.Client()
            response = client.models.generate_content(
                model=self.model_name, contents=prompt
            )
            return response.text
        except Exception as e:
            return f"[ERRORE Gemini] {str(e)}"
