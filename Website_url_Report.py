
from pysitemap import crawler
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd



def get_links(*args):
    crawler(args[0], out_file='URL.xml')

def get_word_count():
    path = 'C:\Windows\chromedriver.exe'
    driver = webdriver.Chrome(path)
    url_collection=[]
    with open('URL.xml') as f:
        Url_soup= BeautifulSoup(f,'xml')
    url_list= Url_soup.find_all('loc')
    para_word_count=0
    para_word=[]
    sl_no=[]
    for i in range(len(url_list)):
        driver.get(url_list[i].getText())
        content = driver.page_source
        page_soup= BeautifulSoup(content,'html.parser')
        para= page_soup.find_all('p')
        for j in range(len(para)):
            para_word_count=para_word_count + len(str(para[j].getText()).split(' '))
        para_word.append(para_word_count)
        para_word_count=0
        url_collection.append(url_list[i].getText())
        sl_no.append(i+1)
        
        url_dict= {'Sl No.':sl_no,'url':url_collection,'No of Words':para_word}
    # total_url=len(url_collection)
    # total_words= sum(para_word)
    # url_dict['Total Url']=(len(url_collection))
    # url_dict['Total Words']=(sum(para_word))
    df= pd.DataFrame(url_dict)
    last_row=[' ','Total Url',len(url_collection)]
    last_row2=[' ','Total Words',sum(para_word)]
    # df['Total Url']=len(url_collection)
    # df['Total Words']=sum(para_word)
    df.loc[-1]=last_row
    df.loc[-2]=last_row2
    df.to_excel('Website_Url_Report.xlsx', index=False)
    print(df)
 
if __name__ == '__main__':
    get_links('https://usbiomag.com/')
    get_word_count()