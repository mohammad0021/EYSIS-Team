#!/usr/bin/python
import re
import urllib
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
state = opener.open("https://adp.iaus.ac.ir/Dept/?DepID=7")

code = state.read()

State_Dept = re.findall("""javascript:void.+>(.+)</a>""",code,re.M)

if "\xda\xa9\xd8\xa8\xd8\xb1\xd9\x8a" in State_Dept[0] :
	print "Notifications from Cobra"
