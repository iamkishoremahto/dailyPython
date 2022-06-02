from ast import IsNot
from calendar import c
from bs4 import BeautifulSoup
from selenium import webdriver
from pysitemap import crawler



def get_blogs(*args):
    # crawler(args[0], out_file='usbiomag_urls.xml')
    with open('usbiomag_urls.xml') as f:
        url_soup= BeautifulSoup(f,'xml')
    all_urls= url_soup.find_all('loc')
    blog_urls_list=[]
    for i in range(len(all_urls)):
        if 'blog' in str(all_urls[i].getText()):
            blog_urls_list.append(all_urls[i].getText())

    path = 'C:\Windows\chromedriver.exe'
    driver = webdriver.Chrome(path)
    blogs_list=[]
    for j in range(1,len(blog_urls_list)):
        driver.get(blog_urls_list[j])
        if "Page not" not in  driver.title:
            content= driver.page_source
            blog_soup= BeautifulSoup(content,'html.parser')
        # if blog_soup :
        #     # blogLen= len(blog_soup)
        #     # for l in range(blogLen):
        # for k in range(len(blog_soup)):
            
            blogs=(blog_soup.find_all("div",{"class":"single-content-full"}))
            for k in range(len(blogs)):
                blogs_list.append(blogs[k].getText())

    # print(title)
    # for k in range(len(blogs)):
    for l in range(len(blogs_list)):
        print(f"{blogs_list[l]}")
    # print(urls_list)
    print(len(blogs_list))
    



if __name__ == '__main__':
    get_blogs('https://usbiomag.com/')
