from PIL import Image
import os
import imghdr
import shutil

def resize(path, originPath, savePath):
	print(path)
	print(originPath)
	print(savePath)
	originalPath = path
	tail = path - originPath
	print(tail)
	tail = "".join(tail)
	print(tail)
	path = os.path.join(savePath, tail)
	print("+++++", os.path.join(savePath, path))
	im = Image.open(path)
	w, h = im.size
	im.thumbnail((w/2, h/2))

	l = path.split("/")
	last = l.pop()
	path = '/'.join(l) + "/new/"
	if not os.path.exists(path):
		os.mkdir(path)

	copyPath = path + "@2x.".join(last.split("."))
	shutil.copyfile(originalPath, copyPath)
	# print(copyPath)
	newPath = os.path.join(path, last)
	# print(newPath)
	im.save(newPath, 'jpeg')



picPath = input("输入图片路径:").strip()
newPath = picPath.split("/")
newPath.pop()
newPath = "/".join(newPath)
newPath = os.path.join(newPath, "new")
if not os.path.exists(newPath):
	os.mkdir(newPath)
if not "/" in picPath[-1]:
	picPath += "/"
if not "/" in newPath[-1]:
	newPath += "/"
pisList = os.listdir(picPath)
# plist = [p + "/" for p in pisList if not "/" in p[-1]
for path in pisList:
	p = picPath+path
	# print(p)
	if os.path.isdir(p):
		continue
	imageType = imghdr.what(p)
	# print ("type: ", imageType, type(imageType))
	if imageType == "jpeg" or imageType == "png":
		resize(p, picPath, newPath)


