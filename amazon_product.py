from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
import requests
from openpyxl import workbook
from selenium import webdriver
import pandas as pd

def get_url(*arg):
    # url= requests.get(arg[0])
    path= 'C:\Windows\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(arg[0])
    content= driver.page_source
    driver.quit()
    # content=url.content
    soup= BeautifulSoup(content, 'html')
    Model= soup.find_all("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
    
    price= soup.find_all("span",{"class":"a-price-whole"})
    
    # file = open("Amazon_Laptop_list.csv","wb")
    # writer = csv.writer(file)

    # writer.writerows('Product Name','Price')
    modelList=[]
    priceList=[]
    for i in range(len(Model)):
    
        modelList.append(Model[i].getText())
        priceList.append(price[i].getText())
    Product_Dict= {"Product Name And Specification":modelList,"Price":priceList}
    df= pd.DataFrame(Product_Dict)
    df.to_excel("Laptop_list in amazon.xlsx")
    print(df)


if __name__ == '__main__':
    get_url('https://www.amazon.in/s?k=laptop&crid=1RICPC7DH9O1N&sprefix=laptop%2Caps%2C274&ref=nb_sb_noss_1')