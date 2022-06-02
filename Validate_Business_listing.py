
from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup

import logging
import logging.config
import sys

#logger configuration
#File Handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
f = logging.Formatter('%(asctime)s - %(message)s')
fh= logging.FileHandler('Validate_Business_listing.log')
fh.setFormatter(f)
logger.addHandler(fh)
#Console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(f)
logger.addHandler(ch)






def get_url(*args):
    path = 'C:\Windows\chromedriver.exe'
    driver = webdriver.Chrome(path)
    url= args[0]
    driver.get(url)
    company_name= args[1]
    Upper_case= company_name.upper()
    Lower_case= company_name.lower()
    url_title=(driver.title)
    count=0
    if company_name in url_title:
        count=count+1
    elif Upper_case in url_title:
        count= count+1
    elif Lower_case in url_title:
        count= count+1
    
    # print(Upper_case , Lower_case)
    content = driver.page_source
    driver.quit()
    # print(content)
    soup = BeautifulSoup(content,'html.parser')
    all_paragraph= soup.find_all("p")
    for i in range(len(all_paragraph)):
        paragraph= str(all_paragraph[i])
        # print(paragraph)
        if paragraph.find(company_name)>=0 or paragraph.find(Upper_case)>=0 or paragraph.find(Lower_case)>=0:
            count= count+1
        
    if count>0:
        logger.info(f"Yes {company_name} is present on this url {args[0]}")
    else:
        logger.info(f"No, {company_name} is not present on this url {args[0]}")
    # print(url_title)
    # print(all_paragraph)
    
def main():
    if len(sys.argv)<=2:
        print("not a enogth information")
    else:
        function = sys.argv[1]
        if function == "get_url" :
            if (len(sys.argv)<4):
                print(sys.argv[1])
            else:
                url= sys.argv[2]
                cname= sys.argv[3]
                get_url(url,cname)
    
if __name__ == '__main__':
    main()
    
# get_url('https://www.ambitionbox.com/overview/vmoksha-technologies-overview','Vmoksha Technologies')