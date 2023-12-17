import time
import json
import schedule
import requests


def getConfig():
    with open('config.json', 'r') as configFile:
        global config
        config = json.load(configFile)


def checkin():
    for luoguCookie in config.get('token'):

        headers={'Cookie': '__client_id=' + luoguCookie.get('__client_id') + '; _uid=' + str(luoguCookie.get('_uid')) + ';',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

        response=requests.get('https://www.luogu.com.cn/index/ajax_punch', headers=headers)

        res=json.loads(response.content)

        print('正在打卡：uid = ' + str(luoguCookie.get('_uid')))

        if (response.status_code != 200):
            print('打卡失败，错误信息：')
            print(response)
        else:
            if (res.get('code') == 200):
                print('打卡成功！')
            if (res.get('code') == 201):
                print('今天已经打过卡了')


getConfig()

checkin()

# schedule.every().days.at('10:00', 'Asia/Shanghai').do(checkin)

while True:
    schedule.run_pending()
    time.sleep(1)