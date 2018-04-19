# -*- coding: utf-8 -*-
import urllib
import simplejson
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def getToken():
	
if __name__ == '__main__':
	key = '12b311c1acd2456c877ecec69123865b'
	api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
	while True:
		info = raw_input('我: ')
		request = api + info
		response = getHtml(request)
		dic_json = simplejson.loads(response)
		print '机器人: '.decode('utf-8') + dic_json['text']
