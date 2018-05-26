#!/usr/bin/python
import re
import urllib
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
state = opener.open("https://adp.iaus.ac.ir/Dept/?DepID=7")

code = state.read()

State_Dept = re.findall("""imgug_2.+?'_blank'\s\s>(.+?)</a>""",code,re.M|re.DOTALL)

f=open('s','w')
f.write(State_Dept[0])
f.close()

print State_Dept
