from bs4 import BeautifulSoup
import requests



print("Welcome to Uri Scrapper. You can findout any problems that your friend or other selected user has solved")

url = input("Enter the url of the profile's url of that person you wanna scrap: ")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
l = soup.find('div', class_='list')
element = l.find('div', id='element')
table = element.find('table')
trs = table.find_all('tr')
f = open('problems.txt', 'w+')
for tr in trs:
    # print(tr)
    idtd = tr.find('td', class_="id")
    try:
        id = idtd.a.text
        name = tr.find('td', class_="wide").text
        f.write(f"{id} - {name}\n")
    except AttributeError:
        continue
print("--DONE--")
f.close()