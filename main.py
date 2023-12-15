import os
import time
import json
import schedule
import requests
from dotenv import load_dotenv


def checkin():

    headers={'Cookie': os.getenv("LUOGU_COOKIE"),
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    response=requests.get('https://www.luogu.com.cn/index/ajax_punch', headers=headers)

    res=json.loads(response.content.decode("unicode_escape"))

    print(res.get("message"))


load_dotenv()

if (os.getenv("LUOGU_COOKIE") == None):
    print("Cannot read LUOGU_COOKIE in .env file, please make sure that you have already configured envirment variables.")


schedule.every().days.at("10:00", "Asia/Shanghai").do(checkin)

while True:
    schedule.run_pending()
    time.sleep(1)