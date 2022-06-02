from stat import filemode
from pysitemap import crawler
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys
import logging
import logging.config

# Logger configuration 
logger = logging.getLogger(__name__)  #assigning name for the logger
logger.setLevel(logging.INFO)   #set level of the logging
f= logging.Formatter('%(asctime)s - %(message)s') # set output formate
fh = logging.FileHandler('Words_in_Each_Url.log') # set logging handler file for records the logging output
fh.setFormatter(f)  # set format
logger.addHandler(fh) #assign file hendler to the logger

#get the url input from the user 

def get_Links(*arg):
    root_url= arg[0]
    crawler(root_url,out_file='sitemap.xml')
# get the number of word on each pages and total words

def get_word_count():
    with open("sitemap.xml") as f:
        soup_sitemap= soup(f,'xml')
    links= soup_sitemap.find_all("loc")
    

    #declear variable

    total_pages=0               
    total_words_per_page=0
    total_words=0
    
    for i in range(len(links)):

        url2= links[i].getText()
        total_pages = total_pages+1
        uClient= uReq(url2)
        page_Html= uClient.read()
        uClient.close()

        page_soup= soup(page_Html, 'html.parser')
        para=(page_soup.find_all('p'))
        for j in range(len(para)):
            parag=(str((para[j].getText()))).split(" ")
            total_words_per_page= total_words_per_page +(len(parag))
        total_words= total_words + total_words_per_page    
        logger.info(f"{url2}  Total words in this page is {total_words_per_page}")
        total_words_per_page=0
    
    logger.info(f"Total words : {total_words}")
    logger.info(f"Total pages : {total_pages}")
    logger.info(f"Average Words per page : {total_words/total_pages}")
    
       


    

def main():
    if len(sys.argv) <=2:
            ("you havent given enough info")
    else:
        function= sys.argv[1]
        if function == "get_Links":
            if( len(sys.argv)<2):
                print(sys.argv[1])
            else:
                root_url= sys.argv[2]
                
                get_Links(root_url)
                get_word_count()
if __name__ == '__main__':
    # links('https://en.wikipedia.org/wiki/Salman_Khan')
    # word_count()
    main()
    # get_Links('https://en.wikipedia.org/wiki/Salman_Khan')
    # get_word_count()