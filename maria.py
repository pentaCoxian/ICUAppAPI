import mariadb
import yakeluso




def main():
    conn = mariadb.connect(
        user = "python",
        password = "pythonAccess56",
        host = "localhost",
        port = 3306,
        database = "syllabusdb"
    )
    testList = yakeluso.getCourseInfo()
    c = conn.cursor()

    setup(c)

        

    # Insert test data
    for x in testList:
        # Make tuple of keys so order does not change
        keyList = x.keys()
        #keyList = keyList.pop(-1)
        print(keyList)
        valList = []
        for y in keyList:
            valList.append(x[y])
        keyStr = ', '.join(keyList)
        #valList = ', '.join(valList)
        #sql = 'insert into courses(rgno, season, ay, course_no, old_cno, lang, section, title_e, title_j, schedule, room , comment, maxnum, instructor, unit, _id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?)', (
        sql = ('insert into courses(' + keyStr + ') values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?)')
        c.execute(sql,valList)

        conn.commit()


    # c.execute('insert into t1(num,name) values (?,?);',(4,'tasukete'))
    # conn.commit()

    # sql = 'select * from t1;'
    # c.execute(sql)
    # print('* cityテーブルの一覧を表示\n')
    # for row in c.fetchall():
    #     print('No:', row[0], 'Content:', row[1])
    # c.execute("drop table couses")
    c.close()

def setup(con):
    c = con
    makeTable = "create table courses(rgno VARCHAR(10), season VARCHAR(10), ay VARCHAR(4), course_no VARCHAR(10), old_cno VARCHAR(10), lang VARCHAR(5), section VARCHAR(30), title_e NVARCHAR(300), title_j NVARCHAR(600), schedule VARCHAR(150), room NVARCHAR(100), comment NVARCHAR(600), maxnum VARCHAR(100), instructor NVARCHAR(200), unit VARCHAR(10), id INT PRIMARY KEY) ENGINE=mroonga DEFAULT CHARSET=utf8mb4"
    c.execute(makeTable)
    makeIndex = "ALTER TABLE courses ADD FULLTEXT INDEX fulltextIndex(title_j) COMMENT 'tokenizer \"TokenMecab\"';"
    c.execute(makeIndex)

    
# {'rgno': '31249', 
# 'season': 'Winter',
# 'ay': '2022',
# 'course_no': 'MCC107',
# 'old_cno': '',
# 'lang': 'E',
# 'section': '',
# 'title_e': 'Introduction to Interpreting ',
# 'title_j': '通訳入門',
# 'schedule': '5/TH,6/TH,7/TH',
# 'room': '',
# 'comment': '',
# 'maxnum': '(180)',
# 'instructor': 'TAMURA, Tomoko',
# 'unit': '3',
# '_id': 31249}
    

main()