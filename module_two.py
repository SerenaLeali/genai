import streamlit as st
import openai

openai.api_key = "your-api-key-here"

def generate_content(prompt: str) -> str:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # oder "gpt-4"
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
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
        prompt = f"Empfehle die besten Zeiten für Social-Media-Posts für ein Unternehmen im Bereich {company_profile['industry']} mit der Zielgruppe: {company_profile['target_audience']}."
        optimal_times = generate_content(prompt)
        st.write("Empfohlene Posting-Zeiten:")
        st.write(optimal_times)

    st.markdown("---")

    st.subheader("Tipps für Community Management")
    st.markdown("xxx.")