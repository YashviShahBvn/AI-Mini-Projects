import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure API
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# List all available models
print("Available models:")
print("-" * 50)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model: {model.name}")
        print(f"Display Name: {model.display_name}")
        print(f"Description: {model.description}")
        print("-" * 50)