import urllib.request, socket, re, sys, os


targetPath = "/Users/admin/Desktop/file/images"



def saveFile(path):
	if not os.path.isdir(targetPath):
		os.mkdir(targetPath)

	pos = path.rindex('/')
	t = os.path.join(targetPath, path[pos+1:])
	return t


url = "https://www.douban.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
                        
req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
data = res.read()

for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
	print(link)
	try:
		urllib.request.urlretrieve(link, saveFile(link))
	except:
		print('失败')