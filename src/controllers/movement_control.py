from controllers.ctrl import Ctrl
from utils.facial_tracking import FacialTracking

class MovementControl(Ctrl):
    """
    Controller by head movement
    """

    def __init__(self):
        self.facial_tracking = FacialTracking()

    def exec(self):
        for position, frame in self.facial_tracking.track():
            if position:
                screen_x, screen_y = position
                self.pag.moveTo(screen_x, screen_y)
            if frame is not None:
                self.facial_tracking.display_frame(frame)
                
        """
            head_position = self.tracking.get_head_position()
            if head_position:
                dx, dy = head_position
                pyautogui.moveRel(dx, dy)
        """
        
    def start(self):
        super().start()
        print("Controle de movimento iniciado.")
            
    def stop(self):
        super().stop()
        self.facial_tracking.stop()
        print("Controle de movimento parado.")
