# Gemini Chatbot

Lightweight Streamlit frontend for Google's Gemini API (Gemini Pro). This project provides a minimal chat UI that sends messages to the Gemini model and displays responses.

## Contents
- `Gemini_Chatbot.py` — main Streamlit app and wrapper logic for calling the Gemini API.
- `.env` — store your `GEMINI_API_KEY` here (this file should be kept secret and is typically gitignored).
- `requirements.txt` — Python dependencies used by the app.

## Features
- Simple chat UI built with Streamlit.
- Maintains a conversation history within the session.
- Buttons to clear or export chat history.

## Requirements
- Python 3.9+ (recommended)
- Streamlit and the packages listed in `requirements.txt`.

## Setup (Windows PowerShell)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the `Gemini_Chatbot` folder with your API key:

```
GEMINI_API_KEY=your_api_key_here
```

Important: Do not commit your real API key to version control. The repository may already include `.gitignore` rules to exclude `.env`.

## Run the app
From the repository root or the `Gemini_Chatbot` folder run:

```powershell
streamlit run Gemini_Chatbot\Gemini_Chatbot.py
```

Then open the local Streamlit URL shown in the terminal (usually http://localhost:8501).

## Usage
- Type messages into the chat input to send them to the Gemini model.
- Use sidebar controls to clear history or export the conversation to a text file.

## Troubleshooting
- "GEMINI_API_KEY not found": ensure the `.env` file exists in `Gemini_Chatbot` and contains `GEMINI_API_KEY`.
- Dependency errors: confirm correct Python version and reinstall packages with `pip install -r requirements.txt`.
- Streamlit not found: ensure virtual environment is activated or install Streamlit globally if appropriate.

## Security & Notes
- Keep your API key secret. Rotate/revoke keys if they are accidentally exposed.
- This project is a simple demo and may send user-provided text to an external API—avoid sending sensitive data.

## License
Add a license file if you plan to publish this project publicly.

## Contact
For questions about this mini-project, check the source in `Gemini_Chatbot/Gemini_Chatbot.py` and `requirements.txt`.
