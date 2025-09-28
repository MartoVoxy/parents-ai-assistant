
# Parents AI Assistant

Parents AI Assistant is a comprehensive Python application designed to help parents with daily tasks and decisions. Currently featuring weather-based clothing advice for children, the platform is built with a modular, extensible architecture to support future AI agents and tools for various aspects of family life.

## Current Features

- **Weather Assistant Agent**: Daily scheduled weather-based clothing advice at 7:00 AM (customizable)
- **Smart Recommendations**: AI-powered suggestions for nursery and kindergarten clothing
- **Multi-AI Support**: Integrates Gemini and Claude models (easily extensible)
- **Telegram Notifications**: Sends advice to one or more configured chats
- **Internationalization**: Support for Italian and English prompts
- **Comprehensive Logging**: Console and file logging for monitoring
- **Modular Architecture**: Ready for future parent-assistant features and agents

## Future Roadmap

Parents AI Assistant is designed to grow with additional agents and tools:
- **Health & Nutrition Agent**: Meal planning and health reminders
- **Schedule Assistant**: Family calendar management and activity suggestions
- **Educational Agent**: Learning activities and homework assistance
- **Emergency Assistant**: Quick access to important contacts and procedures
- **Budget Helper**: Family expense tracking and savings suggestions

## Project Structure

- `main.py` — Main scheduler and orchestrator
- `crewai_agent.py` — AI agent logic and model selection
- `weather_api.py` — Weather data fetcher
- `telegram_bot.py` — Telegram notification sender
- `ai_gemini.py` — Gemini AI integration
- `ai_anthropic.py` — Claude AI integration
- `config.py` — Configuration management
- `.env` — Secrets and configuration
- `requirements.txt` — Python dependencies
- `prompt_*.txt` — Internationalized prompt templates

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

## Contributing

Parents AI Assistant welcomes contributions! Whether you want to add new AI agents, improve existing features, or suggest new tools for parents, please see `CONTRIBUTING.md` for guidelines.

---

**Parents AI Assistant** — Your intelligent companion for family life, starting with weather advice and expanding to support parents in every aspect of raising children. Built with extensibility in mind, ready to grow with your family's needs.