import re
import urllib
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
state = opener.open("https://www.daneshjooyar.com")

code = state.read()

Pattern1 = re.compile('''<li class="cat-item cat-item-12303">(.+?)</ul>''',re.M|re.DOTALL)
base1 = re.findall(Pattern1,code)

Pattern2 = re.compile('''<a href="(.+)" >''',re.M)
Page = re.findall(Pattern2,base1[0])

f = open("2.html","w")

for i in Page:
    f.write(i)

f.close()

