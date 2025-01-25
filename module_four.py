import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def generate_gradient(img_width, img_height, color1, color2):
    """
    Erzeugt einen Hintergrund mit einem linearen Farbverlauf.
    """
    gradient = Image.new("RGB", (img_width, img_height), color=color1)
    draw = ImageDraw.Draw(gradient)
    for i in range(img_height):
        r = int(color1[0] + (color2[0] - color1[0]) * (i / img_height))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / img_height))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / img_height))
        draw.line([(0, i), (img_width, i)], fill=(r, g, b))
    return gradient

def add_banner(draw, img_width, text, font, banner_height=100, banner_color="black"):
    """
    Fügt ein dekoratives Banner mit Text hinzu.
    """
    # Rechteck des Banners
    draw.rectangle([0, img_width - banner_height, img_width, img_width], fill=banner_color)

    # Berechnung der Textgröße mit textbbox
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Berechnet die Koordinaten für die Positionierung des Textes in der Mitte des Banners
    text_x = (img_width - text_width) // 2
    text_y = img_width - banner_height + (banner_height - text_height) // 2

    # Zeichnet den Text zentriert in das Banner
    draw.text((text_x, text_y), text, fill="white", font=font)

def create_instagram_post(text, text_size, bg_color, logo_path=None, gradient_enabled=False, banner_text=None, banner_text_size=60, alignment="Zentriert", banner_height=100, banner_color="black", logo_position="Links"):
    """
    Erstellt ein Instagram-Bild mit Text, der nach den Wünschen des Nutzers ausgerichtet ist.
    """
    img_width, img_height = 1080, 1080

    # Bild mit einfarbigem oder verlaufendem Hintergrund erstellen
    if gradient_enabled:
        img = generate_gradient(img_width, img_height, (30, 144, 255), (255, 140, 0))
    else:
        img = Image.new("RGB", (img_width, img_height), color=bg_color)

    draw = ImageDraw.Draw(img)
    font_path = "C:\\Windows\\Fonts\\arial.ttf"  # Verwende den Windows-Pfad für Arial
    font = ImageFont.truetype(font_path, size=text_size)

    # Berechnet die Textgröße
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Bestimmung der Position anhand der Ausrichtung
    if alignment == "Zentriert":
        text_x = (img_width - text_width) // 2
        text_y = (img_height - text_height) // 2
    elif alignment == "Oben":
        text_x = (img_width - text_width) // 2
        text_y = 50  # Abstand vom oben
    elif alignment == "Unten":
        text_x = (img_width - text_width) // 2
        text_y = img_height - text_height - 50  # Abstand vom unten

    # Zeichnen von Text
    draw.text((text_x, text_y), text, fill="white", font=font)

    # Fügen Sie bei Bedarf ein dekoratives Banner hinzu
    if banner_text:
        add_banner(draw, img_width, banner_text, font, banner_height=banner_height, banner_color=banner_color)

    # Ein Logo hinzufügen (optional)
    if logo_path:
        logo = Image.open(logo_path).resize((200, 200))
        if logo_position == "Links":  # **Logo links positioniert**
            img.paste(logo, (50, 50), logo.convert("RGBA"))
        elif logo_position == "Rechts":  # **Logo rechts positioniert**
            img.paste(logo, (img_width - 250, 50), logo.convert("RGBA"))

    return img

def app():
    """
    Hauptfunktion der Streamlit-Seite.
    """
    st.title("Grafikgenerator für Social Media")
    st.subheader("Gestalten Sie Ihre Grafiken mit kreativen Optionen!")

    # Benutzereingabe
    text = st.text_area("Text des Beitrags", placeholder="Schreiben Sie hier Ihre Nachricht...")
    text_size = st.slider("Textgröße", min_value=20, max_value=120, value=60, step=5)  # Slider für BeitragsText
    bg_color = st.color_picker("Hintergrundfarbe", "#1E90FF")
    logo = st.file_uploader("Logo hochladen (optional)", type=["png", "jpg", "jpeg"])
    # Neue Kontrolle für die Position des Logos
    logo_position = st.radio("Position des Logos:", ["Links", "Rechts"])  # **Radio-Button für Logo-Position**
    gradient_enabled = st.checkbox("Hintergrund mit Farbverlauf aktivieren")
    banner_text = st.text_input("Bannertext (optional)")

    # Personalisierung von Banner und Text im Banner
    text_size = st.slider("Textgröße im Banner", min_value=20, max_value=120, value=60, step=5)
    banner_height = st.slider("Bannerhöhe", min_value=50, max_value=300, value=100, step=10)
    banner_color = st.color_picker("Bannerfarbe", "#000000")
    
    # Option zur Auswahl der Ausrichtung
    alignment = st.selectbox("Textausrichtung:", ["Zentriert", "Oben", "Unten"])

    if st.button("Beitrag generieren"):
        if not text.strip():
            st.error("Geben Sie den Text ein, um den Beitrag zu erstellen!")
        else:
            img = create_instagram_post(
                text=text,
                bg_color=bg_color,
                logo_path=logo,
                gradient_enabled=gradient_enabled,
                banner_text=banner_text,
                alignment=alignment,
                text_size=text_size,
                banner_height=banner_height,
                banner_color=banner_color,
                logo_position=logo_position, 
            )

            # Bild anzeigen
            st.image(img, caption="Post-Vorschau", use_column_width=True)

            # Bild im Speicher speichern
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Schaltfläche zum Herunterladen des Bildes
            st.download_button(
                label="Grafik herunterladen",
                data=buffer,
                file_name="post_instagram_kreativ.png",
                mime="image/png",
            )
