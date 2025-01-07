from dotenv import load_dotenv  # Importiere das dotenv-Modul
import openai
import os

# Lädt die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# API-Schlüssel aus der .env-Datei abrufen
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content(prompt):
    try:
        # Generiere den Inhalt mit der OpenAI API
        response = openai.chat_completions.create(
            model="gpt-3.5-turbo",  # Verwende das passende Modell (z.B. gpt-3.5-turbo oder gpt-4)
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Fehler bei der Generierung des Inhalts: {e}")
        return None
