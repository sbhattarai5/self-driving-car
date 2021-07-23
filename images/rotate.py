"""
To create rotations of image file.
"""


import os

filename = 'taxi.png'

ext = filename.split('.')[-1]
filename = filename.split('.')[0]

startdeg = 0
enddeg = 360
ddeg = 10
for i in range(startdeg, enddeg, ddeg):
    os.system("convert -rotate %s -background 'rgba(0,0,0,0)' %s.%s %s-%s.%s" % (i, filename, ext, filename, ext, i))
