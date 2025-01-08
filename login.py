import streamlit as st

def login_page():
    st.title("Anmeldung")

    if 'user_logged_in' not in st.session_state:
        st.session_state['user_logged_in'] = False

    if not st.session_state['user_logged_in']:
        st.subheader("Bitte melden Sie sich an:")
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
