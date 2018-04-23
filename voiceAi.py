#-*- coding: utf-8 -*-
import sys,string
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib, yaml, json
import os
import vop2
Client_Id = 'WsWs6yVQcHAcHUFr0uRPxngu'
Client_Secret = 'qApo0sCYLy0sRxPRCUZ43w02a06zIGn0'
cuid = '9eoiqwe023'
turingKey = '12b311c1acd2456c877ecec69123865b'
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def save_to_file(file_name, contents):
	fh = open(file_name, 'w')
	fh.write(contents)
	fh.close()
def getToken():
	global Client_Id
	global Client_Secret
	url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + Client_Id + '&client_secret=' + Client_Secret
	response = getHtml(url)
	dic_json = json.loads(response)
	return dic_json['access_token']

def speak(text):
	global cuid
	token = getToken()
	#print text
	url = 'http://tsn.baidu.com/text2audio?tex=' + text + '&lan=zh&per=4&spd=5&cuid=' + cuid + '&ctp=1&tok=' + token
	#save_to_file('output.wav', getHtml(url))
	#os.popen('mpg123 "%s" > /dev/null' %(url)).read()
	os.system('mpg123 -q -s -w output.wav "%s"' %(url)) 
	os.system('aplay -q output.wav')
	#os.system('mpg123 -q "%s"' %(url)) 
	

if __name__ == '__main__':
	api = 'http://www.tuling123.com/openapi/api?key=' + turingKey + '&info='
	while True:
		info = raw_input('Push Space Key to speak: ')
		if info != '' :
			os.system('arecord -f S16_LE -d 2.5 -r 8000 input.wav')
			token = getToken()
			#use vop2's function to get text
			res = yaml.safe_load(vop2.use_cloud(token))
			if res['err_no'] == 0 :
				text = res['result'][0].encode('utf-8')
				print 'Me: ' + text
				request = api + text
				response = getHtml(request)
				dic_json = json.loads(response)
				print 'Robot: '.decode('utf-8') + dic_json['text']
				text = urllib.quote(dic_json['text'].decode("utf-8").encode("utf-8"))
				speak(text)
