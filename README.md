
# CrewAI Weather Assistant

Python application that automates daily weather-based clothing advice for children, integrating AI and Telegram notifications. The workflow replicates a complex n8n automation:

- Daily trigger at 7:00 AM
- Fetch weather data from Google Weather API
- Analyze weather data with a CrewAI agent (custom prompt, memory)
- AI models: Gemini, Claude (API)
- Send advice to Telegram chats

## Project Structure

- `main.py` — Main scheduler and orchestrator

# Parents AI Assistant

Parents AI Assistant is a Python application designed to help parents with daily tasks and decisions, starting with weather-based clothing advice for children. The project is modular and ready to expand with new features to support parents in various aspects of family life.

## Features

- Daily scheduled advice at 7:00 AM (customizable)
- Weather-based clothing recommendations for nursery and kindergarten
- AI-powered suggestions (Gemini, Claude, extensible)
- Telegram notifications to one or more chats
- Internationalized prompts (Italian/English)
- Logging to console and file
- Easy to extend for future parent-assistant features

## Project Structure

- `main.py` — Main scheduler and orchestrator
- `crewai_agent.py` — AI agent logic and model selection
- `weather_api.py` — Weather data fetcher
- `telegram_bot.py` — Telegram notification sender
- `.env` — Secrets and configuration
- `.env.example` — Example environment file
- `requirements.txt` — Python dependencies

## Prerequisites

- Python 3.9+
- Telegram bot token (see below)
- Telegram chat IDs (see below)
- Weather API key (Google or other)
- Gemini API key (Google AI Studio)
- Claude API key (Anthropic)

### Telegram Bot Setup
1. Create a Telegram bot via [BotFather](https://t.me/BotFather):
	- Send `/newbot` and follow instructions to get your bot token.
2. Add your bot to the desired group or chat.
3. Obtain the chat ID:
	- Start a chat with your bot, then use the API (e.g. @userinfobot or via code) to get the chat ID.
	- For groups, you may need to send a message and inspect the chat ID via Telegram API or bot logs.
4. Add your bot token and chat IDs to `.env`:
	```
	TELEGRAM_TOKEN=your_bot_token
	TELEGRAM_CHAT_IDS=chatid1,chatid2
	```

### Weather API Key
1. Register for a Google Weather API key (or use another supported provider).
2. Add your API key to `.env`:
	```
	WEATHER_API_KEY=your_weather_api_key
	```

### Gemini & Claude API Keys
1. Gemini:
	- Sign up at [Google AI Studio](https://aistudio.google.com/) and generate an API key.
	- Add to `.env`:
	  ```
	  GEMINI_API_KEY=your_gemini_api_key
	  GEMINI_MODEL=gemini-1.0-pro
	  ```
2. Claude:
	- Register at [Anthropic](https://www.anthropic.com/) and generate an API key.
	- Add to `.env`:
	  ```
	  CLAUDE_API_KEY=your_claude_api_key
	  CLAUDE_MODEL=claude-3-sonnet-20240229
	  ```

## Quick Start

1. Fill in all required variables in `.env` (see above).
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Run the assistant:
	```bash
	python main.py
	```

## How It Works

Every day at 7:00 AM, Parents AI Assistant:
1. Fetches real weather data for your configured location.
2. Generates clothing advice for nursery and kindergarten children using AI (Gemini or Claude).
3. Sends formatted advice to the configured Telegram chats.

## Customization & Extensibility

- Prompts are internationalized (Italian/English) and can be edited in `prompt_it.txt` and `prompt_en.txt`.
- You can add new AI models by extending `crewai_agent.py` and registering them in the model registry.
- Logging is enabled to both console and `crewai_meteo.log` for monitoring and debugging.
- The project is designed to easily add new features for parents (e.g. reminders, health tips, event notifications).

## Example Output

### Italian (IT)
```
*Asilo nido*
Sarà una giornata davvero bella e soleggiata, con temperature fresche al mattino (circa 16-18°C) che saliranno gradualmente fino a raggiungere e superare i 20°C nel pomeriggio. Non ci sarà pioggia né vento.
- Body a maniche corte (come strato base)
- Maglietta a maniche lunghe leggera o una maglietta a maniche corte con un golfino/felpa facile da mettere e togliere, per gestire il cambio di temperatura
- Pantaloni lunghi comodi e morbidi
- Un cambio completo extra (body, maglietta, pantaloni)

*Scuola dell’infanzia*
Sarà una giornata splendida, con tanto sole e temperature che da fresche al mattino (circa 16-18°C) diventeranno piacevoli e sopra i 20°C nel pomeriggio. L'ideale per giocare all'aperto senza pioggia né vento!
- Maglietta a maniche corte
- Felpa leggera o giacchina aperta facile da mettere e togliere (per il mattino e i momenti meno caldi)
- Pantaloni lunghi leggeri (che permettono libertà di movimento)
- Cappellino per il sole
- Scarpe comode e adatte al gioco all'aperto
```

### English (EN)
```
*Nursery*
It will be a beautiful and sunny day, with cool temperatures in the morning (around 16-18°C) rising gradually to over 20°C in the afternoon. No rain or wind expected.
- Short-sleeved bodysuit (as a base layer)
- Light long-sleeved t-shirt or a short-sleeved t-shirt with a cardigan/sweatshirt easy to put on and take off, to manage temperature changes
- Comfortable long pants
- An extra complete change (bodysuit, t-shirt, pants)

*Kindergarten*
It will be a wonderful day, lots of sun and temperatures that start cool in the morning (around 16-18°C) and become pleasant and above 20°C in the afternoon. Perfect for outdoor play with no rain or wind!
- Short-sleeved t-shirt
- Light sweatshirt or open jacket easy to put on and take off (for the morning and cooler moments)
- Light long pants (allowing freedom of movement)
- Sun hat
- Comfortable shoes suitable for outdoor play
```

---

## Is it ready for open source?

Yes, Parents AI Assistant is ready to be published as open source on GitHub. It includes:
- Clear documentation in English
- Setup instructions and prerequisites for all integrations
- Example outputs
- Modular, extensible code structure
- Logging and error handling
- Internationalization support

Before publishing, double-check that no sensitive data (API keys, tokens) are present in the repository. Add a suitable open source license (e.g. MIT, Apache 2.0) and a `CONTRIBUTING.md` if you want to encourage community contributions.

---

Parents AI Assistant helps parents with daily decisions and tasks, starting with weather-based clothing advice, and is ready to grow with new features for families.