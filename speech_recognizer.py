import speech_recognition as sr

def Main():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                text = text.lower()
                print(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

Main()
