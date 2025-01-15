import streamlit as st

def app():
    st.title("Speicher & Export")
    st.subheader("Willkommen in Modul 3.")
    st.markdown("""
    **Ziel:** Vereinfachung der Bereitstellung und Veröffentlichung von Inhalten.

    **Funktionen:**
    - **Speicher- und Exportoptionen**: Ermöglicht die Speicherung von Ergebnissen in Text- oder PDF-Formaten.
    """)

    st.markdown("---")

    st.subheader("Unternehmensprofil")

    # Check if company_profile is available in session state
    if 'company_profile' in st.session_state:
        company_profile = st.session_state['company_profile']

        # Format company profile data as a plain text string
        company_profile_txt = "\n".join([f"{key}: {value}" for key, value in company_profile.items()])

        # Display company profile data using markdown for better readability
        st.markdown(f"""
```
{company_profile_txt}
```
""")

        # Create a button to download the company profile data as a .txt file
        st.download_button(
            label="Download",
            data=company_profile_txt,
            file_name='unternehmensprofil.txt',
            mime='text/plain',
        )
    else:
        st.warning("Keine Daten gefunden. Bitte erstellen Sie ein Unternehmensprofil auf der Hauptseite.")
