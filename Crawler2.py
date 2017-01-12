# 爬取豆瓣首页
# 
import urllib.request
url = "http://www.douban.com"
request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

data = response.read()
data = data.decode('utf-8')

print(data)
print(type(data))
print(response.geturl())
print(response.info())
print(response.getcode())