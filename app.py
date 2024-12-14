import streamlit as st
import requests
import tempfile


# Streamlit App
st.title("Text to Music Generator")
st.write("Generate music based on a text description using Hugging Face's MusicGen model!")

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"

# Function to query the Hugging Face API
def query_huggingface_api(payload, api_token):
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

# User Input
api_token = st.text_input("Enter your Hugging Face API token (Read):", type="password")
user_input = st.text_input("Enter a description for the music you want to generate:", placeholder="e.g., 80s pop track with bassy drums and synth")

if st.button("Generate Music"):
    if not api_token.strip():
        st.warning("Please enter your API token before generating music.")
    elif not user_input.strip():
        st.warning("Please enter a description before generating music.")
    else:
        with st.spinner("Generating music..."):
            try:
                # Query the Hugging Face API
                payload = {"inputs": user_input}
                audio_data = query_huggingface_api(payload, api_token)

                # Save audio to a temporary file
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_wav:
                    tmp_wav.write(audio_data)
                    tmp_wav_path = tmp_wav.name

                # Display audio player and download link
                st.audio(tmp_wav_path, format="audio/wav")
                st.download_button(
                    label="Download Music",
                    data=open(tmp_wav_path, "rb").read(),
                    file_name="generated_music.wav",
                    mime="audio/wav",
                )

            except Exception as e:
                st.error(f"An error occurred while generating the music: {e}")
