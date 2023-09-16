"""
ReQurv s.r.l.

This module provides the tools to manage multilanguage audio guide with text-to-speech using streamlit.
 """

import streamlit as st
from googletrans import Translator
from elevenlabs import generate, set_api_key
from PIL import Image

# GLOBALS
sample_rate = 44100
translator = Translator()
st.set_page_config(layout="wide", page_icon="🌍", page_title="Chat-Bot Bandi Beta")
st.title("Multilanguage audio guide with :violet[text-to-speech]")
st.markdown(
    """
    <h2 style='text-align: center;'>Genera la tua audio guida personale in 4 lingue in meno di un minuto
    🇮🇹 🇬🇧 🇩🇪 🇨🇵 </h1>
    """,
    unsafe_allow_html=True,
)
st.divider()
# Contact
with st.sidebar:
    image = Image.open("./ReQurv.jpg")
    st.image(image, caption="ReQurv.io")
    st.markdown(
        """
                <h3>ReQurv è una società di sviluppo di software innovativi.</h3>
                <p> Ci occupiamo di <b>innovazione</b> e creaimo progetti su misura
                per imprese e attivit' che vogliono fare utlizzare strumenti di AI
                per la crescita delle proprie attività<br/>
                Se vuoi parlare con noi questi sono si nostri contatti:
                """,
        unsafe_allow_html=True,
    )
    st.write(
        "📬 Contact",
        "**ReQurv.io:**",
        "[ReQurv](https://requrv.io)",
    )

    st.write("**Mail** : info@requrv.io")
    st.write("**Claudio Pacini** : claudio.pacini@requrv.io")
    st.write("**Enzo La Rosa** : enzo.larosa@requrv.io")

# INPUT AUDIO GUIDE
it = st.text_area(
    "Audio guida in italiano",
    value="",
    placeholder="Inserisci il testo per creare la audio guida",
)

translateBtn = st.button(
    "Traduci",
    key=None,
    help=None,
    args=None,
    kwargs=None,
    type="primary",
    disabled=False,
    use_container_width=False,
)
if translateBtn:
    if it == "":
        st.warning("Non hai inserito nessun testo")
    else:
        en_translated = translator.translate(it, src="it", dest="en")
        st.subheader("English version")
        st.write(str(en_translated.text))

        de_translated = translator.translate(it, src="it", dest="de")
        st.subheader("German version")
        st.write(str(de_translated.text))

        fr_translated = translator.translate(it, src="it", dest="fr")
        st.subheader("French  version")
        st.write(str(fr_translated.text))

        # AUDIO
        itAudio = generate(text=it, voice="Matilda", model="eleven_multilingual_v1")
        st.write("Italiano", format="audio/mpeg")
        st.audio(itAudio)
        st.download_button(
            label="Download Audio MP3 in Italiano",
            data=itAudio,
            file_name="Italiano.mp3",
            mime="audio/mpeg",
        )
        enAudio = generate(
            text=en_translated.text, voice="Matilda", model="eleven_multilingual_v1"
        )
        st.write("English")
        st.audio(enAudio, format="audio/mpeg")
        st.download_button(
            label="Download Audio MP3 in Inglese",
            data=enAudio,
            file_name="Inglese.mp3",
            mime="audio/mpeg",
        )

        deAudio = generate(
            text=de_translated.text, voice="Matilda", model="eleven_multilingual_v1"
        )
        st.write("Deutsch")
        st.audio(deAudio, format="audio/mpeg")
        st.download_button(
            label="Download Audio MP3 in Tedesco",
            data=deAudio,
            file_name="Tedesco.mp3",
            mime="audio/mpeg",
        )
        frAudio = generate(
            text=fr_translated.text, voice="Matilda", model="eleven_multilingual_v1"
        )
        st.write("FranÃ§ais")
        st.audio(frAudio, format="audio/mpeg")
        st.download_button(
            label="Download Audio MP3 in Francese",
            data=frAudio,
            file_name="Francese.mp3",
            mime="audio/mpeg",
        )
        st.success("Audio guide tradotto correttamente")
        st.balloons()
