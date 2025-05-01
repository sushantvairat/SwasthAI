import speech_recognition as sr
import pyttsx3
from ..utils.logger import get_logger

class MultilingualSupport:
    def __init__(self):
        self.logger = get_logger("MultilingualSupport")
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.languages = {"en": "English", "hi": "Hindi"}
        self.current_language = "en"
        self.logger.info("MultilingualSupport initialized")

    def set_language(self, lang_code):
        if lang_code in self.languages:
            self.current_language = lang_code
            self.engine.setProperty("voice", self.current_language)
            self.logger.info(f"Language set to {self.languages[lang_code]}")

    def voice_to_text(self):
        try:
            with sr.Microphone() as source:
                self.logger.debug("Listening for voice input")
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio, language=self.current_language)
                self.logger.debug(f"Voice input transcribed: {text}")
                return text
        except Exception as e:
            self.logger.error(f"Voice recognition error: {str(e)}")
            return f"Error in voice recognition: {str(e)}"

    def text_to_voice(self, text):
        self.logger.debug(f"Converting text to voice: {text}")
        self.engine.say(text)
        self.engine.runAndWait()