# coding:utf-8

import os
import shutil

picPath = input("输入文件夹路径:").strip()
head = picPath.split("/")
# glass directory
tail = head.pop()
head = "/".join(head)
newPath = os.path.join(head, "new")
newPath = os.path.join(newPath, tail)
if os.path.exists(newPath):
    shutil.rmtree(newPath)

# print (head)
# print (newPath)

# 一倍图和二倍图
# print("生成中...")
count = len(picPath.split("/"))
# print (count)
for root, dirs, files in os.walk(picPath):

    for file in files:
        path = os.path.join(root, file)
        l = path.split("/")
        # print (path)
        count1 = len(l)
        # print ("count1:", count1)
        # print (len(l))
        # print (count1-count)

        if (count1 - count == 2):
            propert = l[-3]
            if propert == "玻璃":
                propert = "工艺"+"玻璃"

            newTail = "/".join([l[-2], "本系列共享的颜色属性", propert, l[-1]])
            print ("????",l);
            toPath = os.path.join(newPath, newTail)
            ldir = toPath.split("/")
            ldir.pop()
            toDir = "/".join(ldir)
            if not os.path.exists(toDir):
                os.makedirs(toDir)
            shutil.copy2(path, toPath)
        elif count1 - count == 3:
            # print (l)
            newList = l
            # print (l)
            name = newList.pop().split(".")[0]
            # print ("name", name)
            propert = l[-3]
            if propert == "玻璃":
                propert = "工艺"+"玻璃"
            toPath = "/".join([l[-2], name, propert, l[-1]+".png"])
            # print ("&&&&", toPath)
            # print (l)
            toPath = os.path.join(newPath, toPath)
            ldir = toPath.split("/")
            ldir.pop()
            toDir = "/".join(ldir)
            # print ("toDir>>>>>>>>", toDir)
            # print ("toPath>>>>>>>", toPath)
            if not os.path.exists(toDir):
                os.makedirs(toDir)
            shutil.copy2(path, toPath)
            # newTail = "/".join([l[-2], "本系列共享的颜色属性", "工艺玻璃", l.pop()])
            # print ("newTail: **********", newTail)
            # toPath = os.path.join(newPath, newTail)
            # ldir = toPath.split("/")
            # ldir.pop()
            # toDir = "/".join(ldir)
            # print ("toDir>>>>>>>>", toDir)
            # print ("toPath>>>>>>>", toPath)
            # if not os.path.exists(toDir):
            #     os.makedirs(toDir)
            # shutil.c
#         secondPath = os.path.join(root, dir)
#         for root1, dir1s, files1 in os.walk(secondPath):
#             for file in files1:
#                 old = os.path.join(root1, file)
#                 newTail = (old.split(picPath))
#                 new = newPath + newTail[1]
#                 # print(new)
#                 # new =
#
#                 l = new.split(".")
#                 l.pop()
#                 p = "/".join(l)
#
#                 os.makedirs(p)
#                 name = p.split("/").pop()
#                 new = p + "/" + name + ".png"
#                 shutil.copy2(old, new)
                # os.remove(old)

print("完成")




