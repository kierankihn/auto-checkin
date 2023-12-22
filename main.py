import time
import json
import logging
import schedule
import requests


handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s %(filename)s %(levelname)s - %(message)s"))
infoLogger = logging.getLogger('checkin_info')
infoLogger.setLevel(logging.INFO)
infoLogger.addHandler(handler)
errorLogger = logging.getLogger('checkin_error')
errorLogger.setLevel(logging.ERROR)
errorLogger.addHandler(handler)


def getConfig():
    """
    Reads the contents of the 'config.json' file and loads it into the global variable 'config'.

    Parameters:
        None

    Returns:
        None
    """
    with open('config.json', 'r') as configFile:
        global config
        config = json.load(configFile)



def checkin():
    """
    This function is responsible for performing the check-in process. 
    It sends a GET request to the Luogu website with the necessary headers and cookies to authenticate the user. 
    After receiving the response, it checks the status code and prints the appropriate message based on the result. 
    If the check-in is successful, it prints 'Check-in successful!'. 
    If the user has already checked in today, it prints 'Already checked in today.'. 
    If there is an error during the check-in process, it prints the error message returned by the server.

    Parameters:
        None

    Returns:
        None
    """
    for luoguCookie in config.get('token'):

        headers={'Cookie': '__client_id=' + luoguCookie.get('__client_id') + '; _uid=' + str(luoguCookie.get('_uid')) + ';',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

        response=requests.get('https://www.luogu.com.cn/index/ajax_punch', headers=headers)

        res=json.loads(response.content)

        infoLogger.info('Checking in: uid = ' + str(luoguCookie.get('_uid')))

        if (response.status_code != 200):
            errorLogger.error('Check in failed, error message:\n' + response)
        else:
            if (res.get('code') == 200):
                infoLogger.info('Check in successful!')
            if (res.get('code') == 201):
                infoLogger.info('Already checked in today.')


getConfig()

schedule.every().days.at('10:00', 'Asia/Shanghai').do(checkin)

while True:
    schedule.run_pending()
    time.sleep(1)