# # import playsound as playsound
# from playsound import playsound
# import eel

# # playing Assistant sound
# def playAssistantSound():
#     music_dir="www\\assets\\audio\\start_sound.mp3"
#     playsound(music_dir)



import os
import pygame
import eel


@eel.expose
def playAssistantSound():
    # Get the absolute path to the audio file
    base_dir = os.path.dirname(os.path.abspath(__file__))  # This is /jarvis/engine/
    music_path = os.path.abspath(os.path.join(base_dir, '..', 'www', 'assets', 'audio', 'start_sound.mp3'))

    # Optional: print the resolved path to debug
    print("Resolved audio path:", music_path)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

