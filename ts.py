from email.parser import Parser
import string
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from lxml import objectify

from numpy import full

xmlfile="Links.xml"
# tree = ET.ParseError(xmlfile)
tree= ET.parse('Links.xml')
root= tree.getroot()
ET.dump(tree)
# print(root)



# with open("Links.xml") as fp:
#     soup = BeautifulSoup(fp, 'xml')

# link=(soup.find_all("loc"))
# print(link[0].getText())
    #mytree = e.parse("Links.xml")

# file_name = "Links.xml"
# full_path= os.path.abspath(os.path.join('data',file_name))
# tree= ElementTree.parse(full_path)

# root= tree.getroot()

# print(mytree)
    
