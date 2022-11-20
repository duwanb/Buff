from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#for mac
#chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
chrome_path = r'./chromedriver' #path from 'which chromedriver'

options = ChromeOptions()
options.add_extension('./Buff-Utility.crx')
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver = webdriver.Chrome(executable_path=chrome_path, options=options) 
# url of google news website
url = 'https://buff.163.com/market/csgo#tab=selling&page_num=1'


listanome=[]
listapreco=[]
listacompleta=[]


# to open the url in the browser
driver.get(url)  
items = driver.find_elements(By.CLASS_NAME, "market-card")

for a in items:
    filter = a.find_elements(By.TAG_NAME, "li")
    for b in filter:
        nomes = a.find_elements(By.TAG_NAME, "h3")
        precos = a.find_elements(By.TAG_NAME, "strong")
        #precos = a.find_elements(By.CSS_SELECTOR, "grid-column")
        #<span style="color: #eea20e;font-weight: 700;"
for a in nomes:
    listanome.append(a.text)

for a in precos:
    listapreco.append(a.text)

len = len(listanome)
aux = 0

while(aux < len):
    str = (listanome[aux]+ ";" + listapreco[aux])
    listacompleta.append(str)
    aux = aux+ 1

print("\n\n\n\n\n")
for a in listacompleta:
    print(a)


driver.quit()