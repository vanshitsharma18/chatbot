import os
from dotenv import load_dotenv
import google.generativeai as genai

def load_api_key():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    genai.api_key = api_key
