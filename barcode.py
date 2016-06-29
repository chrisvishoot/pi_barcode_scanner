#!/usr/bin/python
from sys import argv
import zbar
import urllib2
import re

# import urllib2
#
# response = urllib2.urlopen('https://www.upcdatabase.com/')
# html = response.read()

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]

#proc.request_size(800,480)

proc.init(device)

# enable the preview window
proc.visible = True

# read at least one barcode (or until window closed)
proc.process_one()

# hide the preview window
proc.visible = False


# extract results
for symbol in proc.results:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
    barcode = symbol.data
    url = "https://www.upcdatabase.com/" + str(barcode)
    response = urllib2.urlopen(url)
    html = response.read()
    match = re.search("<tr><td>Description</td><td></td><td>(.*?)</td></tr>", html)
    print match.group(1)
