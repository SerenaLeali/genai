# module_one.py
import streamlit as st
from gpt_integration import generate_content



def app():
    st.title("Content-Generierung")
    st.subheader("Erstelle kreative Marketing-Inhalte")
    st.markdown("""
    *Ziel:* Erstellung und Bearbeitung von Marketing-Inhalten.

    *Funktionen:*
    - *Post-Ideen-Generator*: Liefert kreative und relevante Vorschläge für Beiträge, die auf Zielgruppe und Marketingzielen basieren.
    - *Inhalte generieren*: Erzeugt Texte auf Basis von Angaben wie Produktinformationen, Zielgruppe und Marketingzielen.
    - *Anpassungsmöglichkeiten & Tone Adjuster*: Ermöglicht die direkte Bearbeitung der generierten Inhalte und bietet Optionen, den Ton anzupassen (formal, humorvoll, informativ etc.).
    - *Caption Creator*: Erstellt ansprechende Bildunterschriften, die individuell angepasst werden können.
    - *Automatische Hashtag-Generierung*: Generiert relevante und zielgerichtete Hashtags zur Optimierung der Beiträge.
    """)

    st.markdown("---")

    # Benutzerdefinierten Prompt erstellen
    company_profile = st.session_state.get("company_profile", None)
    if company_profile:
        prompt = f"Erstelle einen Marketingtext für ein Unternehmen im Bereich {company_profile['industry']} mit dem Ziel {company_profile['campaign_goals']}. Zielgruppe: {company_profile['target_audience']}."

        # Text generieren lassen
        generated_content = generate_content(prompt)

        st.write("Generierter Inhalt:")
        st.write(generated_content)

        # Benutzer kann Inhalt anpassen
        edited_content = st.text_area("Bearbeiten Sie den generierten Inhalt", generated_content)

        if st.button("Speichern"):
            st.session_state['generated_content'] = edited_content
            st.success("Der Inhalt wurde erfolgreich gespeichert!")
    else:
        st.warning("Kein Unternehmensprofil gefunden. Bitte erstellen Sie zuerst ein Profil.")
