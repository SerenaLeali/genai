import openai

def generate_content(prompt):
    try:
        response = openai.chat_completions.create(
            model="gpt-3.5-turbo",  # Verwende das passende Modell (z.B. gpt-3.5-turbo oder gpt-4)
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Fehler bei der Generierung des Inhalts: {e}")
        return None
