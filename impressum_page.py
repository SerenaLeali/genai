import streamlit as st

def app():
    st.title("Impressum")
    
    st.markdown("""
    ### Angaben gemäß § 5 TMG
    
    **ContentCraft**  
    Musterstraße 1  
    12345 Musterstadt
                
    ---

    ### Kontakt:  
    Telefon: 01234 567890  
    E-Mail: info@contentcraft.de  
    Web: [www.contentcraft.de](https://www.contentcraft.de)

    ---
                
    ### Geschäftsführer:  
    Max Mustermann
                
    ---

    ### Registereintrag:  
    Eintragung im Handelsregister.  
    Registergericht: Musterstadt  
    Registernummer: HRB 123456
                
    ---

    ### Umsatzsteuer-ID:  
    Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz: DE123456789
                
    ---

    ### Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV:  
    Max Mustermann  
    Musterstraße 1  
    12345 Musterstadt
    """)