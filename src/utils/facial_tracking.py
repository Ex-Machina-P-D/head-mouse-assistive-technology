import cv2
import mediapipe as mp

class FacialTracking:
    """
    Classe utilitária para rastreamento facial usando MediaPipe.
    """

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        self.screen_width, self.screen_height = cv2.getWindowImageRect('')[2:4]

    def track(self):
        """
        Rastreia os movimentos faciais e calcula a posição do nariz.
        """
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
