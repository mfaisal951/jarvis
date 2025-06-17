import pyttsx3

def speak(text):
    
    engine = pyttsx3.init('sapi5')
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    # print(voices)
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.9)
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    message="Hello, I am your computer speaking"
    speak("i love pakistan")    








# from gtts import gTTS
# import pygame
# import time
# import os

# def speak(text):
#     print("Converting to speech using gTTS...")

#     # Convert text to speech and save as mp3
#     tts = gTTS(text=text, lang='en')
#     filename = "output.mp3"
#     tts.save(filename)
    

#     print("Playing the speech using pygame...")
#     pygame.mixer.init()
#     pygame.mixer.music.load(filename)
#     pygame.mixer.music.play()

#     # Wait until the audio finishes
#     while pygame.mixer.music.get_busy():
#         time.sleep(0.1)

#     # Clean up
#     pygame.mixer.music.unload()
#     os.remove(filename)

# speak("I love Pakistan")

