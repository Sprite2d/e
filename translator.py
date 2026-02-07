import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import pyaudio
import sys

def list_audio_devices():
    """Prints all available audio input devices."""
    p = pyaudio.PyAudio()
    print("\n--- Available Audio Input Devices ---")
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:
            print(f"Index {i}: {dev['name']}")
    p.terminate()

