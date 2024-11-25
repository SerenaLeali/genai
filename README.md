# GenAI: Generative AI Application for Marketing

## Projektbeschreibung und Ziele

Dieses Projekt zielt darauf ab, eine generative KI-Anwendung zu entwickeln, die speziell Marketing- und Sales-Teams unterstützt. Die Anwendung nutzt GPT-Technologie, um personalisierte und kreative Inhalte zu generieren, wie beispielsweise Werbetexte, Produktbeschreibungen, Social-Media-Posts und mehr. Ziel ist es, Marketingprozesse effizienter und innovativer zu gestalten und gleichzeitig ethische Richtlinien zu wahren.

## Kernfunktionen

- **Inhalte generieren**: Erstellung von Texten basierend auf Benutzereingaben (z. B. Produktinformationen, Zielgruppe, Marketingziele).
- **Anpassungsmöglichkeiten**: Bearbeitung und Verfeinerung der generierten Inhalte innerhalb der Anwendung.
- **Speicher- und Exportoptionen**: Ergebnisse können als Text- oder PDF-Dateien gespeichert und exportiert werden.
- **Benutzerfreundliche Oberfläche**: Intuitive Benutzeroberfläche mit Feedback-Funktion und Fehlerbehandlung.
- **Zusatzfeatures**:
  - Automatische Hashtag-Generierung.
  - Intelligenter Redaktionsplan mit Best-Post-Zeiten.
  - Tipps für Community-Management.
  - Post-Ideen-Generator.
  - Caption Creator mit Tone Adjuster.

---

## Installation und Ausführung

### Voraussetzungen

- Python 3.8 oder höher
- Streamlit (für die Benutzeroberfläche)
- OpenAI API-Schlüssel (erforderlich)

### Installation

1. **Repository klonen**:
   ```bash
   git clone https://github.com/<your-username>/genai.git
   cd genai
   ```

2. **Virtuelle Umgebung erstellen**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **API-Schlüssel konfigurieren**:
   Erstellen Sie eine `.env`-Datei im Projektverzeichnis und fügen Sie Ihren OpenAI-API-Schlüssel hinzu:
   ```
   OPENAI_API_KEY=your_api_key
   ```

5. **Anwendung starten**:
   ```bash
   streamlit run app.py
   ```

---

## Verwendung

1. Starten Sie die Anwendung und geben Sie die benötigten Informationen ein:
   - **Produktinformationen**: Name, Eigenschaften, Zielgruppe.
   - **Marketingziele**: Ziel der generierten Inhalte (z. B. Verkaufsförderung, Reichweitensteigerung).

2. Klicken Sie auf **"Generieren"**, um Inhalte zu erstellen.

3. Bearbeiten Sie die Ergebnisse bei Bedarf direkt in der Benutzeroberfläche.

4. Speichern oder exportieren Sie die finalen Inhalte.

---

## Verwendete Prompt-Techniken

1. **Strukturierte Prompts**: Klare Eingabeaufforderungen, z. B.:
   - "Schreibe einen kreativen Werbetext für ein Produkt mit folgenden Eigenschaften: ..."
2. **Kreativitätssteuerung**: Anpassung von Parametern wie "Temperature" und "Max Tokens" zur Steuerung von Kreativität und Umfang der Texte.
3. **Iterative Verfeinerung**: Nutzung mehrerer Runden von Prompts, um Ergebnisse zu optimieren.
4. **Kontextmanagement**: Bereitstellung von Hintergrundinformationen, um personalisierte Inhalte zu erstellen.
5. **Ethik-Filter**: Integration von Richtlinien, um ethische und transparente Inhalte zu garantieren.

---

## Herausforderungen und Lerneffekte

### Herausforderungen

- **Prompt-Optimierung**: Sicherstellung, dass die generierten Inhalte spezifisch, kreativ und fehlerfrei sind.
- **Fehlerbehandlung**: Implementierung von Mechanismen, die den Benutzer bei fehlerhaften Eingaben unterstützen.
- **Ethische Aspekte**: Berücksichtigung von Datenschutz und Vermeidung irreführenden Marketings.

### Lerneffekte

- Praktische Erfahrung mit der Integration der OpenAI-API.
- Verbesserung von Prompt-Techniken für bessere Ergebnisse.
- Verständnis für Benutzerfreundlichkeit und ethische Prinzipien in KI-Anwendungen.

---

## Projektplan und Meilensteine

### Zeitplan und Verantwortlichkeiten

| **Aufgabe**                                             | **Verantwortlich**   | **Deadline**     |
|---------------------------------------------------------|-----------------------|------------------|
| Repository auf GitHub erstellen                         | Serena                | 10.11.2024       |
| Tabelle mit To-Dos und Deadlines erstellen              | Emilia                | 10.11.2024       |
| README.md-Datei schreiben                               | Mette                 | 22.11.2024       |
| GPT-Assistent implementieren                            | Alle                  | 29.11.2024       |
| Nutzung und Erklärung der Prompt-Techniken              | Alle                  | 13.12.2024       |
| Ethische Richtlinien berücksichtigen                    | Alle                  | 20.12.2024       |
| Benutzerfreundliche Oberfläche entwickeln               | Alle                  | 27.12.2024       |
| Fehlerbehandlung und Benutzerfeedback implementieren    | Alle                  | 10.01.2025       |
| Screencast-Video erstellen                              | Alle                  | 15.01.2025       |
| Repository-Link und Video hochladen                     | Alle                  | 27.01.2025       |

---

