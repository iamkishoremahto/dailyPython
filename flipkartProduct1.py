from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import worksheet
import sys

def Flipkart_Electronic_Product_Details(*args):
    s= HTMLSession()

    url= args[0]
    content= s.get(url)
    soup= BeautifulSoup(content.text, 'html.parser')
    all_pages=(soup.find_all("a",{"class":"ge-49M"}))
    pagesLinks=[]
    Model=[]
    specification=[]
    Rating=[]
    Price=[]
    sl_no=[]
    sl=0
    page=(soup.find("div",{"class":"_2MImiq"}))
    page_range=(int(str(page.getText()).split(" ")[3].split("N")[0]))
    # url2=('https://www.flipkart.com'+ (all_pages[0]['href']))
    # print(url2)
    # content2=s.get(url2)
    # page_soup= BeautifulSoup(content2.text,'html.parser')

    # print(page_soup.find_all("div",{"class":"_4rR01T"}))
    for i in range(page_range):

        # pagesLinks.append('https://www.flipkart.com/'+all_pages[i]['href'])
        # url2=('https://www.flipkart.com'+ (all_pages[i]['href']))
        url2=(url.replace("off",str(i)))
        content2=s.get(url2)
        page_soup= BeautifulSoup(content2.text,'html.parser')
        model=(page_soup.find_all("div",{"class":"_4rR01T"}))
        specifi=(page_soup.find_all("ul",{"class":"_1xgFaf"}))
        rating=(page_soup.find_all("span",{"class":"_2_R_DZ"}))
        price=(page_soup.find_all("div",{"class":"_30jeq3 _1_WHN1"}))
        if len(model)<=0:
            break
        else:

            for j in range(len(model)):
                Model.append(model[j].getText())
                specification.append(specifi[j].getText())
                Price.append(price[j].getText())
                sl_no.append(sl+1)
                sl=sl+1
            
            # Rating.append(rating[j].getText())

    product_details={"Sl NO":sl_no,"Product Model":Model,"Specification":specification,"Price":Price}
    df= pd.DataFrame(product_details)
    df.to_excel("Product Datails in flipkart.xlsx", index=False)
    print(df)
    # print(all_pages)
def main():
    if len(sys.argv)<=2:
        print("not a enogth information")
    else:
        function = sys.argv[1]
        if function == "Flipkart_Electronic_Product_Details" :
            if (len(sys.argv)<3):
                print(sys.argv[1])
            else:
                url= sys.argv[2]
                
                Flipkart_Electronic_Product_Details(url)
if __name__ == '__main__':
    Flipkart_Electronic_Product_Details('https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

