
# CrewAI Weather Assistant — Copilot Instructions

- Project type: Python application for daily weather-based advice, AI integration, Telegram notifications
- Main language: Python 3.9+
- Key frameworks/libraries: requests, python-telegram-bot, schedule, google-generativeai, anthropic

## Prerequisites

- Python 3.9 or newer
- Telegram bot token (see README for setup)
- Telegram chat IDs (see README for how to obtain)
- Google Weather API key
- Gemini API key (Google AI Studio)
- Claude API key (Anthropic)

## Setup Steps

1. Fill in all required variables in `.env` (see README)
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## Key Features

- Daily scheduled execution at 7:00 AM
- Fetches weather data, generates advice via AI, sends to Telegram
- Supports Gemini and Claude models (extensible)
- Internationalized prompts (IT/EN)
- Logging to console and file

## Development Guidelines

- Use the current directory as project root
- Do not add media or external links unless requested
- Keep explanations concise and focused
- For extension development, use VS Code API tool only if relevant

## Documentation

- Ensure README.md and this file are up to date and in English
- Include setup instructions and prerequisites for all APIs and integrations
EXTENSION INSTALLATION RULES:
- Only install extension specified by the get_project_setup_info tool. DO NOT INSTALL any other extensions.

PROJECT CONTENT RULES:
- If the user has not specified project details, assume they want a "Hello World" project as a starting point.
- Avoid adding links of any type (URLs, files, folders, etc.) or integrations that are not explicitly required.
- Avoid generating images, videos, or any other media files unless explicitly requested.
- If you need to use any media assets as placeholders, let the user know that these are placeholders and should be replaced with the actual assets later.
- Ensure all generated components serve a clear purpose within the user's requested workflow.
- If a feature is assumed but not confirmed, prompt the user for clarification before including it.
- If you are working on a VS Code extension, use the VS Code API tool with a query to find relevant VS Code API references and samples related to that query.

TASK COMPLETION RULES:
- Your task is complete when:
  - Project is successfully scaffolded and compiled without errors
  - copilot-instructions.md file in the .github directory exists in the project
  - README.md file exists and is up to date
  - User is provided with clear instructions to debug/launch the project

Before starting a new task in the above plan, update progress in the plan.
-->
- Work through each checklist item systematically.
- Keep communication concise and focused.
- Follow development best practices.
- Use pyenv for the Python environment setup.