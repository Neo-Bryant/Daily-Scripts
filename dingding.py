import requests
import json
import sys

def send_msg(url,reminders,contents):
    headers = {'Content-Type': 'application/json;utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": contents
        },
        "at": {
            "atMobiles": reminders,
            "isAtAll": False
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.text

if __name__ == '__main__':
    contents = sys.argv[1]
    reminders = ["18825179357"]
    url = 'https://oapi.dingtalk.com/robot/send?access_token=c217f9c4184060594d37c6bba5ee726f495f0f2db3b0632399b000e18208db23'
    print(send_msg(url,reminders,contents))
