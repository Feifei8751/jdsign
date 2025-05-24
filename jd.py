import os
import requests

#微信推送
def get_access_token():
    # 获取access token的url
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appID}&secret={appsecret}'
    response = requests.get(url).json()
    print(response)
    access_token = response.get('access_token')
    return access_token

def send(txt,txt1):
    body = {
        "touser": touser,
        "template_id": template_id,
        "url": "https://www.655300.xyz",
        "data": {
            "text": {
                "value": txt
            },
            "text1": {
                "value": txt1
            }
        }
    }
    url = f'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={get_access_token()}'
    print(requests.post(url, json.dumps(body)).text)


cookie = os.environ.get("JD_COOKIE")

url = ("https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1"
       "%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1"
       "%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14"
       ".8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp"
       "=jsonp_1645885800574_58482")

headers = {"Connection": 'keep-alive',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Cache-Control": 'no-cache',
           "User-Agent": "okhttp/3.12.1;jdmall;android;version/10.3.4;build/92451;",
           "accept": "*/*",
           "connection": "Keep-Alive",
           "Accept-Encoding": "gzip,deflate",
           "Cookie": cookie
           }

response = requests.post(url=url, headers=headers)
print(response.text)
appID=os.getenv('appID')
appsecret=os.getenv('appsecret')
touser=os.getenv('touser')
template_id=os.getenv('template_id')
send('京东领京豆','领取成功！')
