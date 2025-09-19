import pyautogui as pag
from abc import ABC, abstractmethod

class Ctrl(ABC):
    """
    Controller Base Class (Abstract)
    """

    def __init__(self):
        self.running = False
        self.pag = pag

    def start(self):
        self.running = True
        while self.running:
            self.exec()

    def stop(self):
        self.running = False
        
    @abstractmethod
    def exec(self):
        pass