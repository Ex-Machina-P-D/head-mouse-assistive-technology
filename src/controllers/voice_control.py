from utils.speech_recognition_util import SpeechRecognitionUtil
import pyautogui

class VoiceControl:
    """
    Classe responsável por controlar o mouse com comandos de voz.
    """

    def __init__(self):
        self.speech_recognition = SpeechRecognitionUtil()

    def execute_command(self, command: str):
        """
        Mapeia comandos de voz para ações do mouse.
        """
        commands = {
            "clique": lambda: pyautogui.click(),
            "duplo clique": lambda: pyautogui.doubleClick(),
            "clique direito": lambda: pyautogui.click(button='right'),
            "scroll para cima": lambda: pyautogui.scroll(300),
            "scroll para baixo": lambda: pyautogui.scroll(-300),
        }

        for key, action in commands.items():
            if key in command:
                action()
                return

    def start(self):
        """
        Inicia o controle de voz.
        """
        while True:
            command = self.speech_recognition.get_command()
            if command:
                print(f"Comando reconhecido: {command}")
                self.execute_command(command)
            else:
                print("Comando não reconhecido.")
