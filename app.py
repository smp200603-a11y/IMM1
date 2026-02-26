import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")

image = Image.open('gato_raton.png')
st.image(image, width=350)

with st.sidebar:
    st.subheader("Escribe y/o selecciona texto para ser escuchado.")

# Crear carpeta temporal
try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula.")

st.write("""
Snoopy, el icónico Beagle creado por Charles M. Schulz, debutó el 4 de octubre de 1950 en la tira cómica Peanuts.
Conocido por su inmensa imaginación, duerme sobre su caseta, ama la cerveza de raíz y alterna entre ser un escritor
o el "As de la Aviación" contra el Barón Rojo, representando una vía de escape fantástica.

Aquí te detallamos los aspectos clave de la historia de Snoopy:

Orígenes:
Nació en la granja de cachorros "Daisy Hill" y tuvo siete hermanos, entre ellos Spike y Belle.
Aunque inicialmente fue propiedad de una niña llamada Lila, fue devuelto y finalmente adquirido por Carlitos (Charlie Brown).

Evolución:
En sus inicios (1950), caminaba a cuatro patas y no tenía pensamientos articulados.
Con el tiempo, comenzó a caminar erguido (1956) y a mostrar sus pensamientos en globos de diálogo (1952).

Alter Egos:
- El As de la Aviación: luchando contra el Barón Rojo.
- Joe Cool: estudiante universitario con gafas de sol.
- Escritor: intentando escribir la "gran novela americana".

Amigos y Familia:
Su mejor amigo es el pájaro amarillo Emilio (Woodstock), quien apareció en 1966.
Tiene claustrofobia, por lo que prefiere dormir en el techo de su caseta.

Legado:
La última tira de Peanuts se publicó el 13 de febrero de 2000.
Snoopy se convirtió en un símbolo de la cultura pop.
""")

st.markdown("¿Quieres escucharlo? Copia el texto")

text = st.text_area("Ingrese el texto a escuchar")

option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English")
)

if option_lang == "Español":
    lg = 'es'
else:
    lg = 'en'

def text_to_speech(text, lg):
    tts = gTTS(text=text, lang=lg)
    try:
        my_file_name = text[:20].replace(" ", "_")
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name

if st.button("Convertir a Audio"):
    if text.strip() == "":
        st.warning("Por favor ingrese un texto.")
    else:
        result = text_to_speech(text, lg)
        with open(f"temp/{result}.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.markdown("## Tu audio:")
        st.audio(audio_bytes, format="audio/mp3")

        bin_str = base64.b64encode(audio_bytes).decode()
        href = f'<a href="data:audio/mp3;base64,{bin_str}" download="{result}.mp3">Descargar audio</a>'
        st.markdown(href, unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*.mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

remove_files(7)
