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

# This script is for getting data from the syllabus
# takes in a list of reg number in string format, along with the year

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
        # Regex
        extractTag = re.compile('lbl_[^\"]+')
        resList = []
        for i in range(len(regno)):
            url = "https://campus.icu.ac.jp/public/ehandbook/PreviewSyllabus.aspx?year="+year+"&regno="+regno[i]+"&term="+regno[i][0]
            # Open site
            driver.get(url)
            driver.implicitly_wait(3)
            # Find course table (get page -> get main table -> find span with contents inside it -> )
            form = driver.find_elements(By.TAG_NAME,"form")
            contentTable = BeautifulSoup(form[0].get_attribute('innerHTML'),'lxml')
            rawText = contentTable.find_all('span')

            syllabusDict = {'regno':regno[i]}
            for x in rawText:
                # Process Tag and content
                tag = extractTag.findall(str(x))
                tag = tag[0].replace('lbl_','')
                content = str(x).replace("<br/>",'\n')
                content = re.sub('<[^>]+>','',content)
                # Add to Dict
                syllabusDict.update({tag:content})
            syllabusDict['id'] = int(syllabusDict['regno'])
            syllabusDict['nreferences'] = syllabusDict['references']
            syllabusDict.pop('references')
            print(syllabusDict.keys())
            resList.append(syllabusDict)
                
        return resList
    except:
        traceback.print_exc()
    finally:
        driver.quit()

#testRegno = ['21239']
#print(getSyllabusTags(testRegno,'2022'))