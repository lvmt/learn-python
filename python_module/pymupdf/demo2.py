import fitz
import gzip

# import one of the symbols
# from shapes_and_symbols import heart

# open empty output PDF
doc = fitz.open()

# make new page, square dimensions
page = doc.newPage(-1, width = 256, height = 256)

# start a Shape object
img = page.newShape()

# define some color
red = (1,0,0)

# create symbol on page
heart(img, page.rect, red)

# and commit it
img.commit()

# now turn page into SVG image
txt = page.getSVGimage()

# and compress it
txt_gzip = gzip.compress(txt.encode("utf-8"))
fout = open("heart.svgz", "wb")
fout.write(txt_gzip)
fout.close()