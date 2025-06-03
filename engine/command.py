import pyttsx3

def speak(text):
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices)
    engine.say(text)
    engine.runAndWait() 
speak("i love p")    