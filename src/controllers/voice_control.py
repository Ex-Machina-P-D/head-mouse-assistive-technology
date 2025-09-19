from controllers.ctrl import Ctrl
from utils.speech_recognition_util import SpeechRecognition

class VoiceControl(Ctrl):
    """
    Controller by voice
    """

    def __init__(self):
        self.speech_recognition = SpeechRecognition()

    def execute_command(self, command: str):
        """
        Maps voice commands to mouse actions, & executes them.
        """
        commands = {
            "clique": lambda: self.pag.click(),
            "clique duplo": lambda: self.pag.doubleClick(),
            "clique direito": lambda: self.pag.click(button='right'),
            "sobe": lambda: self.pag.scroll(300),
            "desce": lambda: self.pag.scroll(-300),
        }

        for key, action in commands.items():
            if key in command:
                action()
                return
            else:
                print(f"[VoiceControl] Comando desconhecido: {command}")

    def exec(self):
        command = self.speech_recognition.get_command()
        if command:
            print(f"Comando reconhecido: {command}")
            self.execute_command(command)
        else:
            print("Comando não reconhecido.")

    def start(self):
        super().start()
        print("Controle de voz iniciado.")
                
    def stop(self):
        super().stop()
        print("Controle de voz parado.")
