import os

filename = "Mini_van"
width = 46
os.system("convert -resize %s %s.png %s_small.png" % (width, filename, filename))

# convert example.png -resize 200 example.png
