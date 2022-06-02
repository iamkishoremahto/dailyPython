
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

path ='C:\Windows\chromedriver.exe'
driver = webdriver.Chrome(path)

def get_url(*args):
    driver.get(args[0])
    # url= requests.get(args[0])
    # content= url.content
    content= driver.page_source
    soup= BeautifulSoup(content,'html.parser')
    print(soup)
    all_courses = soup.find_all("a",{"class":"bb-course-title "})
    print(all_courses)

if __name__ == '__main__':
    get_url('https://vault.internetmarketing.gold/courses/')