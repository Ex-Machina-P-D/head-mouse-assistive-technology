import speech_recognition as sr

class SpeechRecognition:
    """
    Speech Recognition Utility.
    
    Capture voice & return as string.
    """

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def adjust_noise(self):
        """
        Ajusta o reconhecimento de ruído ambiente.
        """
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def get_command(self) -> str:
        """
        Escuta e reconhece comandos de voz.
        """
        with self.microphone as source:
            self.adjust_noise()
            print("Aguardando comando de voz...")
            try:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio, language='pt-BR')
                return command.lower()
            except sr.UnknownValueError:
                return None
            except sr.RequestError as e:
                print(f"Erro no serviço de reconhecimento de voz: {e}")
                return None
