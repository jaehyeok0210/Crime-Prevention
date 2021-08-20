#gmail 보내기 예제

import smtplib
import datetime
from email.mime.text import MIMEText

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
Toaccount = input("보낼 이메일의 주소를 입력해주세요: ")
pw = input("발송 이메일 계정의 앱 비밀번호를 입력해주세요 : ")
Getaccount = input("받을 이메일의 주소를 입력해주세요 : ")
#세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

#TLS 보안 시작
s.starttls()
s.login(str(Toaccount), str(pw))

#보낼 메세지 작성
msg = MIMEText('귀하의 집에' + nowDatetime + ' 주거침입이 의심됩니다')
msg['Subject'] = '제목 : 가구 방범 상황 알림입니다.'

#메일 보내기
s.sendmail(str(Toaccount), str(Getaccount), msg.as_string())
s.quit()
