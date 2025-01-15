import streamlit as st
import openai

# Setzen Sie hier Ihren OpenAI API-Schlüssel ein
openai.api_key = ""

def generate_content(prompt: str) -> str:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Sie können auch "gpt-4" verwenden, wenn verfügbar
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Fehler bei der Generierung des Inhalts: {e}"

def generate_hashtags(content: str) -> str:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Sie können auch "gpt-4" verwenden, wenn verfügbar
            prompt=f"Generiere relevante Hashtags für diesen Inhalt: {content}",
            max_tokens=50,
            temperature=0.6
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Fehler bei der Generierung der Hashtags: {e}"

def app():
    st.title("ContentCraft: Planen und Erstellen von Marketing-Inhalten")
    st.subheader("Nutzen Sie KI zur Erstellung und Optimierung Ihrer Inhalte")

    st.markdown("""
    *Ziel:* Erstellen und Planen von Marketing-Inhalten und Social-Media-Posts mit Hilfe von KI.

    *Funktionen:*
    - *Inhaltserstellung*: Generieren Sie maßgeschneiderte Inhalte basierend auf spezifischen Anforderungen.
    - *Hashtag-Generierung*: Lassen Sie sich relevante Hashtags für Ihre Social-Media-Posts vorschlagen.
    """)

    st.markdown("---")

    # Eingabe für den Inhalt
    st.subheader("Inhalt generieren")
    content_prompt = st.text_area("Geben Sie Ihren Prompt für die Inhaltserstellung ein", 
                                "Erstelle einen Marketingtext für ein Unternehmen im Bereich Marketing, "
                                "das junge Erwachsene als Zielgruppe hat und mit dem Ziel arbeitet, die Markenbekanntheit zu steigern.")

    if st.button("Inhalt generieren"):
        # Inhalt generieren basierend auf dem Benutzer-Prompt
        generated_content = generate_content(content_prompt)
        st.write("Generierter Inhalt:")
        st.write(generated_content)

        # Bearbeitungsbereich für den generierten Inhalt
        edited_content = st.text_area("Bearbeiten Sie den generierten Inhalt", generated_content)

        if st.button("Speichern"):
            st.session_state['generated_content'] = edited_content
            st.success("Der Inhalt wurde erfolgreich gespeichert!")

    st.markdown("---")

    # Eingabe für Hashtags
    st.subheader("Hashtags generieren")
    if 'generated_content' in st.session_state:
        st.write("Generierte Hashtags basierend auf dem Inhalt:")
        hashtags = generate_hashtags(st.session_state['generated_content'])
        st.write(hashtags)
    else:
        st.warning("Generieren Sie zuerst Inhalte, um Hashtags zu erhalten.")

    st.markdown("---")

    # Abschlussbereich
    st.markdown("""
    **Hinweis**: Nutzen Sie die generierten Inhalte und Hashtags direkt in Ihren Marketingkampagnen, oder passen Sie diese weiter an.
    """)

