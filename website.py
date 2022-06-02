import requests
from bs4 import BeautifulSoup
#https://backlinko.com/nofollow-link
# https://en.wikipedia.org/wiki/Linux
url =requests.get('https://www.ambitionbox.com/overview/vmoksha-technologies-overview')
data=url.content
soup = BeautifulSoup(data,'html.parser')
parapettify=soup.prettify()
para = soup.find_all('div')
para2= str(para)
para3= para2.split("</p>,")
# print(data)

# print(para2.find(""))
for item in para3:
    print(item +"\n")

# print(soup)
#links = soup.find_all('a')
# title=soup.title
# print(title)
#data2= soup.prettify()
# data3= soup.find_all("a")
# for link in data3:
#     print(link)

# for link in data3:
