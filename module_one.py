import streamlit as st
import openai
from gpt_integration import generate_content, generate_hashtags

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
    st.title("Content-Generierung")
    st.subheader("Willkommen in Modul 1.")
    st.markdown("""
    **Ziel:** Die Erstellung von individuell zugeschnittenen Inhalten, die Ihre Zielgruppe ansprechen.

    **Funktionen:**
    - **Kreative Inhalte**: Generieren von maßgeschneiderten Marketingtexten basierend auf den Unternehmensinformationen und spezifischen Zielen.
    - **Hashtag-Generierung**: Automatisches Erstellen von relevanten Hashtags für Social Media-Posts.
    - **Tone-Adjuster**: Passen Sie den Ton der generierten Inhalte an (z. B. humorvoll, informativ, formell).
    """)
    st.markdown("---")

    if 'company_profile' not in st.session_state:
        st.warning("Bitte erstellen Sie zuerst ein Unternehmensprofil, bevor Sie andere Funktionen nutzen.")
    else:
        st.success(f"Erstelle jetzt neue Inhalte für {st.session_state['company_profile']['company_name']}!")
        
        # Zeige die Unternehmensinformationen
        st.subheader("Ihre Daten")
        st.markdown(f"""
        **Branche:** {st.session_state['company_profile']['industry']}  
        **Zielgruppe:** {st.session_state['company_profile']['target_audience']}  
        **Zielsetzungen der Kampagne:** {st.session_state['company_profile']['campaign_goals']} 
        **Unternehmensgröße:** {st.session_state['company_profile']['company_size']}  
        **Beschreibung des Unternehmens:** {st.session_state['company_profile']['company_description']}  
        **USPs (Unique Selling Points):** {st.session_state['company_profile']['usps']}  
        **Zielsetzungen der Kampagne:** {st.session_state['company_profile']['campaign_goals']}  
        **Alter der Zielgruppe:** {st.session_state['company_profile']['target_age']}  
        **Hauptzielgruppen des Unternehmens:** {st.session_state['company_profile']['target_audience']}  
        **Markenpersönlichkeit und -werte:** {st.session_state['company_profile']['brand_personality']}  
        """)

        st.markdown("---")

        # Produktbeschreibung oder Dokument hochladen
        st.subheader("Produktbeschreibung")
        product_description = st.text_area("Beschreiben Sie das Produkt, das Sie bewerben möchten", placeholder="Geben Sie eine kurze Beschreibung des Produkts ein.")
        uploaded_file = st.file_uploader("Oder laden Sie ein Dokument hoch, das das Produkt beschreibt", type=["pdf", "txt"])

        if uploaded_file is not None:
            import PyPDF2
            pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
            text = ""
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extract_text()
            product_description = text

        if st.button("Inhalt generieren"):
            if not product_description:
                st.error("Bitte geben Sie eine Produktbeschreibung ein oder laden Sie ein Dokument hoch.")
            else:
                # Generiere den Content basierend auf den Unternehmensprofilinformationen und der Produktbeschreibung
                content_prompt = f"""
                Erstelle einen Marketingtext für ein Unternehmen im Bereich {st.session_state['company_profile']['industry']} 
                mit dem Ziel '{st.session_state['company_profile']['campaign_goals']}'.
                Die Zielgruppe sind {st.session_state['company_profile']['target_audience']}.
                Produktbeschreibung: {product_description}
                """
                generated_content = generate_content(content_prompt)  # Verwende die ursprüngliche Funktion
                
                st.write("Generierter Inhalt:")
                st.write(generated_content)

                # Möglichkeit zur Bearbeitung des generierten Inhalts
                edited_content = st.text_area("Bearbeiten Sie den generierten Inhalt", generated_content)

                if st.button("Speichern"):
                    st.session_state['generated_content'] = edited_content
                    st.success("Der Inhalt wurde erfolgreich gespeichert!")

        # Hashtags generieren
        if 'generated_content' in st.session_state:
            st.subheader("Hashtags generieren")
            hashtags = generate_hashtags(st.session_state['generated_content'])
            st.write("Generierte Hashtags:")
            hashtag_list = hashtags.split()[:5]  # Zeigt nur die ersten 5 Hashtags an
            st.write(', '.join(hashtag_list))

        st.markdown("---")

        # Drei Buttons für unterschiedliche Tonalitäten
        st.subheader("Tone-Adjuster")
        tone_choice = st.radio(
            "Wählen Sie den gewünschten Ton für den Text:",
            ("Formell", "Informell", "Humorvoll")
        )

        if st.button("Anpassen"):
            # Erstelle unterschiedliche Versionen des Textes je nach Ton
            if tone_choice == "Formell":
                adjusted_content = generate_content(f"Formuliere den folgenden Text in einem formellen Ton: {st.session_state['generated_content']}")
                st.write("Formelle Version:")
                st.write(adjusted_content)
                st.info("Empfohlen für LinkedIn oder professionelle Blogs.")
            elif tone_choice == "Informell":
                adjusted_content = generate_content(f"Formuliere den folgenden Text in einem informellen Ton: {st.session_state['generated_content']}")
                st.write("Informelle Version:")
                st.write(adjusted_content)
                st.info("Empfohlen für Facebook oder Instagram.")
            elif tone_choice == "Humorvoll":
                adjusted_content = generate_content(f"Formuliere den folgenden Text in einem humorvollen Ton: {st.session_state['generated_content']}")
                st.write("Humorvolle Version:")
                st.write(adjusted_content)
                st.info("Empfohlen für Twitter oder informelle Social-Media-Plattformen.")

#Für Seite 5 (Exportieren)                

if st.button("Speichern"):
    st.session_state["module1_content"] = {
        "generated_content": edited_content,  # Contenuto modificato dall'utente
        "hashtags": hashtag_list,  # Hashtag generati
    }
    st.success("Il contenuto è stato salvato con successo!")