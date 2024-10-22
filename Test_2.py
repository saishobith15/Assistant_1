import speech_recognition as sr
import pyttsx3

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def listen():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    try:
      text = recognizer.recognize_google(audio)
      print(text)
      return text
    except:
      print("Could not understand audio")
      return None

while True:
  command = listen()
  if command:
    if "hello" in command:
      speak("Hello there!")
    elif "how are you" in command:
      speak("I'm doing well, thanks for asking!")
    else:
      speak("I didn't understand that.")

speak()
listen()