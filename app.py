import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('gato_raton.png')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula.")
st.write('Snoopy, el icónico Beagle creado por Charles M. Schulz, debutó el 4 de octubre de 1950 en la tira cómica Peanuts. Conocido por su inmensa imaginación, duerme sobre su caseta, ama la cerveza de raíz y alterna entre ser un escritor o el "As de la Aviación" contra el Barón Rojo, representando una vía de escape fantástica. 
Erik Store
Erik Store
Aquí te detallamos los aspectos clave de la historia de Snoopy:
Orígenes: Nació en la granja de cachorros "Daisy Hill" y tuvo siete hermanos, entre ellos Spike y Belle. Aunque inicialmente fue propiedad de una niña llamada Lila, fue devuelto y finalmente adquirido por Carlitos (Charlie Brown).
Evolución: En sus inicios (1950), caminaba a cuatro patas y no tenía pensamientos articulados. Con el tiempo, comenzó a caminar erguido (1956) y a mostrar sus pensamientos en globos de diálogo (1952).
Alter Egos: Su gran imaginación le permite adoptar múltiples personalidades, siendo las más famosas:
El As de la Aviación: Luchando contra el Barón Rojo.
Joe Cool: Un estudiante universitario "genial" con gafas de sol.
Escritor: Intentando escribir la "gran novela americana".
Amigos y Familia: Su mejor amigo es el pájaro amarillo Emilio (Woodstock), quien apareció en 1966. Tiene claustrofobia, por lo que prefiere dormir en el techo de su caseta en lugar de dentro.
Legado: La última tira de Peanuts se publicó el 13 de febrero de 2000, poco después de la muerte de Schulz. Snoopy se convirtió en un símbolo de la cultura pop, apareciendo en los globos del desfile de Acción de Gracias de Macy's desde 1968. 
Erik Store
Erik Store´)
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
