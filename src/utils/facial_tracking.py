import cv2
import pyautogui as pag
import mediapipe as mp

class FacialTracking:
    """
    Facial Tracking Utility
    
    Capture movement & estimate nose position.
    """

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        self.screen_width, self.screen_height = pag.size()

    def track(self):
        """
        Tracks facial movement & calculates nose position.
        """
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = self.face_mesh.process(rgb_frame)

                if result.multi_face_landmarks:
                    for landmarks in result.multi_face_landmarks:
                        nose = landmarks.landmark[1]
                        screen_x = self.screen_width * nose.x
                        screen_y = self.screen_height * nose.y
                        yield (screen_x, screen_y), frame
                        break
                else:
                    yield None, frame
        finally:
            self.stop()

    def display_frame(self, frame):
        """
        Exibe o vídeo com a visualização do rastreamento.
        """
        cv2.imshow('Facial Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop()

    def stop(self):
        """
        Libera recursos e encerra o rastreamento.
        """
        self.cap.release()
        cv2.destroyAllWindows()
