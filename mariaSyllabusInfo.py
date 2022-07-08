import mariadb
import getSyllabusTags




def main():
    conn = mariadb.connect(
        user = "python",
        password = "pythonAccess56",
        host = "172.31.8.135",
        port = 3306,
        database = "syllabusdb"
    )
    testList = getSyllabusTags.getSyllabusTags(['21239'],'2022')
    c = conn.cursor()
    setup(c)

    # Insert test data
    for x in testList:
        keyList = x.keys()
        #keyList = keyList.pop(-1)

        valList = []
        for y in keyList:
            valList.append(x[y])
        keyStr = ', '.join(keyList)
        print(keyStr)
        #valList = ', '.join(valList)
        #sql = 'insert into courses(rgno, season, ay, course_no, old_cno, lang, section, title_e, title_j, schedule, room , comment, maxnum, instructor, unit, _id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?)', (
        #sql = ('insert into syllabus(regno, ay, id, term, cno, title_e, title_j, lang, instructor, unit_e, koma_lecture_e, koma_seminar_e, koma_labo_e, koma_act_e, koma_int_e, descreption, descreption_j, goals, goals_j, content, content_j, lang_of_inst, pollicy, individual_study, 0references, notes, schedule, url) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        sql = ('insert into syllabus(' + keyStr + ') values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        print(sql)
        c.execute(sql,valList)
        conn.commit()


    command = "select title_j from syllabus where match(descreption) against( '教育' IN BOOLEAN MODE );"
    c.execute(command)
    for (title_j) in c:
        print(f"Successfully retrieved {title_j}")

    # c.execute('insert into t1(num,name) values (?,?);',(4,'tasukete'))
    # conn.commit()

    # sql = 'select * from t1;'
    # c.execute(sql)
    # print('* cityテーブルの一覧を表示\n')
    # for row in c.fetchall():
    #     print('No:', row[0], 'Content:', row[1])
    # c.execute("drop table couses")
    c.close()

def setup(c):
    # ---debug, remake tables everytime---
    debug = "drop table if exists syllabus;"
    c.execute(debug)
    # ---To here---

    makeTable = "create table if not exists syllabus(regno VARCHAR(5), ay VARCHAR(4), term VARCHAR(20), cno VARCHAR(15), title_e VARCHAR(50), title_j NVARCHAR(100), lang NVARCHAR(30), instructor NVARCHAR(100), unit_e NVARCHAR(50), koma_lecture_e VARCHAR(10), koma_seminar_e VARCHAR(10), koma_labo_e VARCHAR(10), koma_act_e VARCHAR(10), koma_int_e VARCHAR(10), descreption NVARCHAR(1000), descreption_j NVARCHAR(2000), goals NVARCHAR(1000), goals_j NVARCHAR(500), content NVARCHAR(2000), content_j NVARCHAR(1000), lang_of_inst NVARCHAR(500), pollicy NVARCHAR(1000), individual_study NVARCHAR(500), nreferences NVARCHAR(1000), notes NVARCHAR(1000), schedule NVARCHAR(100), url NVARCHAR(300), id INT PRIMARY KEY) ENGINE=mroonga DEFAULT CHARSET=utf8mb4"
    c.execute(makeTable)
    makeIndex = "ALTER TABLE syllabus ADD FULLTEXT INDEX fulltextIndex(title_j) COMMENT 'tokenizer \"TokenMecab\"';"
    c.execute(makeIndex)
    makeIndex = "ALTER TABLE syllabus ADD FULLTEXT INDEX fulltextIndexDescription(descreption) COMMENT 'tokenizer \"TokenMecab\"';"
    c.execute(makeIndex)
#['regno', 'ay', 'id', 'term', 'cno', 'title_e', 'title_j', 'lang', 'instructor', 'unit_e', 'koma_lecture_e', 'koma_seminar_e', 'koma_labo_e', 'koma_act_e', 'koma_int_e', 'descreption', 'descreption_j', 'goals', 'goals_j', 'content', 'content_j', 'lang_of_inst', 'pollicy', 'individual_study', 'references', 'notes', 'schedule', 'url']
# ay
# term
# cno
# title_e
# title_j
# lang
# instructor
# unit_e
# koma_lecture_e
# koma_seminar_e
# koma_labo_e
# koma_act_e
# koma_int_e
# descreption
# descreption_j
# goals
# goals_j
# content
# content_j
# lang_of_inst
# pollicy
# individual_study
# references
# notes
# schedule
# url
    

main()