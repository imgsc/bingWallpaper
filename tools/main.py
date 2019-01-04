import requests
from bs4 import BeautifulSoup
import re,json

bingUrl = "https://cn.bing.com/"
html = requests.get(bingUrl)
soup = BeautifulSoup(html.text,"lxml")
#print(soup.prettify())

pattern  = re.compile(r"g_img=(.*?);", re.MULTILINE | re.DOTALL)
#script = soup.find("script", text=pattern)
jsScript = soup.body.find('script',text=pattern)
jsStr = pattern.search(jsScript.text).group(1).replace("\'","\"")
print(jsStr)
json = json.loads(jsStr)
#print(json['url'])