from bs4 import BeautifulSoup
import requests
from camelcase import CamelCase
import sys


def paragraph(*args):
    # self.Url=url
    # self.cname=cname
    
    Web_url= requests.get(args[0])
    company_name=args[1]
    data= Web_url.content
    soup= BeautifulSoup(data, 'html.parser')
    para= str(soup.find_all('a'))
    up_cname=args[1].upper()
    lo_cname=args[1].lower()
    camel_cname= CamelCase(args[1])
        #c_name=[up_cname,lo_cname,camel_cname]
        
        # print(para)
    no=(para.find(up_cname or lo_cname or camel_cname))
    # if up_cname or lo_cname or camel_cname  in para:
    if no>0:
        print(f"yes, your company is mention on this website {args[0]}")
    else:
        print(f"No, your company is not mention on this website{args[0]}")
    # print(para)

def main():
    if len(sys.argv) <=2:
            ("you havent given enough info")
    else:
        function= sys.argv[1]
        if function == "paragraph":
            if( len(sys.argv)<4):
                print(sys.argv[2])
            else:
                url= sys.argv[2]
                cname =sys.argv[3]
                paragraph(url,cname)
if __name__ == '__main__':
    main()
    

# if __name__ == "__main__":
#     url= input("Enter url")
#     cname= input("Enter Company Name : ")
#     paragraph(url,cname)
    