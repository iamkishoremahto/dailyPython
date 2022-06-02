from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.keys import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
from bs4 import BeautifulSoup



path= "C:\Windows\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.crunchbase.com/organization/vmoksha-technologies")
content=(driver.page_source)
soup = BeautifulSoup(content,'html.parser')
vm= soup.find_all('p')
for para in vm:
    print(para.getText())
# print(vm)

# try:
#     main = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.tag, "body")))
#     paragraph =  main.find_element_by_tag_name("p")
#     print(paragraph.text)
# finally:
#     driver.quit()
        

driver.quit()