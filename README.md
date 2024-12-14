
# Text to Music Generator

This Streamlit application allows users to generate music from text descriptions using Hugging Face's MusicGen model (`facebook/musicgen-small`). Users can input a description of the music they want to generate, and the app will produce an audio file that can be played directly or downloaded.

## Features
- Input a text description of the music.
- Generate music using the Hugging Face API.
- Listen to the generated music within the app.
- Download the generated music as a `.wav` file.

## Requirements

### Python Libraries
Ensure you have the following Python libraries installed:
- `streamlit`
- `requests`
- `scipy`

Install the libraries using pip:
```bash
pip install streamlit requests scipy
```

## How to Use

### 1. Run the Application
Run the Streamlit app using the following command:
```bash
streamlit run app.py
```

### 2. Provide Hugging Face API Token
- Enter your Hugging Face API token in the input box. You can obtain a token by logging into your Hugging Face account and navigating to the [Access Tokens](https://huggingface.co/settings/tokens) page.

### 3. Describe the Music
- Enter a description of the music you want to generate (e.g., "80s pop track with bassy drums and synth").

### 4. Generate and Download
- Click the **Generate Music** button.
- Listen to the generated audio using the built-in audio player.
- Optionally, download the generated `.wav` file.

## Code Overview

### Key Components
- **API Integration**:
  The app uses the Hugging Face Inference API to interact with the MusicGen model.
- **User Input**:
  Users provide a text description and their API token.
- **Audio Generation**:
  The app queries the API and processes the generated audio.
- **File Handling**:
  Temporary `.wav` files are created to store the audio, which are then provided for playback and download.

### Main Files
- `app.py`: Contains the Streamlit application code.

## Example
1. Input: `"90s rock song with loud guitars and heavy drums"`
2. Output: A `.wav` file containing the generated music.

## Screenshots

- **Music Description Input**
  ![Input Box Screenshot](#)
- **Audio Player and Download Button**
  ![Audio Player Screenshot](#)

## Troubleshooting

- **Invalid API Token**:
  Ensure you have entered a valid Hugging Face API token.
- **No Music Generated**:
  Check your text description for clarity and try again.
- **Connection Issues**:
  Verify your internet connection and API endpoint status.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Built with [Streamlit](https://streamlit.io/).
- Powered by [Hugging Face MusicGen Model](https://huggingface.co/facebook/musicgen-small).

