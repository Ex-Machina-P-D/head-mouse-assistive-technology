import cv2
import mediapipe as mp
import pyautogui
import speech_recognition as sr
import threading

def voice_control():
    """
    Função que escuta comandos de voz e executa ações do mouse.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
    
    while True:
        with microphone as source:
            print("Aguardando comando de voz...")
            audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio, language='pt-BR').lower()
            print(f"Comando reconhecido: {command}")
            
            if "clique" in command:
                pyautogui.click()
            elif "duplo clique" in command:
                pyautogui.doubleClick()
            elif "clique direito" in command:
                pyautogui.click(button='right')
            elif "scroll para cima" in command:
                pyautogui.scroll(300)
            elif "scroll para baixo" in command:
                pyautogui.scroll(-300)
        
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o comando de voz.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de voz; {e}")

def head_control():
    """
    Função que rastreia o movimento da cabeça e move o cursor do mouse.
    """
    mp_face_mesh = mp.solutions.face_mesh
    cap = cv2.VideoCapture(0)

    screen_width, screen_height = pyautogui.size()
    face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Espelha a imagem para melhor usabilidade
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        
        # Converte a imagem para RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb_frame)
        
        # Verifica se há landmarks detectados
        if result.multi_face_landmarks:
            for facial_landmarks in result.multi_face_landmarks:
                # Usa o ponto do nariz como referência
                nose_point = facial_landmarks.landmark[1]
                x = int(nose_point.x * frame_width)
                y = int(nose_point.y * frame_height)
                
                # Converte a posição do nariz para a posição da tela
                screen_x = screen_width * nose_point.x
                screen_y = screen_height * nose_point.y
                
                # Move o cursor do mouse
                pyautogui.moveTo(screen_x, screen_y)
                
                # Desenha um círculo no nariz para visualização
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        # Exibe o quadro de vídeo
        cv2.imshow('Controle por Movimento da Cabeça', frame)
        
        # Encerra o loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

def main():
    """
    Função principal que inicia as threads de controle de voz e movimento da cabeça.
    """
    # Cria threads separadas para controle de voz e movimento da cabeça
    voice_thread = threading.Thread(target=voice_control)
    head_thread = threading.Thread(target=head_control)
    
    # Inicia as threads
    voice_thread.start()
    head_thread.start()
    
    # Aguarda as threads terminarem
    voice_thread.join()
    head_thread.join()

if __name__ == "__main__":
    main()
