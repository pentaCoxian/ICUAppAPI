import mariadb
import getSyllabusTags




def main():
    conn = mariadb.connect(
        user = "python",
        password = "pythonAccess56",
        host = "localhost",
        port = 3306,
        database = "syllabusdb"
    )
    testList = getSyllabusTags.getSyllabusTags(['21239'],'2022')
    c = conn.cursor()
    c.execute('drop table syllabus')
    setup(c)

    # Insert test data
    for x in testList:
        # Make tuple of keys so order does not change
        keyList = x.keys()
        #keyList = keyList.pop(-1)

        valList = []
        for y in keyList:
            valList.append(x[y])
        keyStr = ', '.join(keyList)
        mouwakaran = ['21239', '2022', 21239, 'Autumn Term', 'LED317', 'Language Assessment: Theory and Practice', '言語評価: 理論と実践', 'Language of Instruction: J', '渡部\u3000良典 (WATANABE, Yoshinori)\n\n', 'CREDIT （単位）: 3', '3', '', '', '', '', 'Testing plays a significant role in the lives of nearly every language student and teacher. This course investigates purposes and methods of classroom language tests and assesses standardized testing instruments (e.g. TOEFL). Students are taught how to design tests for different purposes and how to interpret and use test results.\n\n評価は言語学習・教育に重要な役割を持つ。教室内における言語テストの目的・方法を研究し，これまでに用いられている標準測定方法（TOEFLなど）を検討する。異なる目的のためのテストの作成方法，テスト結果の解釈と活用の仕方を学ぶ。\n\n', '本コースの教材等はMooldeで提供します。All the sessions will be conducted online by Zoom, and all the materials will be distributed by Moodle.\nコー寸目的を一言で表せば、assessment literacyを修得するということになります。\n詳細は以下の通りです。\n\nWith an emphasis on the foreign language context, the course is intended to provide students with a solid grounding in designing and implementing language test and assessment at school. Given this major goal, the purpose of this course is three-fold. First, it purports to provide students with a basic knowledge of the professional field exploring the issue of language testing and assessment. The topics to be covered range from the quality of good language assessment (i.e. reliability, validity, practicality, authenticity, and washback) to the conditions under which the best test use should be achieved, involving social and psychological factors. The second purpose is to help students to implement the knowledge about the principles of language testing and assessment to critically review a variety of tests that are used in various settings for various purposes. Such tests may include not only those tests that are developed and used in Japan (e.g. STEP EIKEN, senior high school entrance examinations, university entrance examinations, etc.), but those that are developed and used internationally (e.g. the TOEFL, IELTS, JLPT日本語能力試験、etc.). The third purpose is to help students develop a range of skills and techniques that are needed to develop their own tests for the sake of their students.\n\n\n教育指導で使われ実施されている言語テストの基本原理を習得します。テストは本当に能力を測っているのか、学校のテストの使い方はこのままでいいのか、外部テストは正しく使われているか、大学入試を変えると教育は変わるのか、読解力を測定するには、語彙力を測定するには、聴解力を測定するにはどうすればよいのか。Can-Doリストとは何か、CEFRとは何か、等々、テストや試験をめぐる様々な疑問を討論し、答えを見つけ出す機会となることを目的としています。テストを批判的に検討し、テスト設計（design）のための青写真を作成することを最終課題とします。\n\n\n\n', '言語テストを批判的に検討し、その意義を見直し、より建設的に使うための技能を身に付けます。\n\nCompletion of this course will enable students to: \n1) be familiar with the ways in which tests are assessed for validity and reliability;\n2) articulate current issues and research in language testing by referring to the theoretical bases that underline the testing of foreign languages;\n3) evaluate and develop foreign language tests, and refine them in group meetings.\n\n\n', '多くの言語能力テストが行われています。TOEFL, IELTS, TOEIC, JLPT（日本語能力試験）などの大規模テスト、さらに大学入学試験、入社試験などの人生を決める可能性のあるテスト、授業中に行われる小テスト等々。私たちは学習者としていつも受ける立場から見ることに慣れています。一方、得点が本当に能力を表しているのか、受験にあたって完全に公平性を保つことは可能なのかどうか、受験勉強は効果的なのか、等々いろいろな疑問を抱えながら受験することが多いのではないでしょうか。言語テスト（Language Testing）は一つの学術分野として多くの成果を上げていますが、ほとんどは専門性が高く、せっかくの成果が受験者としての素朴な疑問に答えるような形になっていないのが実情です。本コースでは専門的な研究成果をわかりやすく伝え、その上で現在行われているテストを批判的に検討してみたいと考えています。将来教員を目指している方々はもちろんですが、テストと教育に関心のある方にも資するところがあるはずです。\n\n\n', '1. Introduction: The role of evaluation, assessment, and testing in foreign language teaching\n1) Understand the basic terms and the principles of language assessment.\n2) Discuss to understand the role of language assessment in foreign language teaching.\n3) Examine sample test papers.\n\n2. Understanding the purpose of language assessment\n1) Purposes (e.g., diagnostic, screening, placement, program evaluation, etc.)\n2) Timing (formative, summative, etc.)\n\n3. Principles of language assessment 1: Reliability\n1) Test reliability: Examining the quality of the test\n2) Rater reliability: Assessing students’ essays\n\n4. Principles of language assessment 2: Validity\n1) Construct validity: Relationships between theory of language and test scores \n2) Content validity: Does the test score tell us what the learner has learned? \n\n5. Principles of language assessment 3:\n1) Consequences: Does the test bring about the intended effect? \n2) Practicality: Feasibility and usefulness of the test\n\n6. Alternatives in assessment\n1) Performance assessment\n2) Dynamic testing\n3) Portfolio assessment\n\n7. Using test scores\n1) Giving a final grade\n2) Gaining diagnostic information\n3) Evaluating curriculum\n\n8. Social issues of language assessment\n1) Fairness\n2) Code of ethics\n\n9. The role of language assessment in Japanese educational policy \n1) CAN-DO statements \n2) Plurilingualism and Common European Framework of Reference (CEFR)\n3) University admission policies \n\n10. And bring them all together\n1) LEARNING-ORIENTED LANGUAGE ASSESSMENT  \n2) REVERSE ENGINEERING &amp; TEST SPECIFICATIONS \n3) ASSESSMENT LITERACY \n\n\n', '\n\n', 'Lecture: Japanese &amp; English 日本語および英語\nReadings/Materials:English 英語\nTests/Quizzes/Assignments: English or Japanese\u3000英語あるいは日本語\nDiscussions/Presentations/Other learning activities: Japanese &amp; English 日本語および英語\n----\nCommunication with the instructor:日本語あるいは英語 Japanese or English \n\n', '1. Presentation and discussion \t25%\nIn class, students will be asked to review and comment on the range of test tasks that are taken from existent assessments (e.g., the TOEFL, the Center Test, etc.).  \n授業中、テストや教育評価に関する意見を述べ、持ち寄ったテストについて批判的に検討する。\n2. Reflective journal 30%\nSubmission of a reflective journal for each class.\n毎回の授業のコメントを提出。\n3. Final project 45%\nAs a final project, the student will be asked to produce a blueprint or a test-specification about a test of his or her own choice. \nこれまでに受けたことのあるテスト、作成したことのあるテストを批判的に検討し、よりよりテスト作成のための設計図（テスト細目Test specifications）を作成して提出する。\n\n', '210 minutes per week.\n\n', 'Reference works\nBrown, H. D. &amp; Abeywickrama, P. (2010) Language assessment: Principles and classroom practices, second edition. New York: Pearson Longman. （この本を参考にしながら進めますが必ずしも購入する必要はありません）\nAlderson, J. C., Clapham, C. &amp; Wall, D. (1995). Language test construction and evaluation. Cambridge: Cambridge University Press. 渡部良典（編訳）『言語テストの作成と評価』（春風社）.\nBrown, J. D. (2005). Testing in language programs: A comprehensive guide to English language assessment. New York: McGraw-Hill.\nHughes, A. (2002). Testing for language teachers, second edition. Cambridge: Cambridge University Press. 靜哲人（訳）『英語のテストはこう作る』（研究社）.\n\n\n', 'The class will be conducted on the basis of the interaction between the teacher and students and between the students. \n\n', '5/F,6/F,7/F\n\n', '\n\n'] 
        
        #valList = ', '.join(valList)
        #sql = 'insert into courses(rgno, season, ay, course_no, old_cno, lang, section, title_e, title_j, schedule, room , comment, maxnum, instructor, unit, _id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?, ?)', (
        sql = ('insert into syllabus(regno, ay, id, term, cno, title_e, title_j, lang, instructor, unit_e, koma_lecture_e, koma_seminar_e, koma_labo_e, koma_act_e, koma_int_e, descreption, descreption_j, goals, goals_j, content, content_j, lang_of_inst, pollicy, individual_study, 0references, notes, schedule, url) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
        print(sql)
        c.execute(sql,mouwakaran)
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

def setup(con):
    c = con
    
    makeTable = "create table syllabus(regno VARCHAR(5), ay VARCHAR(4), term VARCHAR(20), cno VARCHAR(15), title_e VARCHAR(50), title_j NVARCHAR(100), lang NVARCHAR(30), instructor NVARCHAR(100), unit_e NVARCHAR(50), koma_lecture_e VARCHAR(10), koma_seminar_e VARCHAR(10), koma_labo_e VARCHAR(10), koma_act_e VARCHAR(10), koma_int_e VARCHAR(10), descreption NVARCHAR(1000), descreption_j NVARCHAR(2000), goals NVARCHAR(1000), goals_j NVARCHAR(500), content NVARCHAR(2000), content_j NVARCHAR(1000), lang_of_inst NVARCHAR(500), pollicy NVARCHAR(1000), individual_study NVARCHAR(500), 0references NVARCHAR(1000), notes NVARCHAR(1000), schedule NVARCHAR(100), url NVARCHAR(300), id INT PRIMARY KEY) ENGINE=mroonga DEFAULT CHARSET=utf8mb4"
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