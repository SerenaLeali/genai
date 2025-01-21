import streamlit as st
from fpdf import FPDF
import io

def export_to_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Module 1: Inhalte
    if "module1_content" in st.session_state:
        content = st.session_state["module1_content"]
        pdf.cell(200, 10, txt="Modulo 1: Erstellter Inhalt", ln=True, align="C")
        pdf.multi_cell(0, 10, txt=f"Erstellter Inhalt:\n{content['generated_content']}")
        pdf.multi_cell(0, 10, txt=f"Hashtags: {', '.join(content['hashtags'])}")
        pdf.ln(10)

    # Module 2: Redaktionsplan
    if "module2_content" in st.session_state:
        content = st.session_state["module2_content"]
        pdf.cell(200, 10, txt="Modulo 2: Redaktionsplan", ln=True, align="C")
        pdf.multi_cell(0, 10, txt=f"Optimale Zeiten:\n{content['optimal_times']}")
        pdf.multi_cell(0, 10, txt=f"Tipps für die Community:\n{content['community_tips']}")
        pdf.ln(10)

    # Speichern der PDF-Datei
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

def app():
    st.title("Exportieren generierter Inhalte")

    st.write("Auf dieser Seite können Sie alle in den vorherigen Modulen erstellten Inhalte exportieren.")
    
    if st.button("Als PDF exportieren"):
        pdf_file = export_to_pdf()
        st.download_button(
            label="PDF herunterladen",
            data=pdf_file,
            file_name="generated_content.pdf",
            mime="application/pdf",
        )
