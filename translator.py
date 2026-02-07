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

def run_translator(device_index, target_lang='es'):
    """Main translation loop."""
    recognizer = sr.Recognizer()
    translator = Translator()
    engine = pyttsx3.init()
    

    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)    
    engine.setProperty('volume', 0.9)  

    print(f"\n--- AI Translator Active (Using Device {device_index}) ---")
    print("Press Ctrl+C to stop.")

    with sr.Microphone(device_index=device_index) as source:
        
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        while True:
            try:
                print("\nListening...")
                
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=7)
                
                print("Transcribing...")
                text = recognizer.recognize_google(audio)
                print(f"-> You: {text}")

                
                result = translator.translate(text, dest=target_lang)
                print(f"-> AI ({target_lang}): {result.text}")

                
                engine.say(result.text)
                engine.runAndWait()

            except sr.UnknownValueError:
                print("... (Silence or unclear audio) ...")
            except sr.RequestError:
                print("Error: Check your internet connection.")
            except KeyboardInterrupt:
                print("\nAssistant shutting down. Goodbye!")
                break

if _name_ == "_main_":
    
    list_audio_devices()
    
    
    try:
        idx = int(input("\nEnter the Index number of your earphones: "))
        lang = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French, 'hi' for Hindi): ").lower()
        run_translator(device_index=idx, target_lang=lang)
    except ValueError:
        print("Please enter a valid number for the device index.")
        
