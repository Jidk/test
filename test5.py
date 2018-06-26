import requests
from bs4 import BeautifulSoup

def getContent(_rul):
	result = requests.get(_rul, 'html.parser')
	soup = BeautifulSoup(result.text, 'html.parser')

	main = soup.find(id="main-container")
	content = main.text.split("※ 發信站:")[0]
	print(content)

url = 'https://www.ptt.cc'
n = 1
while True:
	html = requests.get("https://www.ptt.cc/bbs/MobileComm/index{x}.html".format(x=str(n)),'html.parser')
	if html.status_code == 200:
		s = BeautifulSoup(html.text, 'html.parser')

		for i in s.find_all('div',{"class":"r-ent"}):
			for j in i.find_all('div',{"class":"title"}):
				getContent(url + j.find('a').get('href'))
	else:
		break
	n += 1
