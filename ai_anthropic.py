import os
import requests

class AIModelAnthropic:
    def __init__(self, model_name=None):
        self.model_name = model_name or os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")
        self.api_url = os.getenv("CLAUDE_API_URL", "https://api.anthropic.com/v1/messages")
        self.api_key = os.getenv("CLAUDE_API_KEY")
        if not self.api_key:
            raise ValueError("[ERRORE] Configura CLAUDE_API_KEY nel file .env.")

    def generate(self, prompt):
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        payload = {
            "model": self.model_name,
            "max_tokens": 1024,
            "system": "Sei un assistente per genitori. Rispondi solo con testo umano, formato markdown, secondo le istruzioni fornite.",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            if "content" in result and isinstance(result["content"], list):
                return "\n".join([c.get("text", "") for c in result["content"]])
            else:
                return result.get("content", "")
        except Exception as e:
            return f"[ERRORE Claude] {str(e)}"
