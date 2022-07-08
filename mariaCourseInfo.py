import mariadb
import helper




def main():
    conn = mariadb.connect(
        user = "python",
        password = "pythonAccess56",
        host = "172.31.8.135",
        port = 3306,
        database = "syllabusdb"
    )
    testList = helper.getCourseInfo()
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
        #sql = 'insert into courses(rgno, season, ay, course_no, old_cno, lang, section, title_e, title_j, schedule, room , comment, maxnum, instructor, unit, _id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?)', (
        sql = ('insert into courses(' + keyStr + ') values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?)')
        c.execute(sql,valList)
        conn.commit()
    c.close()

# Initial setup for making tables and making fulltext indexes
def setup(con):
    c = con
    # debug, remake tables everytime
    debug = "drop table if exists courses;"
    c.execute(debug)

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