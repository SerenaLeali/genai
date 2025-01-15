import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Lade die Umgebungsvariablen
load_dotenv()

# Setze deinen OpenAI API-Schlüssel aus der .env-Datei
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_content(prompt: str) -> str:
    try:
        # Verwende den richtigen Chat-Modell-Endpunkt für gpt-4
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Verwende das gpt-4 Modell
            messages=[{"role": "user", "content": prompt}],  # Chat-API erwartet eine Liste von Nachrichten
            max_tokens=150,
            temperature=0.7
        )
        # Extrahiere den generierten Text aus der Antwort
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Fehler bei der Generierung des Inhalts: {e}"

def generate_hashtags(content: str) -> str:
    try:
        # Verwende den richtigen Chat-Modell-Endpunkt für gpt-4
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Verwende das gpt-4 Modell
            messages=[{"role": "user", "content": f"Generiere relevante Hashtags für diesen Inhalt: {content}"}],  # Chat-API erwartet eine Liste von Nachrichten
            max_tokens=50,
            temperature=0.6
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Fehler bei der Generierung der Hashtags: {e}"
