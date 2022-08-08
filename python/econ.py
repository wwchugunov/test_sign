import json
import base64
import hashlib
import hmac
import random
import requests
from datetime import datetime


pan = 4441114403682477
cvv = 666
exp = 2909
key_API = "mkmFFINdHDr0tQ=u3piUYUwptXeYOalTisRXOIWifVnsw"
terminal = "TE1575"
ordertype = 2
amount = 1



def encode (x): #Процедура кодировкивки в base64
    type_encode = x.encode("UTF-8")
    base_encode = base64.b64encode(type_encode)
    return base_encode.decode("UTF-8")


def make_digest(message, key): #Процедура хеширование в SHA1 и кодировки в BASE64
    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')
    digester = hmac.new(key, message, hashlib.sha1)
    signature1 = digester.digest()
    signature2 = base64.b64encode(signature1)    
    return str(signature2, 'UTF-8')


def signature(req_data):
    reqest_str=str(req_data)
    reqest_eval=eval(reqest_str)
    reqests = json.dumps(reqest_eval)
    reqest = reqests.replace(" ","").replace('/', r'\/')
    private_key = key_API
    type_encode1 = encode(x=reqest)
    contact = private_key+type_encode1+private_key
    pre_signature = make_digest(contact,private_key)
    reqest_json = json.loads(reqest)
    reqest_json['sign'] = pre_signature
    singed_reqest = json.dumps(reqest_json)
    return singed_reqest


def post_reqest(send):
    url = 'https://api-inst2.paylink.com.ua/'
    headers = {'Content-type': 'application/json',  # Определение типа данных
            'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
    requests_sid = requests.post(url, data=send, headers=headers)
    respons = requests_sid.json()

    current_datetime = datetime.now()
    print(current_datetime)
    print(respons)
    return respons

param_for_reqest = {
    "type":"getSession",
    "merchant":terminal,
    "tranid":str(random.randint(10000, 999999)),
    "callback":"",
    "ordertype":str(ordertype),
    "description":"Оплата test",
    "amount": str(amount),
    "fee": "0",
    "currency": "980",
    "clientParams": {
        "cardHolderName": "KOLESNYK SERHII",
        "billAddrCity": "Kyiv",
        "billAddrCountry": "804",
        "billAddrLine3": "",
        "billAddrLine2": "",
        "billAddrLine1": "Hazoprovidna St, 9",
        "billAddrPostCode": "01001",
        "billAddrState": "30",
        "billMobilePhone": "380684256838",
        "billEmail": "kolesnk.s@gmail.com"
    },
    "browserParams": {
        "browserAcceptHeader": "*/*",
        "browserUserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "browserLanguage": "ru",
        "browserTZ": "-180",
        "browserColorDepth": "32",
        "browserJavaEnabled": "false",
        "browserIp": "3.11.37.216",
        "browserScreenHeight": "1200",
        "browserScreenWidth": "1920",
        "windowHeight": "910",
        "windowWidth": "426"
    }
}
singed_reqest_rt= signature(param_for_reqest)
print(singed_reqest_rt)
response= post_reqest(singed_reqest_rt)
if "sid" in response:
    sid = response.get("sid")

param_for_reqest_f = {
    "type":"purchase",
    "sid":sid,
    "pan":str(pan),
    "expdate":str(exp),
    "cvv":str(cvv)
    }
singed_reqest_rt= signature(param_for_reqest_f)
print(singed_reqest_rt)
response= post_reqest(singed_reqest_rt)

pre_reqest = {"type":"getTranState", "sid":sid}
singed_reqest_rt= signature(pre_reqest)
print(singed_reqest_rt)
response= post_reqest(singed_reqest_rt)





print("https://inst2.paylink.com.ua/frame/ecom/result.html?sid="+sid)