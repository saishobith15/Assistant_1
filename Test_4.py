import speech_recognition as sr
import pyttsx3
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            return text
        except:
            print("Could Not understand, Please repeat")
            return None
while True:
    command = listen()
    if command == 'hello' or command == 'hey' or command == 'hi' or command == 'namaste':
        speak("hello there! I'm friday, I will be looking after your problems today, How can I help you?")
    elif command == 'how are you' or command == 'how are your doing' or command == 'are you alright':
        speak("I'm doing Great, how are you")
    elif command == 'exit':
        speak("Good bye, pleasure to help you today")
        break
    elif command == 'open internet':
        speak("opening internet")
        webbrowser.open_new_tab("https://www.google.com")
    elif command == 'open youtube':
        speak("open youtube")
        url = 'youtube'
        webbrowser.open_new_tab(f"https://www.{url}.com")
