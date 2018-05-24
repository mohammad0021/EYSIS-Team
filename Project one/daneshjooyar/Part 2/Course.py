#!/usr/bin/python
import re
import urllib
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
state = opener.open("https://www.daneshjooyar.com")

code = state.read()

Course = re.findall('''"(.+)" class="col-lg-3 col-sm-4 col-xs-12''',code,re.M)

f = open('Course.Link','w')

for i in Course:
	f.write(i)
	
f.close()
