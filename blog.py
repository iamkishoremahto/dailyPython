import requests
from bs4 import BeautifulSoup as bs
from pysitemap import crawler
import xml.etree.ElementTree as ET
import logging
import logging.config
import sys

# Logger configuration 
logger = logging.getLogger(__name__)  #assigning name for the logger
logger.setLevel(logging.INFO)   #set level of the logging
f= logging.Formatter('%(asctime)s - %(message)s') # set output formate
fh = logging.FileHandler('blog.log') # set logging handler file for records the logging output
fh.setFormatter(f)  # set format
logger.addHandler(fh) #assign file hendler to the logger





# html_url=''




def get_url(*args):
    
    html_url = args[0] 
    crawler(html_url, out_file="Links.xml")
    Get_word_count()
    blogs(html_url)
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
        
        logger.info(f"{url2}  Total Words in this page is {total_words_per_link}")
        total_Words_link= total_Words_link+ total_words_per_link
        total_words_per_link=0
    logger.info(f"Total Url : {total_url_link}")
    logger.info(f"Total Words : {total_Words_link}")
        
    
def get_list_pages():
    urls=[]
    page_url=[]
    with open("Links.xml") as f:
        link_soup= bs(f,'xml')
    links= link_soup.find_all("loc")
    for i in range(len(links)):
        urls.append(links[i].getText())
    for j in range(len(urls)):
        str_url=str(urls[j])
        if "desktop" in str_url:
            return page_url.append(str_url)
    logger.info(page_url[1])

            

    
    # page_url= requests.get('https://james-camerons-avatar.fandom.com/wiki/Blog:Recent_posts')
    # # page_url= requests.get(html_url)


    # page_url_content=page_url.content
    # page_soup=bs(page_url_content,'html.parser')
    # # print(page_soup)
    # page2=str(page_soup.find_all("nav")).split("<span>")
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
    
def blogs(html_url):
    page_url= requests.get(html_url)
    # page_url= requests.get(html_url)
    page_url_content=page_url.content
    page_soup=bs(page_url_content,'html.parser')
    blogs_writter=page_soup.find_all("a",{"class":"blog-listing__user-name"})
    blogs_header=page_soup.find_all("h2",{"class":"blog-listing__title"})
    blogs_contant=page_soup.find_all("div",{"class":"blog-listing__summary"})
    # print(blogs_writter)
    b_header_len=len(blogs_header)
    total_words_blog=0
    for n in range(b_header_len):
        logger.info(f"{n+1} {blogs_writter[n].getText()}")
        logger.info(f"{blogs_header[n].getText()}")
        logger.info(f"{blogs_contant[n].getText()}")
        total_words_blog= total_words_blog +len(str(blogs_contant[n].getText()).split(" "))
    logger.info(f"Total Words in blog : {total_words_blog}")
    logger.info(f"No of blogs : {b_header_len}")
    logger.info(f"Average words per blog: {total_words_blog/b_header_len}")
    


    # print(soup.prettify)

    # data= url.content
    # soup= bs(data,'html.parser')

def main():
    if len(sys.argv) <=2:
            ("you havent given enough info")
    else:
        function= sys.argv[1]
        if function == "get_url":
            if( len(sys.argv)<2):
                print(sys.argv[1])
            else:
                html_url= sys.argv[2]
                
                get_url(html_url)
                

if __name__ == '__main__':
    # # get_url('https://james-camerons-avatar.fandom.com/wiki/Blog:Recent_posts')
    # get_url('https://usbiomag.com/')
    
    # # Get_word_count()
    # get_list_pages()
    # blogs()
    main()

# https://usbiomag.com/