import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def generate_gradient(img_width, img_height, color1, color2):
    """
    Genera uno sfondo con gradiente lineare.
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
    Aggiunge un banner decorativo con il testo.
    """
    # Disegna il rettangolo del banner
    draw.rectangle([0, img_width - banner_height, img_width, img_width], fill=banner_color)

    # Calcola la dimensione del testo usando textbbox
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calcola le coordinate per posizionare il testo centrato nel banner
    text_x = (img_width - text_width) // 2
    text_y = img_width - banner_height + (banner_height - text_height) // 2

    # Disegna il testo centrato nel banner
    draw.text((text_x, text_y), text, fill="white", font=font)

def create_instagram_post(text, bg_color, logo_path=None, gradient_enabled=False, banner_text=None, alignment="Centrato"):
    """
    Crea un'immagine Instagram con testo allineato in base alla scelta dell'utente.
    """
    img_width, img_height = 1080, 1080

    # Crea l'immagine con sfondo solido o gradiente
    if gradient_enabled:
        img = generate_gradient(img_width, img_height, (30, 144, 255), (255, 140, 0))
    else:
        img = Image.new("RGB", (img_width, img_height), color=bg_color)

    draw = ImageDraw.Draw(img)
    font_path = "/Library/Fonts/Supplemental/Arial.ttf"  # Percorso corretto per macOS
    font = ImageFont.truetype(font_path, size=60)

    # Calcola la dimensione del testo
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Determina la posizione in base all'allineamento
    if alignment == "Centrato":
        text_x = (img_width - text_width) // 2
        text_y = (img_height - text_height) // 2
    elif alignment == "In alto":
        text_x = (img_width - text_width) // 2
        text_y = 50  # Distanza dall'alto
    elif alignment == "In basso":
        text_x = (img_width - text_width) // 2
        text_y = img_height - text_height - 50  # Distanza dal basso

    # Disegna il testo
    draw.text((text_x, text_y), text, fill="white", font=font)

    # Aggiungi un banner decorativo, se richiesto
    if banner_text:
        add_banner(draw, img_width, banner_text, font)

    # Aggiungi un logo (opzionale)
    if logo_path:
        logo = Image.open(logo_path).resize((200, 200))
        img.paste(logo, (50, 50), logo.convert("RGBA"))

    return img

def app():
    """
    Funzione principale della pagina Streamlit.
    """
    st.title("Generatore di Grafiche per Instagram")
    st.subheader("Personalizza la tua grafica con opzioni creative!")

    # Input utente
    text = st.text_area("Testo del post", placeholder="Scrivi qui il tuo messaggio...")
    bg_color = st.color_picker("Colore di sfondo", "#1E90FF")
    logo = st.file_uploader("Carica il logo (opzionale)", type=["png", "jpg", "jpeg"])
    gradient_enabled = st.checkbox("Attiva sfondo gradiente")
    banner_text = st.text_input("Testo del banner (opzionale)")

    # Opzione per scegliere l'allineamento
    alignment = st.selectbox("Allineamento del testo:", ["Centrato", "In alto", "In basso"])

    if st.button("Genera Post"):
        if not text.strip():
            st.error("Inserisci del testo per generare il post!")
        else:
            img = create_instagram_post(
                text=text,
                bg_color=bg_color,
                logo_path=logo,
                gradient_enabled=gradient_enabled,
                banner_text=banner_text,
                alignment=alignment,
            )

            # Mostra l'immagine
            st.image(img, caption="Anteprima del Post", use_column_width=True)

            # Salva l'immagine in memoria
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Pulsante per scaricare l'immagine
            st.download_button(
                label="Scarica la grafica",
                data=buffer,
                file_name="post_instagram_creativo.png",
                mime="image/png",
            )
