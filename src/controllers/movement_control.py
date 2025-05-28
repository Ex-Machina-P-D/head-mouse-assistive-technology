from utils.facial_tracking import FacialTracking
import pyautogui

class MovementControl:
    """
    Classe responsável por controlar o cursor do mouse com movimentos da cabeça.
    """

    def __init__(self):
        self.facial_tracking = FacialTracking()

    def start(self):
        """
        Inicia o controle de movimento por rastreamento facial.
        """
        for position, frame in self.facial_tracking.track():
            if position:
                screen_x, screen_y = position
                pyautogui.moveTo(screen_x, screen_y)
            self.facial_tracking.display_frame(frame)
