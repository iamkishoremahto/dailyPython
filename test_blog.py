from bs4 import BeautifulSoup
from selenium import webdriver

driver= webdriver.Chrome('C:\Windows\chromedriver.exe')
driver.get('https://usbiomag.com/blog/biomagnetism-living-beyond-arthritis/')
content=(driver.page_source)
soup=BeautifulSoup(content,'html.parser')
print(soup.find_all("div",{"class":"single-content-full"})[0].getText())
# print(soup.find_all("div",{"class":"single-content-full"}).getText())
