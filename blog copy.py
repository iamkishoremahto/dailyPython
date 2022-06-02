import requests
from bs4 import BeautifulSoup as bs
from pysitemap import crawler
import xml.etree.ElementTree as ET

html_url=''

def get_url(*args):
    global html_url
    html_url = args[0] 
    crawler(html_url, out_file="Links.txt")
def Get_word_count():
    total_words_per_link=0
    total_Words_link=0
    total_url_link=0
    with open("Links.xml") as f:
        link_soup= bs(f,'xml')
    links= link_soup.find_all("loc")
    for i in range(len(links)):
        url2= links[i].getText()
        total_url_link= total_url_link + 1
        # print(url2)
        url= requests.get(url2)
        url_content=url.content
        soup= bs(url_content,'html.parser')
        para=soup.find_all('p')
        for j in range(len(para)):
            para_each=str(para[j].getText()).split(" ")
            total_words_per_link= total_words_per_link+len(para_each)
        print(f"{url2}  Total Words in this page is {total_words_per_link}")
        total_Words_link= total_Words_link+ total_words_per_link
        total_words_per_link=0
    
def get_list_pages():
    page_url= requests.get('https://james-camerons-avatar.fandom.com/wiki/Blog:Recent_posts')
    # page_url= requests.get(html_url)
    page_url_content=page_url.content
    page_soup=bs(page_url_content,'html.parser')
    # print(page_soup)
    page2= page_soup.find_all("ul",{"class":"wds-list wds-is-linked"})
    print(page2)
    # for ele in page2:
    #     print(ele.attrs['href'])
    
    # for p in range (len(page2)):
    #     print(page2[p].getText())
    
    # p2=len(page2)
    
    # # for k in range(p2):
    # #     pages= str(page_soup.find_all("nav")).split("<span>")[k].split("</span>")[0]
    # #     # pages_name=
    # #     print(k+1,pages)
    
    # # print(page3)
    # total_words_per_page=0
    # total_words_page=0
    # total_page_url=0
    # for l in range(p2):
    #     page3_url=str(page_soup.find_all("nav")).split("<li>")[l+3].split("<a")[1].split("href=\"")[1].split("\">")[0]
    #     total_page_url= total_page_url + 1
    #     # print(url2)
    #     url= requests.get(page3_url)
    #     url_content=url.content
    #     soup= bs(url_content,'html.parser')
    #     para=soup.find_all('p')
    #     for m in range(len(para)):
    #         para_each=str(para[m].getText()).split(" ")
    #         total_words_per_page= total_words_per_page+len(para_each)
    #     print(f"{page3_url}  Total Words in this page is {total_words_per_page}")
    #     total_words_page= total_words_page + total_words_per_page
    #     total_words_per_page=0
    
def blogs():
    page_url= requests.get('https://james-camerons-avatar.fandom.com/wiki/Blog:Recent_posts')
    # page_url= requests.get(html_url)
    page_url_content=page_url.content
    page_soup=bs(page_url_content,'html.parser')
    blogs_writter=page_soup.find_all("a",{"class":"blog-listing__user-name"})
    blogs_header=page_soup.find_all("h2",{"class":"blog-listing__title"})
    blogs_contant=page_soup.find_all("div",{"class":"blog-listing__summary"})
    print(blogs_writter)
    b_header_len=len(blogs_header)
    total_words_blog=0
    for n in range(b_header_len):
        print(n+1,blogs_writter[n].getText())
        print(blogs_header[n].getText())
        print(blogs_contant[n].getText())
        total_words_blog= total_words_blog +len(str(blogs_contant[n].getText()).split(" "))
    print("Total Words in blog :",total_words_blog)
    print("No of blogs : ",b_header_len)
    print("Average words per blog: ",total_words_blog/b_header_len)
    


    # print(soup.prettify)

    # data= url.content
    # soup= bs(data,'html.parser')
    

if __name__ == '__main__':
    # get_url('https://james-camerons-avatar.fandom.com/wiki/Blog:Recent_posts')
    
    Get_word_count()
    # get_list_pages()
    #blogs()

