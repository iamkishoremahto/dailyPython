from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import worksheet

def get_url(*args):
    global url=args[0]
    return url

def soup():
    s = HTMLSession()
    content=s.get(get_url)
    soup= BeautifulSoup(content.text,'html.parser')
    print(soup)
    return soup

get_url('https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
soup()