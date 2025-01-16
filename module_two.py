import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Lade die Umgebungsvariablen
load_dotenv()

# Setze deinen OpenAI API-Schlüssel aus der .env-Datei
openai.api_key = os.getenv('OPENAI_API_KEY')

# Funktion zur Inhaltserstellung mit GPT-4 Chat-API
def generate_content(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Verwende das gpt-4 Modell
            messages=[{"role": "user", "content": prompt}],  # Chat-Modell erwartet eine Liste von Nachrichten
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()  # Der generierte Text wird zurückgegeben
    except Exception as e:
        return f"Fehler bei der Generierung des Inhalts: {e}"

def app():
    st.title("Planung & Management")
    st.subheader("Willkommen in Modul 2.")
    st.markdown("""
    **Ziel:** Effektive Organisation und Planung von Inhalten.

    **Funktionen:**
    - **Intelligenter Redaktionsplan**: Hilft bei der zeitlichen Planung von Inhalten und gibt automatisierte Empfehlungen für optimale Veröffentlichungszeiten.
    - **Tipps für Community-Management**: Bietet praktische Ratschläge für den Umgang mit Kommentaren, Reaktionen und den Aufbau einer aktiven Community.
    """)
    
    st.markdown("---")
    # Intelligente Planerstellung und Community-Tipps
    st.subheader("Intelligenter Redaktionsplan")
    st.markdown("Planen Sie Ihre Inhalte mithilfe von automatisierten Vorschlägen für optimale Veröffentlichungszeiten, basierend auf Ihrer Zielgruppe und Branche.")
    
    if 'company_profile' in st.session_state:
        company_profile = st.session_state['company_profile']
        
        # Erstelle den Prompt für die Empfehlung der besten Posting-Zeiten basierend auf dem Unternehmensprofil
        prompt = f"""
        Empfehle die besten Zeiten für Social-Media-Posts für ein Unternehmen im Bereich {company_profile['industry']} 
        mit der Zielgruppe: {company_profile['target_audience']}.
        Berücksichtige dabei branchenübliche Verhaltensmuster und die Vorlieben der Zielgruppe.
        """
        # Generiere die optimalen Posting-Zeiten mit dem Custom GPT
        optimal_times = generate_content(prompt)
        
        # Zeige die empfohlenen Zeiten an
        st.write("Empfohlene Posting-Zeiten:")
        st.write(optimal_times)

    st.markdown("---")

    st.subheader("Tipps für Community Management")
    st.markdown("Erhalte nützliche Tipps zum Umgang mit Kommentaren und dem Aufbau einer aktiven Community.")

    if 'company_profile' in st.session_state:
        company_profile = st.session_state['company_profile']
        
        # Erstelle einen Prompt für die Tipps zum Community-Management
        prompt = f"""
        Gib praktische Tipps für das Community-Management für ein Unternehmen im Bereich {company_profile['industry']} 
        mit der Zielgruppe: {company_profile['target_audience']}. 
        Berücksichtige dabei, wie man effektiv mit Kommentaren und Reaktionen umgehen kann.
        """
        
        # Generiere Tipps mit dem Custom GPT
        community_tips = generate_content(prompt)
        
        # Zeige die Community-Tipps an
        st.write("Community-Management Tipps:")
        st.write(community_tips)

    st.markdown("---")
