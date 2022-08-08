import json
import base64
import hashlib
import hmac

def encode (x): #Процедура кодировкивки в base64
  type_encode = reqest.encode("UTF-8")
  base_encode = base64.b64encode(type_encode)
  return base_encode.decode("UTF-8")

def make_digest(message, key): #Процедура хеширование в SHA1 и кодировки в BASE64
  key = bytes(key, 'UTF-8')
  message = bytes(message, 'UTF-8')
  digester = hmac.new(key, message, hashlib.sha1)
  signature1 = digester.digest()
  signature2 = base64.b64encode(signature1)    
  return str(signature2, 'UTF-8')
  
  
reqest = {"type":"getSession","merchant":"000000020000001","tranid":"268942a1-6bd4-49bf-950f-dc12e459728b","ordertype":"2","callback":"","description":"null","amount":"10","fee":"0","currency":"980","clientParams":{"cardHolderName":"KOLESNYK SERHII","billAddrCity":"Mykolaiv","billAddrCountry":"UA","billAddrLine2":"","billAddrLine1":"st. Potomkinska b.127","billAddrPostCode":"54000","billAddrState":"Mykolaivska oblast","billMobilePhone":"+380684256838","billEmail":"kolesnk.s@gmail.com"},"browserParams":{"browserAcceptHeader":"*/*","browserUserAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","browserLanguage":"ru","browserTZ":"-180","browserColorDepth":"30","browserJavaEnabled":"false","browserIp":"3.11.37.216","browserScreenHeight":"1200","browserScreenWidth":"1920","windowHeight":"910","windowWidth":"426"}}
private_key = '	A0BF2AC6B66E2BFA9C1672BBA817722F'
reqest_str=str(reqest)
reqest_eval=eval(reqest_str)
reqests = json.dumps(reqest_eval)
reqest = reqests.replace(" ","").replace('/', r'\/')
type_encode1 = encode(x=reqest)
contact = private_key+type_encode1+private_key
pre_signature = make_digest(contact,private_key)
reqest_json = json.loads(reqest)
reqest_json['sign'] = pre_signature
singed_reqest = json.dumps(reqest_json)
print(singed_reqest)
