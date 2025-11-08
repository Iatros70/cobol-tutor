import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env laden (liest deinen Key automatisch)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY fehlt. Bitte in .env eintragen!")

genai.configure(api_key=api_key)
print("API-Key erkannt:", api_key[:6] + "..." + api_key[-4:])

models = genai.list_models()
for m in models:
    if "generateContent" in getattr(m, "supported_generation_methods", []):
        print("-", m.name)
