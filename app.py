# Importing the Streamlit package which is used to create web applications
import streamlit as st

# Importing custom modules for different pages of the application
from login import login_page
import main_page
import module_one
import module_two
import module_three
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
        "**Content-Generierung**": module_one,
        "**Planung & Management**": module_two,
        "**Speicher & Export**": module_three,
        "Impressum": impressum_page,
    }

    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Seite auswählen", list(PAGES.keys()))

    # Dynamically execute selected page module
    try:
        PAGES[selection].app()
    except KeyError:
        st.error(f"Die Seite '{selection}' konnte nicht geladen werden. Stellen Sie sicher, dass die entsprechende Datei existiert.")
