import scrape
from bs4 import BeautifulSoup
import pandas as pd

table = scrape.get_courses()

df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))



###soup = BeautifulSoup(html,'html.parser')
###courses = soup.find('tr').find_all('tr')
###
###for i in range(3):
###    print(courses[i])
###    print('----------')
###