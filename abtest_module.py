import streamlit as st
import openai
from gpt_integration import generate_content

# Funktion zur Inhaltserstellung mit GPT-4 Chat-API
def generate_content(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Verwende das gpt-4 Modell
            messages=[{"role": "user", "content": prompt}],  # Chat-Modell erwartet eine Liste von Nachrichten
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()  # Der generierte Text wird zurückgegeben
    except Exception as e:
        return f"Fehler bei der Generierung des Inhalts: {e}"


def app():
    st.title("A/B-Test-Vorschläge")
    st.subheader("Erstellen Sie Varianten für Ihre Marketingstrategie")

    st.markdown("""
    *Funktion:*
    Erstellen Sie verschiedene Varianten eines Werbetextes, einer Überschrift oder einer Kampagne für A/B-Tests.
    Nutzen Sie GPT, um unterschiedliche Zielgruppen oder Ansätze anzusprechen.
    """)

    st.markdown("---")

    # Eingabefelder für den Nutzer
    product_or_service = st.text_input("Produkt oder Dienstleistung", placeholder="z. B. ein neues Smartphone, ein Reinigungsservice")
    goal = st.text_input("Ziel", placeholder="z. B. höhere Conversion-Rate, stärkere Markenbindung")
    target_audience = st.text_area("Zielgruppe", placeholder="Beschreiben Sie Ihre Zielgruppe, z. B. junge Erwachsene, Berufstätige")
    platform = st.text_input("Plattform", placeholder="z. B. Facebook, LinkedIn")

    if st.button("Varianten generieren"):
        if not product_or_service.strip() or not goal.strip() or not target_audience.strip() or not platform.strip():
            st.error("Bitte füllen Sie alle Felder aus, um Varianten zu generieren.")
        else:
            # GPT-Prompt erstellen
            prompt = f"""
            Erstelle zwei oder mehr Varianten eines Werbetextes für {product_or_service} mit dem Ziel, {goal} zu erreichen.
            Jede Variante sollte sich auf unterschiedliche Zielgruppen oder Ansätze konzentrieren.
            Achte darauf, dass die Texte klar, überzeugend und prägnant sind.
            Verwende folgende Informationen:
            Zielgruppe: {target_audience}, Plattform: {platform}.
            """

            try:
                # GPT nutzen, um Varianten zu generieren
                generated_variants = generate_content(prompt)

                st.markdown("### Generierte Varianten:")
                st.write(generated_variants)


            except Exception as e:
                st.error(f"Fehler bei der Generierung der Varianten: {e}")

    st.markdown("---")

    # Optional: Zusatzinformationen oder Tipps anzeigen
    st.info("Nutzen Sie diese Varianten, um Ihre Zielgruppe effektiv anzusprechen und A/B-Tests durchzuführen.")