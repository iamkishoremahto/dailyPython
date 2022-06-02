

from matplotlib.pyplot import table
from numpy import append
from pysitemap import crawler
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import sys
import mysql.connector
from sqlalchemy import create_engine
password='Root@1234'
my_con = create_engine(f"mysql+pymysql://root:Root1234@localhost/website_report")


# mydb= mysql.connector.connect(
#     host= "localhost",
#     user= "root",
#     password= "Root@1234",
#     database='website_report'
# )

# mycursor= mydb.cursor()
# mycursor.execute("show databases;")
# for x in mycursor:
#     print(x)


def get_links(*args):
    # pass
    crawler(args[0], out_file='URL2.xml')

def get_word_count():
    path = 'C:\Windows\chromedriver.exe'
    driver = webdriver.Chrome(path)
    url_collection=[]
    with open('URL2.xml') as f:
        Url_soup= BeautifulSoup(f,'xml')
    url_list= Url_soup.find_all('loc')
    para_word_count=0
    para_word=[]
    sl_no=[]
    not_found_list=[]
    Not_found=0
    nsl_no=[]
    nsl=1
    slNO=1
    for i in range(len(url_list)):
        if "php" not in str(url_list[i].getText()) and "json" not in str(url_list[i].getText()) and "css" not in str(url_list[i].getText()) and "js" not in str(url_list[i].getText()):
            driver.get(url_list[i].getText())
            content = driver.page_source
            if "Page not found" in driver.title:
                not_found_list.append(url_list[i].getText())
                nsl_no.append(nsl)
                nsl= nsl+1
                Not_found= Not_found +1
            if "Page not found" not in driver.title:
                page_soup= BeautifulSoup(content,'html.parser')
                para= page_soup.find_all('p')
                for j in range(len(para)):
                    para_word_count=para_word_count + len(str(para[j].getText()).split(' ')) #count words on each paragraph
                para_word.append(para_word_count)
                
                url_collection.append(url_list[i].getText())
                
                sl_no.append(slNO)
               
                # sql= "INSERT INTO url_report (sl_no, url,no_of_words) VALUES (slNO,url_list[i].getText(),para_word_count)"
                # val=()
                
                
                
                slNO= slNO +1
                para_word_count=0
                url_dict= {'Sl No.':sl_no,'url':url_collection,'No of Words':para_word}
    # total_url=len(url_collection)
    # total_words= sum(para_word)
    # url_dict['Total Url']=(len(url_collection))
    # url_dict['Total Words']=(sum(para_word))
    notFoundDict={'Sl No.':nsl_no,'Not Found URL(404)':not_found_list}
    df= pd.DataFrame(url_dict)
    last_row=[' ','Total Url',len(url_list)]
    last_row2=[' ','Total Words',sum(para_word)]
    last_row3=[' ','Page Not Found',Not_found]
    # df['Total Url']=len(url_collection)
    # df['Total Words']=sum(para_word)
    tableName=url_list[0].getText()
    # df.rename(columns={'Sl No.':'sl_no','url':'url','No of Words':'no_of_words'}, inplace=True)
    df.to_sql(tableName,my_con,if_exists='append', index=False) 
    df.loc[-1]=last_row
    df.loc[-2]=last_row2
    df.loc[-3]=last_row3
    df.to_excel('Website_Url_Report2.xlsx', index=False)
    df2= pd.DataFrame(notFoundDict)
    
    df2.to_excel('Report_of_not_found_url.xlsx', index=False)
   
    print(df)

def main():
    if len(sys.argv)<=2:
        print("not a enogth information")
    else:
        function = sys.argv[1]
        if function == "get_links" :
            if (len(sys.argv)<3):
                print(sys.argv[1])
            else:
                url= sys.argv[2]
                get_links(url)
                get_word_count()
 
if __name__ == '__main__':
    get_links('https://en.wikipedia.org/wiki/Kishore_Kumar')
    get_word_count()
    # main()