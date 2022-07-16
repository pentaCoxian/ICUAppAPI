import scrape
import helper


datas = scrape.getSyllabus('2022',['22122'])[0]

res = []
for k,v in datas.items():
    t = [k]
    fs = ''.join(t)
    print(fs,end = ', ')


for k,v in datas.items():
    print(k)

regs = helper.getCourseInfo()
def getCourseList():
    resgs=[]
    for x in regs:
        resgs.append(x['rgno'])

print(resgs)