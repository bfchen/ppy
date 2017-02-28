from PIL import Image, ImageDraw, ImageFont

img = Image.open('1.jpg')
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('myf.ttf', size = 50)
width, height = img.size
draw.text((40, 40), 'hello', font = myfont, fill = "#000000")
img.save('result.jpg', 'jpeg')

