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



def get_courses():
    try: 
        service = Service(ChromeDriverManager().install()) 
        driver = webdriver.Chrome(service=service, options=chrome_options)
        url = "https://campus.icu.ac.jp/icumap/ehb/SearchCO.aspx"

        # Open site (will be sent to SSO login)
        driver.get(url)
        driver.implicitly_wait(3)

        # Login to ICU SSO
        driver.find_element(By.ID,"username_input").send_keys(login_config.username)
        driver.find_element(By.ID,"password_input").send_keys(login_config.password)
        driver.find_element(By.ID,"login_button").click()
        driver.implicitly_wait(3)

        # Select show ALL results to get full course list
        select_element = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_ddlPageSize")
        select_object = Select(select_element)
        select_object.select_by_visible_text("ALL")
        driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_btn_search").click()
        driver.implicitly_wait(3)

        # Find course table
        tables = driver.find_elements(By.TAG_NAME,"table")
        course_table = tables[3].get_attribute('innerHTML')
        #print(course_table)
        return course_table
    except:
        traceback.print_exc()
    finally:
        driver.quit()


def getSyllabus(year,regno):
    try:
        service = Service(ChromeDriverManager().install()) 
        driver = webdriver.Chrome(service=service, options=chrome_options)

        ### --- maybe not needed for public access? --- 
        # Init SSO
        url = "https://campus.icu.ac.jp/icumap/ehb/SearchCO.aspx"
        # Open site (will be sent to SSO login)
        driver.get(url)
        driver.implicitly_wait(0.5)
        # Login to ICU SSO
        driver.find_element(By.ID,"username_input").send_keys(login_config.username)
        driver.find_element(By.ID,"password_input").send_keys(login_config.password)
        driver.find_element(By.ID,"login_button").click()
        driver.implicitly_wait(0.5)
        ### --- to here ---

        ### make regex filter
        # for content inside tag (devide text between text by <br> tag?)
        extractContent = re.compile('>[^<]+')
        # for extracting tag
        extractTag = re.compile('lbl_[^\"]+')

        resList = []

        for i in range(len(regno)):
            url = "https://campus.icu.ac.jp/public/ehandbook/PreviewSyllabus.aspx?year="+year+"&regno="+regno[i]+"&term="+regno[i][0]
            # Open site
            driver.get(url)
            driver.implicitly_wait(3)
            # Find course table (get page -> get main table -> find td with contents inside it -> )
            tables = driver.find_elements(By.TAG_NAME,"table")
            contentTable = BeautifulSoup(tables[4].get_attribute('innerHTML'),'lxml')
            rawText = contentTable.find_all('span')
            #regex and format
            resDict = {"regno":regno[i],}
            for j in range(len(rawText)):
                tag = extractTag.findall(str(rawText[j]))
                contentText = extractContent.findall(str(rawText[j])) #<- this is a python list?
                for k in range(len(contentText)):
                    contentText[k] = contentText[k].replace(">","").replace('\r\n', '').replace('\n', '')
                print(contentText)
                resDict[tag[0]]= contentText
                #print(tag[0] + ": ", contentText)
            resDictHash = hash(json.dumps(resDict))
            resDict['hash'] = resDictHash
            resList.append(resDict)
        #print(course_table)
        return resList
    except:
        traceback.print_exc()
    finally:
        driver.quit()

# Debug
#f = open("./log.txt","x")
#f.write(get_courses())
#f.close()
