import speech_recognition as sr
import pyttsx3
import os
import webbrowser
engine = pyttsx3.init()
r = sr.Recognizer()
def new_main():
    engine.say("Hello I'm trying to be your assistant and I'm currently in developing state hope I answer your question")
    engine.runAndWait()
    while True:
        try:

            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source)
                input = r.recognize_google(audio)
                print(input)
                input = input.lower()

                if input == 'internet':
                    engine.say("Opening the net")
                    engine.runAndWait()
                    import web
                elif input == 'files':
                    engine.say("which drive should I look into: ")
                    if input == 'd':
                        engine.say("Name the folder or file which I need to open")
                        os.startfile(fr'D:\{input}')
                        engine.runAndWait()
                    elif input == 'c':
                        engine.say("Name the folder or file which I need to open")
                        os.startfile(fr'C:\{input}')
                        engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand")
new_main()