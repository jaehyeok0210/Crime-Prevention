
import speech_recognition as sr
import csv

r = sr.Recognizer()
sit = 0
while sit !=1 :
    with sr.Microphone() as source:
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language = 'ko-KR')
            print("You said : {}".format(text))
            f = open('crime_data.csv', 'r', encoding = 'cp949')
            rd = csv.reader(f)
            for i in rd:
                if text in i: 
                    print("위급상황")
                    sit = 1
        except:
            print("Sorry could not recognize what you said")
