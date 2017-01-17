from PIL import Image
import os


def resize(path):
	im = Image.open(path)
	w, h = im.size
	im.thumbnail((w/2, h/2))

	l = path.split("/")
	print("---",l)
	last = l.pop()
	print("+++", last)

	print("0000", l)
	path = '/'.join(l) + "/new/" + "@2x.".join(last.split("."))
	print("%%%%%:", path)
	im.save(path, 'jpeg')


path = "/Users/admin/Desktop/a/0.jpg"
l = path.split('/')
print(l)
print('/'.join(l))

picPath = input("输入图片路径:") 
if not "/" in picPath[-1]:
	picPath += "/"
pisList = os.listdir(picPath)
for path in pisList:
	if "jpg" in path or "png" in path:
		
		resize(picPath + path)
# resize(path)


