from bs4 import BeautifulSoup

from requests_html import HTMLSession
from pysitemap import crawler
from selenium import webdriver

path='C:\Windows\chromedriver.exe'

def get_links(*args):
    url= args[0]
    path='C:\Windows\chromedriver.exe'
    # driver = webdriver.Chrome(path)
    blog_links=[]
    Safe_links=[]
    # s= HTMLSession()
    # driver.get(url)
    # content= driver.page_source
    
    # content_soup= BeautifulSoup(content,'html.parser')
    # all_links= content_soup.find_all("a")
    # # print(all_links[0]['href'])
    # for i in range(len(all_links)):
    #     if "blog" in str(all_links[i]['href']):
    #         Safe_links.append((all_links[i]['href']))
       
    # print(Safe_links)

    uselessURL=[]
    crawler(url, out_file="AllLinks.xml")
    with open("AllLinks.xml") as f:
        link_soup= BeautifulSoup(f,'xml')
    soup_link= link_soup.find_all('loc')
    for i in range(len(soup_link)):
        if "json" not in str(soup_link[i].getText()) and "js" not in str(soup_link[i].getText()) and "css" not in str(soup_link[i].getText()) and "php" not in str(soup_link[i].getText()):
            
            if "blog" in str(soup_link[i].getText()) or "post" in str(soup_link[i].getText()) or "category" in str(soup_link[i].getText()):
                blog_links.append(soup_link[i].getText())

    print(blog_links)
    for i in range(len(blog_links)):
        blog_url= blog_links[i]
        driver = webdriver.Chrome(path)
        driver.get(blog_url)
        if "Page not found" in str(driver.title):
            pass
        else:

            blog_content= driver.page_source
        
            blog_soup= BeautifulSoup(blog_content,'html.parser')
            all_para = blog_soup.find_all("p")
            for j in range(len(all_para)):
                print(all_para[j].getText())

    
    #__________________________________________________

    # for item in blog_links:
    #     blog_url=item


if __name__ == '__main__':
    get_links('https://usbiomag.com/blog/')