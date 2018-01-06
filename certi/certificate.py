from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from xlrd import open_workbook

wb = open_workbook('Extras.xlsx')
s = wb.sheet_by_index(0)

font1 = ImageFont.truetype('TCB_____.TTF',170)
font2 = ImageFont.truetype('TCM_____.TTF',132)

W, H = (2480,3508)
for x in range(1):	
	im = Image.open('certificate.jpg')
	draw = ImageDraw.Draw(im)
	msg1 = str(s.cell(x,0).value).upper()
	msg2 = str(s.cell(x,1).value).upper()
	msg3 = str(s.cell(x,2).value).upper()	
	w1, h1 = draw.textsize(msg1,font = font1)
	w2, h2 = draw.textsize(msg2,font = font2)
	w3, h3 = draw.textsize(msg3,font = font1)
	draw.text(((W-w1)/2,1500),msg1,fill = "#127369",font = font1)
	draw.text(((W-w2)/2,1750),msg2,fill = "#127369",font = font2)
	draw.text(((W-w3)/2,2000),msg3,fill = "#127369",font = font1)
	im.save("IMG"+str(x+567)+".jpg","JPEG")
