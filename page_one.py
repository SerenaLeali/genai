# Importing the Streamlit package which is used to create web applications
import streamlit as st

# Defining the main function for the application
def app():
    # Setting the title of the page
    st.title('ContentCraft - Das Marketingtool für Unternehmen')

    # Beschreibung der Startseite
    st.write(
        "Willkommen bei ContentCraft! Nutzen Sie die Kraft der generativen KI, um Ihre Marketingstrategien zu optimieren. Unsere Funktionen helfen Ihnen dabei, kreative Inhalte zu erstellen, Ihr Unternehmensprofil zu analysieren und somit Ihre Zielgruppe effektiv zu erreichen. Probieren Sie es jetzt aus!"
    )

 # Anmelde- und Abmeldefunktion
    if 'user_logged_in' not in st.session_state:
        st.session_state['user_logged_in'] = False

    if not st.session_state['user_logged_in']:
        st.subheader("Anmeldung")
        with st.form(key='login_form'):
            username = st.text_input("Benutzername", placeholder="Geben Sie Ihren Benutzernamen ein")
            password = st.text_input("Passwort", type="password", placeholder="Geben Sie Ihr Passwort ein")
            login_button = st.form_submit_button("Anmelden")

            if login_button:
                if username == "admin" and password == "password":  # Beispielhafte Loginprüfung
                    st.session_state['user_logged_in'] = True
                    st.success("Erfolgreich angemeldet!")
                else:
                    st.error("Ungültige Anmeldedaten. Bitte versuchen Sie es erneut.")
    else:
        st.sidebar.success(f"Willkommen zurück, {st.session_state.get('username', 'Benutzer')}!")
        if st.sidebar.button("Abmelden"):
            st.session_state['user_logged_in'] = False
            st.session_state.pop('company_profile', None)
            st.warning("Sie wurden abgemeldet.")
            st.experimental_rerun()

 # Unternehmensprofil muss zuerst ausgefüllt werden
    if 'company_profile' not in st.session_state:
        st.warning("Bitte erstellen Sie zuerst ein Unternehmensprofil, bevor Sie andere Funktionen nutzen.")
        with st.form(key='company_profile_form'):
            # Text input field for company name
            company_name = st.text_input("Name des Unternehmens", placeholder="z. B. Muster GmbH")

            # Text area for company description
            company_description = st.text_area("Beschreibung des Unternehmens", placeholder="Geben Sie eine kurze Beschreibung des Unternehmens ein.")

            # Text area for marketing goals
            marketing_goals = st.text_area("Marketingziele", placeholder="z. B. Erhöhung der Markenbekanntheit, Steigerung des Umsatzes")

            # Text input for target audience
            target_audience = st.text_input("Zielgruppe", placeholder="z. B. junge Erwachsene, Technikbegeisterte")

            # Text area for core values
            core_values = st.text_area("Kernwerte des Unternehmens", placeholder="z. B. Innovation, Nachhaltigkeit, Qualität")

            # Button to submit the form
            submit_button = st.form_submit_button("Unternehmensprofil erstellen")

            # Check if the submit button was pressed
            if submit_button:
                if not company_name.strip():
                    st.error("Bitte geben Sie einen Namen für das Unternehmen ein.")
                else:
                    # Save the company profile data in the session state
                    st.session_state['company_profile'] = {
                        "company_name": company_name,
                        "company_description": company_description,
                        "marketing_goals": marketing_goals,
                        "target_audience": target_audience,
                        "core_values": core_values,
                    }

                    # Display a success message
                    st.success(f"Das Unternehmensprofil für '{company_name}' wurde erfolgreich erstellt!")

                    # Optionally display the created company profile details
                    with st.expander("Details des erstellten Unternehmensprofils"):
                        st.write(st.session_state['company_profile'])
    else:
  # Übersicht der Kernfunktionen
    st.subheader("Kernfunktionen")
    st.markdown("""
    - **Inhalte generieren**: Erstellen Sie ansprechende Texte basierend auf Ihren Angaben wie Produktinformationen, Zielgruppe und Marketingzielen.
    - **Anpassungsmöglichkeiten**: Bearbeiten und verfeinern Sie Inhalte direkt in der Anwendung.
    - **Speicher- und Exportoptionen**: Speichern Sie Ergebnisse als Text- oder PDF-Dateien.
    - **Benutzerfreundliche Oberfläche**: Eine intuitive UI mit Feedback-Funktion und Fehlerbehandlung.
    - **Direktes Posten**: Veröffentlichen Sie Inhalte direkt auf Social-Media-Plattformen.
    """)

      # Zusatzfeatures
    st.subheader("Zusatzfeatures")
    st.markdown("""
    - Automatische Hashtag-Generierung
    - Intelligenter Redaktionsplan mit Best-Post-Zeiten
    - Tipps für Community-Management
    - Post-Ideen-Generator
    - Caption Creator mit Tone Adjuster
    - Kreative Post-Erstellung
    """)

    # Navigation zu spezifischen Tools
    st.write("Wählen Sie eine der folgenden Optionen, um loszulegen:")
    if st.button("Inhalte generieren"):
        st.write("Hier können Sie Inhalte basierend auf Ihren Marketingzielen erstellen.")
        # Logik zum Weiterleiten zur Inhaltserstellung einfügen
    if st.button("User Persona erstellen"):
        st.write("Definieren Sie detaillierte User Personas für Ihre Zielgruppe.")
        # Logik zum Weiterleiten zur Persona-Erstellung einfügen
    if st.button("Social-Media-Post erstellen"):
        st.write("Erstellen und posten Sie kreative Inhalte direkt auf Social-Media-Plattformen.")
        # Logik zum Weiterleiten zur Social-Media-Post-Erstellung einfügen

   
# This part is for testing purposes if you run this script directly
if __name__ == "__main__":
    app()
