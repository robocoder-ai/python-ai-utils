# Description: This script uses the whisper library to transcribe audio in real-time using a pre-trained model.

import keyboard
import numpy as np
import whisper
import torch
import time
import speech_recognition as sr
from queue import Queue
from pynput.keyboard import Controller

SAMPLE_RATE = 16000
PHRASE_TIME_LIMIT = 1
MODEL_NAME = "base"
k = Controller()

def type_text(text):
    """
    Function to type the transcribed text using pynput.
    """
    for char in text:
        k.type(char)
        time.sleep(0.02)  # Add a small delay between each character

# Constants

# Global variables
data_queue = Queue()
recorder = sr.Recognizer()
source = sr.Microphone(sample_rate=SAMPLE_RATE)
audio_model = whisper.load_model(MODEL_NAME)
transcription = ['']
is_recording = False


def record_audio(_, audio: sr.AudioData) -> None:
    """
    Callback function to record audio data when recordings finish.
    """
    if is_recording:
        data = audio.get_raw_data()
        data_queue.put(data)

def start_recording(e):
    """
    Function to start recording audio.
    """
    global is_recording
    global transcription
    if not is_recording:
        is_recording = True
        transcription = ['']
        print("Recording audio...")

def stop_recording(e):
    """
    Function to stop recording audio and transcribe the recorded audio.
    """
    global is_recording
    if is_recording:
        time.sleep(1)  # Wait for 1 second to ensure all audio data has been processed
        is_recording = False
        print("Stopped recording audio...")
        transcribe_audio()


def transcribe_audio():
    """
    Function to transcribe the recorded audio.
    """
    audio_data = b''.join(data_queue.queue)
    data_queue.queue.clear()
    audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
    result = audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
    text = result['text'].strip()
    transcription.append(text)
    print_transcription()
    type_text(text)


def print_transcription():
    """
    Function to print the transcription.
    """
    print("\n\nTranscription:")
    for line in transcription:
        print(line)


def main():
    """
    Main function to start and stop recording on key press and release.
    """
    recorder.listen_in_background(source, record_audio, phrase_time_limit=PHRASE_TIME_LIMIT)
    keyboard.on_press_key("f4", start_recording)
    keyboard.on_release_key("f4", stop_recording)
    keyboard.wait()


if __name__ == "__main__":
    main()

