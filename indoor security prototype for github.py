## Automatic Indoor Security System
## Date: 2021.08.20.
## Author: Jaehyeok Jang

#Assume that System is ON
#Assume that Setting is "indoor", there is only user in the room

#Import
import os
import datetime
from twilio.rest import Client
import speech_recognition as sr
import csv
import smtplib
from email.mime.text import MIMEText

#Input Stage
#E-mail info input
Toaccount = input("보낼 G-mail의 주소를 입력해주세요: ")
pw = input("발송 이메일 계정의 앱 비밀번호를 입력해주세요 : ")
Getaccount = input("받을 이메일의 주소를 입력해주세요 : ")
#SMS info input
phone = input("문자를 보내실 연락처를 입력해주세요 : ex: (+821012345678)")
#Sending agent info 
account_sid = 'account_sid'
auth_token = 'auth_token'
#Home address info input
Home = input("현재 거주중인 주소를 입력해주세요 : ")

#Normal State / Create Objects / Set Default environment
r = sr.Recognizer()
sit = 0
con = "정상"
#Assume that Two People are Detected By RF Signal 

#Notification to User
#Save the current time and send it to user 
now1 = datetime.datetime.now()
nowDatetime1 = now1.strftime('%Y-%m-%d %H:%M:%S')
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(str(Toaccount), str(pw))
msg = MIMEText('귀하의 집에' + nowDatetime1 + ' 주거침입이 의심됩니다')
msg['Subject'] = '제목 : 가구 방범 상황 알림입니다.'
s.sendmail(str(Toaccount), str(Getaccount), msg.as_string())
s.quit()

#Criminal Word Detection
sit = 1
#Determine Situation 
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
                        if splits[k] in i[j] and len(splits[k])>=3:
                            con = "위급상황"
                            sit=0
            #Action in Crime Situation
            if con == "위급상황":                
                print("위급상황")
                #Time Update
                now2 = datetime.datetime.now()
                nowDatetime2 = now2.strftime('%Y-%m-%d %H:%M:%S')
                #Report to police , but user phone in this prototype
                client = Client(account_sid, auth_token)
                message = client.messages.create(body= Home + nowDatetime2 + " 범죄 상황이 발생했습니다. 신고 접수합니다.",from_='+17146811745',to= phone)
                print(message.sid)
        except:
            print("Sorry could not recognize what you said")

