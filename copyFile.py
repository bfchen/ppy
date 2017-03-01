#coding:utf-8

import os
import shutil


picPath = input("输入文件夹路径:").strip()
head = picPath.split("/")
tail = head.pop()
head = "/".join(head)
newPath = os.path.join(head, "new")
newPath = os.path.join(newPath, tail)
if os.path.exists(newPath):
    shutil.rmtree(newPath)


# 一倍图和二倍图
print("生成中...")
for root, dirs, files in os.walk(picPath):
    for dir in dirs:
        secondPath = os.path.join(root, dir)
        for root1, dir1s, files1 in os.walk(secondPath):
            for file in files1:
                old = os.path.join(root1, file)
                newTail = (old.split(picPath))
                new = newPath+newTail[1]
                # print(new) 
                # new = 
                
                l = new.split(".")
                l.pop()
                p = "/".join(l)

                os.makedirs(p)
                name = p.split("/").pop()
                new = p + "/"+ name+ ".png"
                shutil.copy2(old, new)
                # os.remove(old)

print("完成")




