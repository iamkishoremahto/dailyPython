from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from openpyxl import workbook

def blogs(*args):
    path ='C:\Windows\chromedriver.exe'
    driver = webdriver.Chrome(path)
    content= driver.page_source
    soup = BeautifulSoup(content,'html.parser')
    Blogs_url= soup.find_all("a",{"class":"blog-button"})
    print(Blogs_url)

if __name__ == '__main__':
    blogs('https://usbiomag.com/blog/')