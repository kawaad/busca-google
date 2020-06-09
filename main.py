import urllib
import requests
from bs4 import BeautifulSoup

query = input() + " site:ifb.edu.br" #site exemplo
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

headers = {"user-agent" : USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")

results = []

for g in soup.find_all('div', class_='r'):
    anchors = g.find_all('a')
    if anchors:
        link = anchors[0]['href']
        title = g.find('h3').text
        item = {
            "title = ": title,
            "link = ": link
        }
        results.append(item)

for i in range(0, 3):
	for resultado,conteudo in (results[i].items()):
		print(conteudo)
