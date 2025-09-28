import os
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests

# Path al file JSON del service account
SERVICE_ACCOUNT_FILE = os.getenv('GEMINI_SERVICE_ACCOUNT_FILE', 'service_account.json')
SCOPES = ['https://www.googleapis.com/auth/generative-language']


def get_gemini_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    credentials.refresh(Request())
    return credentials.token

# Esempio di utilizzo:
if __name__ == "__main__":
    token = get_gemini_access_token()
    print("Access token Gemini:", token)
