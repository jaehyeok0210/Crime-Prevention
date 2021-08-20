# 파이썬으로 문자 보내기

import os
import datetime
from twilio.rest import Client

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
phone = input("문자를 보내실 연락처를 입력해주세요 : ex: (+821012345678)")
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'account_sid'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="귀하의 집에" + nowDatetime + "주거침입이 의심됩니다.",
                     from_='sending_phone_number',
                     to= phone
                 )   

print(message.sid)
