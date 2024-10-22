import os
import speech_recognition as sr

def test():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                if text.lower() == f'open {text} in d drive' or text.lower() == (text):
                    try:
                        file = fr"D:\\{text}"
                        os.startfile(file)
                    except:
                        print("enter a valid dir")

                text = text.lower()
                print(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
test()
