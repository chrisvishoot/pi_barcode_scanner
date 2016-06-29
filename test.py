import urllib2
import re

response = urllib2.urlopen('https://www.upcdatabase.com/item/0071990095116')
html = response.read()

match = re.search("<tr><td>Description</td><td></td><td>(.*?)</td></tr>", html)
print match.group(1)
