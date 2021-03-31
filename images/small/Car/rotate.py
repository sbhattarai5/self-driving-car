import os

filename = 'Car'
for i in range(0, 360, 10):
    os.system("convert -rotate %s -background 'rgba(0,0,0,0)' %s.png %s-%s.png" % (i, filename, filename, i))
              
