"""
ReQurv s.r.l.

This module provides the tools to manage multilanguage audio guide with text-to-speech using streamlit.
 """

import os
import streamlit as st
from elevenlabs import generate, set_api_key
from PIL import Image
from src.services.translation import translateString

# GLOBALS
set_api_key(st.secrets["ELEVENLAB_API_KEY"])
sample_rate = 44100
st.set_page_config(
    layout="wide", page_icon="🌍", page_title="Chat-Bot Audio Guide Beta"
)
prompt_examples = [
    """
La prima sala del museo è dedicata all'arte rinascimentale fiorentina. Qui potrete ammirare alcune delle opere più famose di artisti come Botticelli, Leonardo da Vinci e Michelangelo. Tra le opere più importanti di questa sala ci sono la "Nascita di Venere" di Botticelli e la "Madonna del Garofano" di Leonardo da Vinci.
    """,
    """
La seconda sala del museo ospita una vasta collezione di sculture rinascimentali, tra cui il famoso "David" di Michelangelo. Questa statua, alta più di cinque metri, rappresenta l'eroe biblico David prima della sua battaglia contro Golia.
    """,
    """
La terza sala del museo è dedicata all'arte barocca. Qui potrete ammirare opere di artisti come Caravaggio, Bernini e Rubens. Tra le opere più importanti di questa sala ci sono il "San Giovanni Battista" di Caravaggio e il "Ratto di Proserpina" di Bernini.
    """,
    """
La quarta sala del museo ospita una collezione di dipinti e sculture del XIX e XX secolo. Tra gli artisti rappresentati ci sono Macchiaioli, Impressionisti e Futuristi. Tra le opere più importanti di questa sala ci sono "La signora Matisse" di Henri Matisse e "Il ciclista" di Umberto Boccioni.
    """,
]

# SIDEBAR
with st.sidebar:
    # IMAGE
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = Image.open(os.path.join(script_dir, "src/assets/C_White.png"))
    st.image(image_path)

    st.title("ReQurv è una società di sviluppo di Intelligenza Artificiale.")
    st.caption(
        """
        Ci occupiamo di **innovazione** e creiamo progetti su misura
        per imprese e attività che vogliono utilizzare strumenti di AI 
        per la crescita delle proprie attività;
        """
    )

    st.write(
        "📬 **Contattaci** :",
        "[requrv.io](https://requrv.io)",
    )

    st.write("📧 **Mail** : info@requrv.io")
    st.write("**Claudio Pacini** : claudio.pacini@requrv.io")
    st.write("**Enzo La Rosa** : enzo.larosa@requrv.io")


st.title("Audioguide in multilingua :violet[in pochi secondi] - ReQurv")
st.subheader(
    """
   Genera la tua audio guida personale in 4 lingue in meno di un minuto 🇮🇹 🇬🇧 🇩🇪 🇨🇵
    """
)
st.divider()


# APP
it = st.text_area(
    "Scrivi un testo in italiano",
    value="",
    placeholder="Inserisci il testo per creare la audio guida",
)

translateBtn = st.button(
    "Avvia",
    args=None,
    kwargs=None,
    type="primary",
    disabled=False,
    use_container_width=False,
)

st.subheader("Oppure copiane una già preparata:")

ncol = prompt_examples.__len__()
column = st.columns(ncol)
for col, idx in enumerate(column):
    with idx:
        with st.container(height=200, border=True):
            st.write(prompt_examples[col])

# ACTIONS
if translateBtn:
    if it == "":
        st.warning("Non hai inserito alcun testo")
    else:
        en_translated = translateString(it, fromLang="it", toLang="en")
        st.subheader("English version")
        st.write(str(en_translated))

        de_translated = translateString(it, fromLang="it", toLang="de")
        st.subheader("German version")
        st.write(str(de_translated))

        fr_translated = translateString(it, fromLang="it", toLang="fr")
        st.subheader("French  version")
        st.write(str(fr_translated))

        ch_translated = translateString(it, fromLang="it", toLang="zh-cn")
        st.subheader("Chinese  version")
        st.write(str(ch_translated))

        ru_translated = translateString(it, fromLang="it", toLang="ru")
        st.subheader("Russian  version")
        st.write(str(ru_translated))

        pl_translated = translateString(it, fromLang="it", toLang="pl")
        st.subheader("Polish  version")
        st.write(str(pl_translated))
        try:
            # AUDIO
            itAudio = generate(text=it, voice="Matilda", model="eleven_multilingual_v1")
            st.write("Italiano")
            st.audio(itAudio, format="audio/mpeg")
            st.download_button(
                label="Download Audio MP3 in Italiano",
                data=itAudio,
                file_name="Italiano.mp3",
                mime="audio/mpeg",
            )
            enAudio = generate(
                text=en_translated, voice="Matilda", model="eleven_multilingual_v1"
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
                text=de_translated, voice="Matilda", model="eleven_multilingual_v1"
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
                text=fr_translated, voice="Matilda", model="eleven_multilingual_v1"
            )
            st.write("Francais")
            st.audio(frAudio, format="audio/mpeg")
            st.download_button(
                label="Download Audio MP3 in Francese",
                data=frAudio,
                file_name="Francese.mp3",
                mime="audio/mpeg",
            )

            chAudio = generate(
                text=ch_translated, voice="Matilda", model="eleven_multilingual_v1"
            )
            st.write("Chinese")
            st.audio(chAudio, format="audio/mpeg")
            st.download_button(
                label="Download Audio MP3 in Cinese",
                data=chAudio,
                file_name="Cinese.mp3",
                mime="audio/mpeg",
            )

            ruAudio = generate(
                text=ru_translated, voice="Matilda", model="eleven_multilingual_v1"
            )
            st.write("Russian")
            st.audio(ruAudio, format="audio/mpeg")
            st.download_button(
                label="Download Audio MP3 in Russo",
                data=ruAudio,
                file_name="Russo.mp3",
                mime="audio/mpeg",
            )

            plAudio = generate(
                text=pl_translated, voice="Matilda", model="eleven_multilingual_v1"
            )
            st.write("Polish")
            st.audio(plAudio, format="audio/mpeg")
            st.download_button(
                label="Download Audio MP3 in Polacco",
                data=plAudio,
                file_name="Polacco.mp3",
                mime="audio/mpeg",
            )

            st.success("Audio guide tradotto correttamente")
            st.balloons()
        except Exception as e:
            st.write("C'è stato un problema: ", e)
