#!/usr/bin/python3
# -*- coding:UTF-8 -*-


import requests
import lxml.html
import sys


url = sys.argv[1]


for i in range(1,10000):
	html = requests.get(url= url+'/home.php?uid={0}'.format(i),verify=False).content
	selector = lxml.html.fromstring(html)
	res = selector.xpath("///a/text()")
	res1 = selector.xpath("///a/@href")
	print(res[-5])
