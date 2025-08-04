# 🔊 Enhanced AI Text-to-Speech with Kokoro-TTS

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.streamlit.app)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A user-friendly Streamlit application for converting text into high-quality speech using the `hexgrad/Kokoro-TTS` model. Select from a variety of voices to customize the audio output.

---

## ✨ Features

- **Text-to-Speech Conversion**: 🗣️ Converts user-provided text into speech.
- **Multiple Voices**: 🎤 Offers a selection of American and British male and female voices.
- **Audio Playback**: 🎶 Includes an audio player with advanced controls to listen to the generated speech.
- **Download Audio**: 💾 Allows users to download the generated audio in WAV format.
- **Responsive Interface**: 📱 Built with Streamlit for a seamless user experience on different devices.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.12+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (optional, but recommended for faster dependency management)

### 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/my-project.git
    cd my-project
    ```

2.  **Using `uv` (Recommended):**
    -   Install `uv`:
        ```bash
        pip install uv
        ```
    -   Create and activate a virtual environment:
        ```bash
        uv venv
        source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
        ```
    -   Install the dependencies:
        ```bash
        uv pip install -r requirements.txt
        ```

3.  **Using `pip`:**
    -   Create and activate a virtual environment:
        ```bash
        python -m venv .venv
        source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
        ```
    -   Install the dependencies:
        ```bash
        pip install -r requirements.txt
        ```

---

## ▶️ Usage

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run main.py
```

This will open the application in your default web browser.

---

## 📚 Dependencies

The application relies on the following Python libraries:

-   `streamlit`: For creating the web application interface.
-   `kokoro-tts`: The core text-to-speech model.
-   `soundfile`: For handling audio files.
-   `streamlit-advanced-audio`: For the advanced audio player.
-   `torch`: A required dependency for the TTS model.
-   `spacy`: For natural language processing.

For a complete list of dependencies, please see the `requirements.txt` file.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 🙏 Acknowledgments

-   This application is powered by the [hexgrad/Kokoro-TTS](https://huggingface.co/hexgrad/Kokoro-TTS) model.
-   The user interface is built with [Streamlit](https://streamlit.io).
-   The advanced audio player is provided by the [streamlit-advanced-audio](https://pypi.org/project/streamlit-advanced-audio/) library.