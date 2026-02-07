import tkinter as tk
from tkinter import ttk, messagebox
import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import pyaudio
import threading

class VoiceTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Voice Assistant Translator")
        self.root.geometry("500x450")
        
        
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.engine = pyttsx3.init()
        self.is_listening = False

        self.create_widgets()
        self.load_devices()

    def create_widgets(self):
        """Creates the visual buttons and labels."""
        tk.Label(self.root, text="AI Voice Translator", font=("Arial", 18, "bold")).pack(pady=10)

        
        tk.Label(self.root, text="Select Earphones/Mic:").pack()
        self.device_combo = ttk.Combobox(self.root, width=50, state="readonly")
        self.device_combo.pack(pady=5)

        
      
