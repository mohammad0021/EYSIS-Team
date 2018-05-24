#!/usr/bin/python
import re
import urllib
import urllib2

Link = "https://www.daneshjooyar.com/category/%d8%a2%d9%85%d9%88%d8%b2%d8%b4-%d9%87%d8%a7%db%8c-%d9%85%d8%af%d8%b1%d8%b3%db%8c%d9%86/%d9%85%d8%af%d8%b1%d8%b3-%d8%a7%da%a9%d8%a8%d8%b1%db%8c-%d9%85%d9%86%d8%b4/"
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
state = opener.open(Link)

code = state.read()

Course = re.findall('''"(.+)" class="col-lg-3 col-sm-4 col-xs-12''',code,re.M)

f = open('Course.Link','w')

for i in Course:
	f.write(i)
	
f.close()
