# main.py
# This code is a Streamlit application that uses the Kokoro-TTS model to generate speech
# from user-provided text. It allows users to select from various voices and provides an audio
# playback feature with advanced controls.
import streamlit as st
from kokoro import KPipeline
import soundfile as sf
import io
import numpy as np
from streamlit_advanced_audio import audix, WaveSurferOptions
# Set up the title of the Streamlit app
st.title("🔊 Enhanced AI Text-to-Speech with Kokoro-TTS")

# Add a description of the app
st.markdown("""
This application utilizes the `hexgrad/Kokoro-TTS` model to convert your text into high-quality speech. 
You can now select from a variety of voices to customize the audio output.
Enter your text in the box below, choose a voice, and click the 'Generate Speech' button.
""")


# A list of available voices
# Sourced from the official documentation and community findings
available_voices = {
    "American Female (Sarah)": "af_sarah",
    "American Female (Bella)": "af_bella",
    "American Female (Nicole)": "af_nicole",
    "American Female (Sky)": "af_sky",
    "American Male (Adam)": "am_adam",
    "American Male (Michael)": "am_michael",
    "British Female (Emma)": "bf_emma",
    "British Female (Isabella)": "bf_isabella",
    "British Male (George)": "bm_george",
    "British Male (Lewis)": "bm_lewis",
}

# --- Caching and Callback Setup ---
@st.cache_resource
def get_pipeline():
    return KPipeline(lang_code='a')

@st.cache_data
def generate_speech(text, voice_id):
    pipeline = get_pipeline()
    generator = pipeline(text, voice=voice_id)
    audio_chunks = [audio for _, _, audio in generator]
    if audio_chunks:
        full_audio = np.concatenate(audio_chunks)
        buffer = io.BytesIO()
        sf.write(buffer, full_audio, 24000, format='WAV')
        buffer.seek(0)
        return buffer
    return None

def generate_speech_callback():
    text = st.session_state.get("text_input", "")
    voice_name = st.session_state.get("voice_name", list(available_voices.keys())[0])
    voice_id = available_voices[voice_name]
    if text:
        buffer = generate_speech(text, voice_id)
        st.session_state["audio_buffer"] = buffer
        st.session_state["voice_id"] = voice_id
    else:
        st.session_state["audio_buffer"] = None

# --- Widgets with session state and callbacks ---
st.selectbox(
    "Choose a voice:",
    list(available_voices.keys()),
    key="voice_name",
    on_change=generate_speech_callback
)

st.text_input(
    "Enter the text you want to convert to speech:",
    key="text_input",
    placeholder="Type your text here...",
    on_change=generate_speech_callback
)

if st.button("Generate Speech"):
    generate_speech_callback()

# --- Playback and download if audio exists ---
if st.session_state.get("audio_buffer"):
    st.subheader("Generated Audio Playback")
    audix(st.session_state["audio_buffer"], format="audio/wav", autoplay=True)
    wavesurfer_options = WaveSurferOptions(
        wave_color="#2B88D9",
        progress_color="#b91d47",
        height=100
    )
    st.download_button(
        label="Download Audio",
        data=st.session_state["audio_buffer"],
        file_name="generated_speech.wav",
        mime="audio/wav"
    )
    st.success("Audio generated successfully!")
elif "audio_buffer" in st.session_state and st.session_state["audio_buffer"] is None:
    st.warning("The model did not produce any audio output.")

# Add a footer with model information
st.markdown("---")
st.markdown("Powered by [hexgrad/Kokoro-TTS](https://huggingface.co/hexgrad/Kokoro-TTS)")