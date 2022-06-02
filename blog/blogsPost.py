from openpyxl import workbook
from bs4 import BeautifulSoup
import json
from requests_html import HTMLSession
from pysitemap import crawler
from selenium import webdriver
import pandas as pd
import requests
from urllib.request import urlopen


def get_url(*args):
    url= args[0]
    postUrl=[]
    
    crawler(url, out_file="All_url.xml")
    with open("All_url.xml" , errors='ignore') as f:
        link_soup= BeautifulSoup(f,'xml')
    soup_link= link_soup.find_all('loc')
    for link in soup_link:
        if "posts" in link.getText():
            postUrl.append(link.getText())
    # print(len(postUrl))
    # print(postUrl[3])
    driver = webdriver.Chrome()
    for i in range(len(postUrl)):
        if "json" in postUrl[i]:
            url=postUrl[i]
            driver.get(url)
        
            # post_soup= BeautifulSoup(driver.page_source, 'json')
            # pageDict= json.loads(page_source)
            # print(post_soup.find_all('link'))
            # print(post_soup[0].attrs['href'])
            json_url = urlopen(postUrl[i])

            data = json.loads(json_url.read())
            # print(data)
            Dict_title=(data.get('title'))
            Dict_title2=Dict_title.get("rendered")
            dis=data.get('content')
            print(Dict_title2)
            BlogDescription=(dis.get("rendered"))
            Blog_Description_soup= BeautifulSoup(BlogDescription,'html.parser')
            paragraph=(Blog_Description_soup.find_all('p'))
            print(Blog_Description_soup.getText())
            
            print("####################################################################################################################")
            print("####################################################################################################################")
            print("####################################################################################################################")
            # for para in Blog_Description_soup:
            #     print(para.getText())
            # print(data)
            # content=(data.get('link'))
            # driver.get(content)
            # content_data= driver.page_source
            # content_soup= BeautifulSoup(content_data,'html.parser')
            # para= content_soup.find_all('p')
            # for p in para:
            #     print(p.getText())
            
            
            
            
            # df = pd.DataFrame(page_source)
            # print(df)
            # df.to_excel("blog.xlsx", index=False)
if __name__ == '__main__':
    get_url('https://themindfool.com/')