# Whisper Writer
## Real-Time Audio Transcription Application

This application is a real-time audio transcription tool written in Python. It uses the whisper library to transcribe audio in real-time using a pre-trained model. The application starts recording audio when the user presses the F4 key and stops recording when the user releases the F4 key. The recorded audio is then transcribed, and the transcription is printed and typed out.

## Installation

Before running the application, you need to install the required Python dependencies. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

Please note that the `whisper` library is not a standard Python library and may not be available for installation via pip. You may need to install it from a specific source or replace it with an equivalent library.

## Running the Application

To run the application, navigate to the directory containing the `whisper_writer.py` file in your terminal and run the following command:

```bash
python whisper_writer.py
```

Once the application is running, you can start recording audio by pressing the F4 key. Release the F4 key to stop recording and transcribe the recorded audio.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.