#!/usr/bin/python
import re
import urllib
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
state = opener.open("https://www.daneshjooyar.com/security-on-php-websites/")

code = state.read()

User_list = re.findall('''"name">(.+)</span>''',code,re.M)

f = open('Users','w')

for i in User_list:
	f.write(i)

f.close()
