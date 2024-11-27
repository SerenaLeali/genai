# Importing the Streamlit package
import streamlit as st

def app():
    # Setting the title of the page
    st.title('ContentCraft - Das Marketingtool für Ihr Unternehmen')

    # Beschreibung der Hauptfunktionen
    st.subheader("Was bietet ContentCraft?")
    st.markdown("""
    - **Inhalte generieren**: Erstellen Sie ansprechende Texte basierend auf Ihren Angaben wie Produktinformationen, Zielgruppe und Marketingzielen.
    - **Anpassungsmöglichkeiten**: Bearbeiten und verfeinern Sie Inhalte direkt in der Anwendung.
    - **Speicher- und Exportoptionen**: Speichern Sie Ergebnisse als Text- oder PDF-Dateien.
    - **Benutzerfreundliche Oberfläche**: Eine intuitive UI mit Feedback-Funktion und Fehlerbehandlung.
    - **Direktes Posten**: Veröffentlichen Sie Inhalte direkt auf Social-Media-Plattformen.
    """)

    st.subheader("Zusatzfunktionen")
    st.markdown("""
    - Automatische Hashtag-Generierung
    - Intelligenter Redaktionsplan mit Best-Post-Zeiten
    - Tipps für Community-Management
    - Post-Ideen-Generator
    - Caption Creator mit Tone Adjuster
    - Kreative Post-Erstellung
    """)

    # Unternehmensprofil erstellen oder bearbeiten
    if 'company_profile' not in st.session_state:
        st.warning("Bitte erstellen Sie zuerst ein Unternehmensprofil, bevor Sie andere Funktionen nutzen.")
        with st.form(key='company_profile_form'):
            company_name = st.text_input("Unternehmensname", placeholder="z. B. Muster GmbH")
            industry = st.text_input("Branche", placeholder="z. B. Mode, Technologie, Dienstleistung")
            company_size = st.selectbox("Unternehmensgröße", ["Kleinunternehmen", "Mittelständisches Unternehmen", "Großunternehmen"])
            company_description = st.text_area("Beschreibung des Unternehmens", placeholder="Geben Sie eine kurze Beschreibung des Unternehmens ein.")
            usps = st.text_area("USPs (Unique Selling Points)", placeholder="z. B. Nachhaltigkeit, Premium-Qualität, Innovation")
            campaign_goals = st.text_area("Zielsetzungen der Kampagne", placeholder="z. B. Erhöhung der Markenbekanntheit, Erschließung neuer Märkte")
            target_age = st.slider("Alter der Zielgruppe", 18, 65, (25, 45), step=1)
            target_audience = st.text_area("Hauptzielgruppen des Unternehmens", placeholder="z. B. junge Erwachsene, technikaffine Personen")
            core_values = st.text_area("Kernwerte des Unternehmens", placeholder="z. B. Innovation, Nachhaltigkeit, Qualität")
            brand_personality = st.text_area("Markenpersönlichkeit und -werte", placeholder="z. B. kreativ, zuverlässig, innovativ")

            submit_button = st.form_submit_button("Unternehmensprofil erstellen")
            if submit_button:
                missing_fields = []
                if not company_name.strip():
                    missing_fields.append("Unternehmensname")
                if not industry.strip():
                    missing_fields.append("Branche")
                if not company_description.strip():
                    missing_fields.append("Beschreibung des Unternehmens")
                if not usps.strip():
                    missing_fields.append("USPs")
                if not campaign_goals.strip():
                    missing_fields.append("Zielsetzungen der Kampagne")
                if not target_audience.strip():
                    missing_fields.append("Hauptzielgruppen des Unternehmens")
                if not core_values.strip():
                    missing_fields.append("Kernwerte des Unternehmens")
                if not brand_personality.strip():
                    missing_fields.append("Markenpersönlichkeit und -werte")

                if missing_fields:
                    st.error(f"Bitte füllen Sie die folgenden Felder aus: {', '.join(missing_fields)}")
                else:
                    st.session_state['company_profile'] = {
                        "company_name": company_name,
                        "industry": industry,
                        "company_size": company_size,
                        "company_description": company_description,
                        "usps": usps,
                        "campaign_goals": campaign_goals,
                        "target_age": target_age,
                        "target_audience": target_audience,
                        "core_values": core_values,
                        "brand_personality": brand_personality,
                    }
                    st.success(f"Das Unternehmensprofil für '{company_name}' wurde erfolgreich erstellt!")
    else:
        st.success(f"Willkommen, {st.session_state['company_profile']['company_name']}!")
        st.subheader("Unternehmensprofil")
        with st.expander("Details des Unternehmensprofils anzeigen oder bearbeiten"):
            # Anzeigen des Profils
            profile = st.session_state['company_profile']
            company_name = st.text_input("Unternehmensname", value=profile["company_name"])
            industry = st.text_input("Branche", value=profile["industry"])
            company_size = st.selectbox("Unternehmensgröße", ["Kleinunternehmen", "Mittelständisches Unternehmen", "Großunternehmen"], index=["Kleinunternehmen", "Mittelständisches Unternehmen", "Großunternehmen"].index(profile["company_size"]))
            company_description = st.text_area("Beschreibung des Unternehmens", value=profile["company_description"])
            usps = st.text_area("USPs (Unique Selling Points)", value=profile["usps"])
            campaign_goals = st.text_area("Zielsetzungen der Kampagne", value=profile["campaign_goals"])
            target_age = st.slider("Alter der Zielgruppe", 18, 65, profile["target_age"], step=1)
            target_audience = st.text_area("Hauptzielgruppen des Unternehmens", value=profile["target_audience"])
            core_values = st.text_area("Kernwerte des Unternehmens", value=profile["core_values"])
            brand_personality = st.text_area("Markenpersönlichkeit und -werte", value=profile["brand_personality"])

            if st.button("Änderungen speichern"):
                st.session_state['company_profile'] = {
                    "company_name": company_name,
                    "industry": industry,
                    "company_size": company_size,
                    "company_description": company_description,
                    "usps": usps,
                    "campaign_goals": campaign_goals,
                    "target_age": target_age,
                    "target_audience": target_audience,
                    "core_values": core_values,
                    "brand_personality": brand_personality,
                }
                st.success("Das Unternehmensprofil wurde erfolgreich aktualisiert!")

    # Navigation zu Modulen nebeneinander
        st.subheader("Navigieren Sie zu:")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Modul 1"):
                if 'company_profile' not in st.session_state:
                    st.error("Bitte erstellen Sie zuerst ein Unternehmensprofil, bevor Sie diese Funktion nutzen.")
                else:
                    st.query_params.update(page="module_one")

        with col2:
            if st.button("Modul 2"):
                if 'company_profile' not in st.session_state:
                    st.error("Bitte erstellen Sie zuerst ein Unternehmensprofil, bevor Sie diese Funktion nutzen.")
                else:
                    st.query_params.update(page="module_two")

        with col3:
            if st.button("Modul 3"):
                if 'company_profile' not in st.session_state:
                    st.error("Bitte erstellen Sie zuerst ein Unternehmensprofil, bevor Sie diese Funktion nutzen.")
                else:
                    st.query_params.update(page="module_three")

        with col4:
            if st.button("Modul 4"):
                if 'company_profile' not in st.session_state:
                    st.error("Bitte erstellen Sie zuerst ein Unternehmensprofil, bevor Sie diese Funktion nutzen.")
                else:
                    st.query_params.update(page="module_four")