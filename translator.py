import customtkinter as ctk
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import threading
import os

# Initialize components
translator = Translator()
recognizer = sr.Recognizer()

class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Voice Translator")
        self.geometry("500x550")
        ctk.set_appearance_mode("dark")

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Voice Translator", font=("Arial", 28, "bold"))
        self.label.pack(pady=20)

        # Language Selection
        self.lang_frame = ctk.CTkFrame(self)
        self.lang_frame.pack(pady=10)

        self.lang_label = ctk.CTkLabel(self.lang_frame, text="Target Language:")
        self.lang_label.grid(row=0, column=0, padx=10)

        self.lang_menu = ctk.CTkOptionMenu(self.lang_frame, values=["Spanish", "French", "German", "Japanese", "Hindi"])
        self.lang_menu.grid(row=0, column=1, padx=10)
        self.lang_menu.set("Spanish")

        # Text Displays
        self.input_text = ctk.CTkTextbox(self, width=400, height=100)
        self.input_text.pack(pady=10)
        self.input_text.insert("0.0", "Your speech will appear here...")

     
