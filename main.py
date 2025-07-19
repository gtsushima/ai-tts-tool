# main.py
# This code is a Streamlit application that uses the Kokoro-TTS model to generate speech
# from user-provided text. It allows users to select from various voices and provides an audio
# playback feature with advanced controls.
import streamlit as st
from kokoro import KPipeline
import soundfile as sf
import io
import numpy as np
from streamlit_advanced_audio import audix , WaveSurferOptions
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

# Voice selection dropdown
selected_voice_name = st.selectbox("Choose a voice:", list(available_voices.keys()))
voice_id = available_voices[selected_voice_name]

# Text input from the user
text_input = st.text_input("Enter the text you want to convert to speech:", 
                           placeholder="Type your text here...", icon=  "📝")

# A button to trigger the speech generation
if st.button("Generate Speech"):
    if text_input:
        try:
            # Initialize the Kokoro-TTS pipeline
            # Using 'a' for American English as a base, the voice parameter will override this
            with st.spinner("Initializing the model and generating audio..."):
                pipeline = KPipeline(lang_code='a')

                # Generate speech from the input text with the selected voice
                generator = pipeline(text_input, voice=voice_id)

                # The generator yields audio chunks; we'll concatenate them
                audio_chunks = []
                for i, (gs, ps, audio) in enumerate(generator):
                    audio_chunks.append(audio)

                if audio_chunks:
                    # Concatenate the audio chunks into a single numpy array
                    full_audio = np.concatenate(audio_chunks)

                    # Create an in-memory buffer for the audio
                    buffer = io.BytesIO()
                    sf.write(buffer, full_audio, 24000, format='WAV')
                    buffer.seek(0)

                    # Advanced audio playback with custom styling
                    st.subheader("Generated Audio Playback")
                    audix(buffer, format="audio/wav", autoplay=True)
                    wavesurfer_options = WaveSurferOptions(
                        wave_color="#2B88D9",
                        progress_color="#b91d47",
                        height=100
                    )

                    # # Play the generated audio and track playback status
                    # result = audix(buffer, wavesurfer_options=wavesurfer_options)
                    # if result:
                    #     st.write(f"Current Time: {result['currentTime']}s")
                    #     if result['selectedRegion']:
                    #         st.write(f"Selected Region: {result['selectedRegion']['start']} - {result['selectedRegion']['end']}s")

                    # Provide a download link for the generated audio
                    st.download_button(
                        label="Download Audio",
                        data=buffer,
                        file_name="generated_speech.wav",
                        mime="audio/wav"
                    )
                    st.success("Audio generated successfully!")
                else:
                    st.warning("The model did not produce any audio output.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to generate speech.")

# Add a footer with model information
st.markdown("---")
st.markdown("Powered by [hexgrad/Kokoro-TTS](https://huggingface.co/hexgrad/Kokoro-TTS)")