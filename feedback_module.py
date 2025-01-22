import streamlit as st
import json
import os

# Funktion zum Laden der Feedback-Daten
def load_feedback():
    if not os.path.exists("feedback.json"):
        return []
    with open("feedback.json", "r") as file:
        return json.load(file)

# Funktion zum Speichern der Feedback-Daten
def save_feedback(feedback_data):
    with open("feedback.json", "w") as file:
        json.dump(feedback_data, file, indent=4)

def app():
    st.title("Feedback-Modul")
    st.subheader("Bewerten Sie unsere Anwendung")

    st.markdown("---")

    # Initialisiere feedback als leeres Dictionary
    feedback = {"rating": "", "suggestion": None}

    # Feedback-Bereich
    st.subheader("Wie bewerten Sie die Anwendung?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Daumen hoch 👍"):
            feedback = {"rating": "up", "suggestion": None}
            st.success("Danke für Ihr positives Feedback!")
    with col2:
        if st.button("Daumen runter 👎"):
            feedback = {"rating": "down", "suggestion": None}
            st.warning("Danke für Ihr Feedback! Bitte machen Sie Verbesserungsvorschläge unten.")

    # Verbesserungsvorschläge sammeln
    suggestion = st.text_area("Ihre Verbesserungsvorschläge", placeholder="Wie können wir die Anwendung verbessern?")
    if st.button("Feedback senden"):
        feedback = {
            "rating": feedback.get("rating", ""),
            "suggestion": suggestion if suggestion.strip() else None,
        }

        # Feedback-Daten laden, aktualisieren und speichern
        feedback_data = load_feedback()
        feedback_data.append(feedback)
        save_feedback(feedback_data)

        st.success("Vielen Dank für Ihr Feedback! Es wurde gespeichert.")

    st.markdown("---")

    # Optional: Feedback-Daten anzeigen (nur für Entwickler/Debugging)
    if st.checkbox("Gesammelte Feedbacks anzeigen"):
        feedback_data = load_feedback()
        st.json(feedback_data)
