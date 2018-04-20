#-*- coding: utf-8 -*-
import sys,string
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import simplejson
import os
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
	dic_json = simplejson.loads(response)
	return dic_json['access_token']

def getFile(text):
	global cuid
	token = getToken()
	print text
	url = 'http://tsn.baidu.com/text2audio?tex=' + text + '&lan=zh&per=1&spd=5&cuid=' + cuid + '&ctp=1&tok=' + token
	#save_to_file('voice.wav', getHtml(url))
	#c = "wget \"%s\" -O \"%s\"" % (url, "voice.mp3")
	#os.system(c.encode('utf-8'))
	os.popen('mpg123 "%s" > /dev/null' %(url)).read()
	#os.system('mpg123 "%s" > /dev/null' %(url)) 
	

if __name__ == '__main__':
	api = 'http://www.tuling123.com/openapi/api?key=' + turingKey + '&info='
	while True:
		info = raw_input('me: ')
		request = api + info
		response = getHtml(request)
		dic_json = simplejson.loads(response)
		print 'Robot: '.decode('utf-8') + dic_json['text']
		text = urllib.quote(dic_json['text'].decode("utf-8").encode("utf-8"))
		getFile(text)
