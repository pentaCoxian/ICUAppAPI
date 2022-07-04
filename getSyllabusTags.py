import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import re


import login_config #import credentials


# Chrome settings
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito") #don't want cache
chrome_options.add_argument("--headless")

def getSyllabusTags(regno,year):
    try:
        service = Service(ChromeDriverManager().install()) 
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
        extractContent = re.compile('>[^<]+')
        extractTag = re.compile('lbl_[^\"]+')

        resList = []
        for i in range(len(regno)):
            url = "https://campus.icu.ac.jp/public/ehandbook/PreviewSyllabus.aspx?year="+year+"&regno="+regno[i]+"&term="+regno[i][0]
            # Open site
            driver.get(url)
            driver.implicitly_wait(3)
            # Find course table (get page -> get main table -> find td with contents inside it -> )
            form = driver.find_elements(By.TAG_NAME,"form")
            
            contentTable = BeautifulSoup(form[0].get_attribute('innerHTML'),'lxml')
            rawText = contentTable.find_all('span')

            for x in rawText:
                tag = extractTag.findall(str(x))
                for y in tag:
                    print(y.replace('lbl_',''))
                print(str(x).replace("<br/>",'\n'))

                


            #regex and format
            #resDict = {"regno":regno[i],}
            #for j in range(len(rawText)):
            #    tag = extractTag.findall(str(rawText[j]))
            #    for x in tag:
           #         x.
           #     print(tag)
                #contentText = extractContent.findall(str(rawText[j])) #<- this is a python list?
                #for k in range(len(contentText)):
                #    contentText[k] = contentText[k].replace(">","").replace('\r\n', '').replace('\n', '')
                #print(contentText)
                #resDict[tag[0]]= contentText
                #print(tag[0] + ": ", contentText)
            #resDictHash = hash(json.dumps(resDict))
            #resDict['hash'] = resDictHash
            #resList.append(resDict)
        #print(course_table)
        return resList
    except:
        traceback.print_exc()
    finally:
        driver.quit()

testRegno = ['21239']
print(getSyllabusTags(testRegno,'2022'))