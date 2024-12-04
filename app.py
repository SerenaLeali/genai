# Importing the Streamlit package which is used to create web applications
import streamlit as st

# Importing custom modules for different pages of the application
from login import login_page
import main_page
import module_one
import module_two
import module_three
import module_four
import summary_page
import impressum_page

# Check if user is logged in
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False

# Route based on login status
if not st.session_state['user_logged_in']:
    login_page()
else:
    # Sidebar Navigation for Main Pages
    PAGES = {
        "Startseite": main_page,
        "Modul 1": module_one, # Optional: Nicht in die Sidebar aufnehmen
        "Modul 2": module_two,
        "Modul 3": module_three,
        "Modul 4": module_four,
        "Datenübersicht": summary_page,
        "Impressum": impressum_page,
    }

    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Seite auswählen", list(PAGES.keys()))

    # Dynamically execute selected page module
    try:
        PAGES[selection].app()
    except KeyError:
        st.error(f"Die Seite '{selection}' konnte nicht geladen werden. Stellen Sie sicher, dass die entsprechende Datei existiert.")

    # Logout Button
    if st.sidebar.button("Abmelden"):
        st.session_state['user_logged_in'] = False
        st.session_state.pop('company_profile', None)
        st.experimental_rerun()