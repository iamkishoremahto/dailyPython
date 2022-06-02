
from stat import filemode
from bs4 import BeautifulSoup as bs
import requests
import logging
import logging.config
from pysitemap import crawler
import sys



# Logger configuration 
logger = logging.getLogger(__name__)  #assigning name for the logger
logger.setLevel(logging.INFO)   #set level of the logging
f= logging.Formatter('%(asctime)s - %(message)s') # set output formate
fh = logging.FileHandler('paragraph.log')
 # set logging handler file for records the logging output

fh.setFormatter(f)  # set format
logger.addHandler(fh) #assign file hendler to the logger


def get_url(*args):
    html_url=args[0]
    # crawler(html_url,out_file='paragraph.xml')
    get_paragraph(html_url)
def get_paragraph(cUrl):
    url=requests.get(cUrl)
    url_content= url.content
    html_soup= bs(url_content, 'html.parser')
    all_paragraph= html_soup.find_all("p")
    # print(len(all_paragraph))
    for i in range(len(all_paragraph)):
        para= all_paragraph[i].getText()
        logger.info(f"{para}")

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
    # get_url('https://james-camerons-avatar.fandom.com/wiki/Blog:Recent_posts')
    main()
    

