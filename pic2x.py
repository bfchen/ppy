from PIL import Image
import os
import imghdr
import shutil


def resize(path, originPath, savePath):
    im = Image.open(path)
    originalPath = path
    tail = path.replace(originPath, '')
    singlePath = os.path.join(savePath, tail)
    # 二倍图路径
    componentes = singlePath.split("/")
    last = componentes.pop()
    diretory = "/".join(componentes)
    if not os.path.exists(diretory):
        os.makedirs(diretory)
    last = "@2x.".join(last.split("."))
    doublePath = os.path.join("/".join(componentes), last)
    # 复制二倍图
    shutil.copyfile(originalPath, doublePath)

    # 生成单倍图
    w, h = im.size
    im.thumbnail((w / 2, h / 2))
    im.save(singlePath, 'jpeg')


def createIcon(path, savePath):
    shutil.copyfile(path, savePath + "icon.png")
    im = Image.open(path)
    sizeList = [1024, 512, 167, 152, 76, 80, 40, 58, 29, 28, 20, 108, 16]
    for length in sizeList:
        newPath = savePath + "icon" + str(length) + ".png"
        im.thumbnail((length, length))
        im.save(newPath)


picPath = input("输入图片路径:").strip()
newPath = picPath.split("/")
newPath.pop()
newPath = "/".join(newPath)
newPath = os.path.join(newPath, "new")
if not os.path.exists(newPath):
    os.mkdir(newPath)
if "/" not in picPath[-1]:
    picPath += "/"
if "/" not in newPath[-1]:
    newPath += "/"


# 一倍图和二倍图
print("生成二倍图、单倍图中...")
for root, dirs, files in os.walk(picPath):
    for name in files:
        if name == "icon.png":
            continue
        path = os.path.join(root, name)
        if os.path.isdir(path):
            continue
        imageType = imghdr.what(path)
        # print ("type: ", imageType, type(imageType))
        if imageType == "jpeg" or imageType == "png":
            resize(path, picPath, newPath)

# icon
print("生成二倍图、单倍图完成")
print("生成icon中...")
iconDir = newPath + "icon/"
#print(iconDir)
if not os.path.exists(iconDir):
    os.mkdir(iconDir)
iconPath = picPath + "icon.png"
createIcon(iconPath, iconDir)
print("生成icon完成")
