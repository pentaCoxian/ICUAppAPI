import scrape
from bs4 import BeautifulSoup

table = scrape.get_courses()

soup = BeautifulSoup(table,'lxml')
courses = soup.find('tr').find_all('tr')

offset = 2
targetNumber= 0
targetNumber = str(targetNumber).zfill(2)
#print(courses[i])

print('----------')
id = "ctl00_ContentPlaceHolder1_grv_course_ctl"+targetNumber+"_lbl_rgno"
print(id)
print(courses[i].find('span',{'id': id}))
#print('----------')
#id = 'ctl00_ContentPlaceHolder1_grv_course_ctl02_lbl_rgno'
#print(id)
#print(courses[i].find('span',{'id': id}))