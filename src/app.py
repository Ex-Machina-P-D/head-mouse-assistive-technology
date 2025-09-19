from controllers.movement_control import MovementControl
from controllers.voice_control import VoiceControl
import threading

def main():
    """ 
    Initialize the threads & define the working flux of the app. 
    """
    
    movement_control = MovementControl()
    voice_control = VoiceControl()

    voice_thread = threading.Thread(target=voice_control.start)
    head_thread = threading.Thread(target=movement_control.start)

    voice_thread.start()
    head_thread.start()

    try:
        voice_thread.join()
        head_thread.join()
        
    except KeyboardInterrupt:
        print("Encerrando...")
        voice_control.stop()
        movement_control.stop()

if __name__ == "__main__":
    main()
