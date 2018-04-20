#-*- coding: utf-8 -*-
import base64, requests, urllib
import simplejson
import os
Client_Id = 'WsWs6yVQcHAcHUFr0uRPxngu'
Client_Secret = 'qApo0sCYLy0sRxPRCUZ43w02a06zIGn0'
cuid = '9eoiqwe023'
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def getToken():
	global Client_Id
	global Client_Secret
	url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + Client_Id + '&client_secret=' + Client_Secret
	response = getHtml(url)
	dic_json = simplejson.loads(response)
	return dic_json['access_token']
d = open('hello.wav', 'rb').read()
token = getToken()
data = {
    #"format": "pcm",
    "format": "wav",
    "rate": 8000,
    "channel": 1,
    "token": token,
    "cuid": cuid,
    "len": len(d),
    "speech": base64.encodestring(d).replace('\n', '')
}
result = requests.post('http://vop.baidu.com/server_api', json=data, headers={'Content-Type': 'application/json'})
data_result = result.json()
print data_result['err_msg']
if data_result['err_msg']=='success.':
    print "语音结果：" + data_result['result'][0].encode('utf-8')
else:
    print data_result
