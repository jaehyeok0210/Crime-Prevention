
import speech_recognition as sr
import csv

r = sr.Recognizer()
sit = 1
con = "정상"
while sit ==1 :
    with sr.Microphone() as source:
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language = 'ko-KR')
            splits = text.split()
            print("You said : {}".format(splits))
            f = open('crime_data.csv', 'r', encoding = 'cp949')
            rd = csv.reader(f)
            for i in rd:
                for j in range(len(i)):
                    for k in range(len(splits)):
                        if splits[k] in i[j] and len(splits[k])>=2:
                            con = "위급상황"
                            sit = 0
            if con == "위급상황":
                print("위급상황")
        except:
            print("Sorry could not recognize what you said")
