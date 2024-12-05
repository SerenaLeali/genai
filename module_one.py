import streamlit as st

def app():
    st.title("Content-Generierung")
    st.subheader("Willkommen in Modul 1.")
    st.markdown("""
    **Ziel:** Erstellung und Bearbeitung von Marketing-Inhalten.

    **Funktionen:**
    - **Post-Ideen-Generator**: Liefert kreative und relevante Vorschläge für Beiträge, die auf Zielgruppe und Marketingzielen basieren.
    - **Inhalte generieren**: Erzeugt Texte auf Basis von Angaben wie Produktinformationen, Zielgruppe und Marketingzielen.
    - **Anpassungsmöglichkeiten & Tone Adjuster**: Ermöglicht die direkte Bearbeitung der generierten Inhalte und bietet Optionen, den Ton anzupassen (formal, humorvoll, informativ etc.).
    - **Caption Creator**: Erstellt ansprechende Bildunterschriften, die individuell angepasst werden können.
    - **Automatische Hashtag-Generierung**: Generiert relevante und zielgerichtete Hashtags zur Optimierung der Beiträge.
    """)