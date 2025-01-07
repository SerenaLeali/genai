import streamlit as st

def app():
    st.title("Planung & Management")
    st.subheader("Effektive Organisation und Planung von Inhalten")
    st.markdown("""
    *Ziel:* Effektive Organisation und Planung von Inhalten.

    *Funktionen:*
    - *Intelligenter Redaktionsplan*: Hilft bei der zeitlichen Planung von Inhalten und gibt automatisierte Empfehlungen für optimale Veröffentlichungszeiten.
    - *Tipps für Community-Management*: Bietet praktische Ratschläge für den Umgang mit Kommentaren, Reaktionen und den Aufbau einer aktiven Community.
    """)

    st.markdown("---")

    # Redaktionsplan
    st.subheader("Intelligenter Redaktionsplan")
    st.markdown("Planen Sie Ihre Inhalte mithilfe von automatisierten Vorschlägen für optimale Veröffentlichungszeiten.")

    if 'company_profile' in st.session_state:
        company_profile = st.session_state['company_profile']

        # Automatisierte Empfehlungen für Veröffentlichungszeiten
        st.write(f"Basierend auf Ihrer Zielgruppe ({company_profile['target_audience']}) empfehlen wir folgende Veröffentlichungszeiten:")
        optimal_times = ["Montag, 8:00 Uhr", "Mittwoch, 12:00 Uhr", "Freitag, 18:00 Uhr"]
        st.write(optimal_times)

        st.markdown("---")

        # Community-Management-Tipps
        st.subheader("Tipps für Community-Management")
        st.markdown("""
        - *Reaktionen priorisieren:* Antworten Sie schnell auf Kommentare, um eine aktive Community aufzubauen.
        - *Positive Atmosphäre schaffen:* Danken Sie für positives Feedback und reagieren Sie angemessen auf Kritik.
        - *Hashtags und Markierungen nutzen:* Fördern Sie die Sichtbarkeit Ihrer Beiträge.
        """)
    else:
        st.warning("Kein Unternehmensprofil gefunden. Bitte erstellen Sie zuerst ein Profil.")