import requests
from bs4 import BeautifulSoup
import telegram
import schedule
import time
import ssl
import urllib.request
import json
import urllib3
import asyncio

# Telegram
async def bot_send(msg):
    telegram_token = "5128692345:AAHkO-3JZ9tZYP2hrS5UAlnYCrO0PiO09_A"
    telegram_id = "444879086"
    bot = telegram.Bot(token = telegram_token)
    await bot.sendMessage(chat_id=telegram_id, text=msg)

# sst
# telegram_token_sst = "5684538461:AAEPO_Uyv9NPxLEAHWwvBkZ9t1oa03NYcWY"
# telegram_id_sst = "5731627764"
# bot_sst = telegram.Bot(token = telegram_token_sst)

url = 'https://yeyak.seoul.go.kr/web/reservation/selectListReservCalAjax.do'

palyload = {
    'file_id': '',
    'sysToday': '20230303',
    'rsv_svc_id': 'S230211150852224390',
    'grp_code': '',
    'resve_unit_seq': '',
    'resve_unit_seq2': '',
    'use_time_unit_code': 'B409',
    'tme_ty_code': 'TM02',
    'wait_posbl_co': '',
    'use_stdr_rcept_daycnt': '60',
    'use_stdr_rcept_time': '14',
    'rsvde_stdr_rcept_daycnt':'0',
    'rsvde_stdr_rcept_time': '17',
    'sltYear': '2023',
    'sltMonth': '03',
    'sltDay': '03',
    'yyyymm': '202303',
    'yyyy': '2023',
    'mm': '03',
    'dd': '03',
}

palyload2 = {
    'file_id': '',
    'sysToday': '20230303',
    'rsv_svc_id': 'S230211145025248959',
    'grp_code': '',
    'resve_unit_seq': '',
    'resve_unit_seq2': '',
    'use_time_unit_code': 'B409',
    'tme_ty_code': 'TM02',
    'wait_posbl_co': '',
    'use_stdr_rcept_daycnt': '60',
    'use_stdr_rcept_time': '14',
    'rsvde_stdr_rcept_daycnt':'0',
    'rsvde_stdr_rcept_time': '17',
    'sltYear': '2023',
    'sltMonth': '03',
    'sltDay': '03',
    'yyyymm': '202303',
    'yyyy': '2023',
    'mm': '03',
    'dd': '03',
}

palyload3 = {
    'file_id': '',
    'sysToday': '20230303',
    'rsv_svc_id': 'S230211150020900809',
    'grp_code': '',
    'resve_unit_seq': '',
    'resve_unit_seq2': '',
    'use_time_unit_code': 'B409',
    'tme_ty_code': 'TM02',
    'wait_posbl_co': '',
    'use_stdr_rcept_daycnt': '60',
    'use_stdr_rcept_time': '14',
    'rsvde_stdr_rcept_daycnt':'0',
    'rsvde_stdr_rcept_time': '17',
    'sltYear': '2023',
    'sltMonth': '03',
    'sltDay': '03',
    'yyyymm': '202303',
    'yyyy': '2023',
    'mm': '03',
    'dd': '03',
}

palyload4 = {
    'file_id': '',
    'sysToday': '20230303',
    'rsv_svc_id': 'S230211151235143865',
    'grp_code': '',
    'resve_unit_seq': '',
    'resve_unit_seq2': '',
    'use_time_unit_code': 'B409',
    'tme_ty_code': 'TM02',
    'wait_posbl_co': '',
    'use_stdr_rcept_daycnt': '60',
    'use_stdr_rcept_time': '14',
    'rsvde_stdr_rcept_daycnt':'0',
    'rsvde_stdr_rcept_time': '17',
    'sltYear': '2023',
    'sltMonth': '03',
    'sltDay': '03',
    'yyyymm': '202303',
    'yyyy': '2023',
    'mm': '03',
    'dd': '03',
}

# context = ssl._create_unverified_context()
# response = urllib.request.urlopen(url, context=context)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# response = requests.post(url, data=palyload, verify=False)
# print(response.status_code)
# print(response.json().get('resultListDays'))

def message1():
    # 난지 D존
    response = requests.post(url, data=palyload, verify=False, headers={'User-Agent':'Mozilla/5.0'})
    cnt = 0
    message = "[" + "난지 캠핑장(03월 D형)" + "]" + " https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230211150852224390" + '\n'
    if response.status_code == 200:
        jsonData = response.json()
        for data in jsonData.get('resultListDays'):
            if data.get("SVC_RESVE_CODE") == "Y":
                if data.get("YMD") == "20230304":
                    cnt += 1
                    message = message + data.get("YMD")
        # print("message : ", message)
        if cnt > 0:
            print("message : ", message)
            asyncio.run(bot_send(message)) 
            # bot.sendMessage(chat_id=telegram_id, text=message)
            # bot_sst.sendMessage(chat_id=telegram_id_sst, text=message)
    else :
        print(response.status_code)

    # 난지 B존
    response = requests.post(url, data=palyload2, verify=False, headers={'User-Agent':'Mozilla/5.0'})
    cnt = 0
    message = "[" + "난지 캠핑장(03월 B형)" + "]" + " https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230211145025248959" + '\n'
    if response.status_code == 200:
        jsonData = response.json()
        for data in jsonData.get('resultListDays'):
            if data.get("SVC_RESVE_CODE") == "Y":
                if data.get("YMD") == "20230304":
                    cnt += 1
                    message = message + data.get("YMD")
        # print("message : ", message)
        if cnt > 0:
            print("message : ", message)
            asyncio.run(bot_send(message)) 
            # bot.sendMessage(chat_id=telegram_id, text=message)
            # bot_sst.sendMessage(chat_id=telegram_id_sst, text=message)
    else :
        print(response.status_code)    

    # 난지 C존
    response = requests.post(url, data=palyload3, verify=False, headers={'User-Agent':'Mozilla/5.0'})
    cnt = 0
    message = "[" + "난지 캠핑장(03월 C형)" + "]" + " https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230211150020900809" + '\n'
    if response.status_code == 200:
        jsonData = response.json()
        for data in jsonData.get('resultListDays'):
            if data.get("SVC_RESVE_CODE") == "Y":
                if data.get("YMD") == "20230304":
                    cnt += 1
                    message = message + data.get("YMD")
        # print("message : ", message)
        if cnt > 0:
            print("message : ", message)
            asyncio.run(bot_send(message)) 
            # bot.sendMessage(chat_id=telegram_id, text=message)
            # bot_sst.sendMessage(chat_id=telegram_id_sst, text=message)
    else :
        print(response.status_code)   

    # 난지 프리캠핑존
    response = requests.post(url, data=palyload4, verify=False, headers={'User-Agent':'Mozilla/5.0'})
    cnt = 0
    message = "[" + "난지 캠핑장(03월 프리캠핑형)" + "]" + " https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S230211151235143865" + '\n'
    if response.status_code == 200:
        jsonData = response.json()
        for data in jsonData.get('resultListDays'):
            if data.get("SVC_RESVE_CODE") == "Y":
                if data.get("YMD") == "20230304":
                    cnt += 1
                    message = message + data.get("YMD")
        # print("message : ", message)
        if cnt > 0:
            print("message : ", message)
            asyncio.run(bot_send(message)) 
            # bot.sendMessage(chat_id=telegram_id, text=message)
            # bot_sst.sendMessage(chat_id=telegram_id_sst, text=message)
    else :
        print(response.status_code)    

# step3.실행 주기 설정
schedule.every(10).seconds.do(message1)
# schedule.every(1).minutes.do(message1)

while True:
    schedule.run_pending()
    time.sleep(1)


