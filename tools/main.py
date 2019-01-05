import requests
#from bs4 import BeautifulSoup
import re,json

def getUrl():
	bingUrl = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1546656919100&pid=hp"
	html = requests.get(bingUrl)
	jsonUrl = json.loads(html.text)
	url = jsonUrl['images'][0]['url']
	return url

def downloadImg(url):
	jpgUrl ="https://cn.bing.com/{0}".format(url)
	#print(jpgUrl)
	req = requests.get(jpgUrl)
	if req.status_code == 200:
		with open("bingWallpaper.jpg",'wb') as f:
			f.write(req.content)

if __name__ == '__main__':
	url = getUrl()
	downloadImg(url)


#print(soup.prettify())
'''
style = soup.select('#bgDiv')
print(style)
pattern  = re.compile(r"g_img=(.*?);", re.MULTILINE | re.DOTALL)
#script = soup.find("script", text=pattern)
jsScript = soup.body.find('script',text=pattern)
jsStr = pattern.search(jsScript.text).group(1).replace("\'","\"")
print(jsStr)
json = json.loads(jsStr)
#print(json['url'])
'''