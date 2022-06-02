import scrape
from bs4 import BeautifulSoup
import json

raw = scrape.get_courses()
full = BeautifulSoup(raw,'lxml')
courses = full.find('tr').find_all('tr')


# Fill 0 for first 10 ids
def convertToTarget(num):
    if(num <10):
        res = str(num).zfill(2)
    else:
        res = str(num)
    return(res)


targetNumber= 2
labels = ["rgno","season","ay","course_no","old_cno","lang","section","title_e","title_j","schedule","room","comment","maxnum","instructor","unit"]

for i in range(len(courses)):
    # Set Course number
    targetString = convertToTarget(targetNumber)
    id = "ctl00_ContentPlaceHolder1_grv_course_ctl" + targetString + "_lbl_"
    resDict = {}
    for j in range(len(labels)):
        # Generate label
        tarID = id + labels[j]
        # Find element
        res = courses[i].find('span',{'id': tarID}).getText()
        #print(labels[j],": ",res)
        resDict[labels[j]] = res
    print(json.dumps(resDict))
    print("\n")
    targetNumber = targetNumber + 1





    