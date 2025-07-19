import pyttsx3
import speech_recognition as sr
import pyaudio

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source, 10, 6)
    try:
        print(" Recognization")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    except Exception as e:
        return ""
    return query.lower()

text=takecommand()
            
        
    
speak(text)

if __name__ == "__main__":
    takecommand()   








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



