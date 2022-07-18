import MeCab as mb
import os
import scrape
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy.dialects.mysql import match
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import time
#import scrape
load_dotenv()
engine = sa.create_engine(os.environ['MARIADB_ADDRESS'],echo=False)
Base = declarative_base()

def makeKey(msg):
    print('INPUT: ',msg)
    tagger = mb.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')#sudo find / | grep mecab-ipadic-neologd
    rs = tagger.parseToNode(msg)    
    r = set()
    while rs:
        hold = rs.feature.split(',')
        type = hold[0]
        subtype = hold[1]
        dia1 = hold[6]
        word = rs.surface
        #print(word,rs.feature)
        if type == '名詞':
            #print(word,type,subtype,dia1)
            r.add(word)
        rs = rs.next
    t=' +'.join(r)
    print('TAGS: ',t)
    return t
# print('size difference:',len(msg),'->',len(comp(rs)))
# print("--- %s seconds ---" % (time.time() - start))


class Course(Base):
    __tablename__ ="syllabuses"
    __table_args__ = {
        'mariadb_ENGINE': 'mroonga',
        'mariadb_DEFAULT_CHARSET': 'utf8mb4'
    }
    regno = sa.Column(sa.Integer, primary_key=True)
    ay = sa.Column(sa.String(length=5))
    term = sa.Column(sa.String(length=100))
    cno = sa.Column(sa.String(length=100))
    title_e = sa.Column(sa.String(length=300))
    title_j = sa.Column(sa.String(length=300))
    lang = sa.Column(sa.String(length=300))
    instructor = sa.Column(sa.String(length=100))
    unit_e = sa.Column(sa.String(length=100))
    koma_lecture_e = sa.Column(sa.String(length=10))
    koma_seminar_e = sa.Column(sa.String(length=10))
    koma_labo_e = sa.Column(sa.String(length=10))
    koma_act_e = sa.Column(sa.String(length=10))
    koma_int_e = sa.Column(sa.String(length=10))
    descreption = sa.Column(sa.Text)
    descreption_j = sa.Column(sa.Text)
    goals = sa.Column(sa.Text)
    goals_j = sa.Column(sa.Text)
    content = sa.Column(sa.Text)
    content_j = sa.Column(sa.Text)
    lang_of_inst = sa.Column(sa.Text)
    pollicy = sa.Column(sa.Text)
    individual_study = sa.Column(sa.Text)
    ref = sa.Column(sa.Text)
    notes = sa.Column(sa.Text)
    schedule = sa.Column(sa.String(length=500))
    url = sa.Column(sa.String(length=300))

Base.metadata.create_all(engine)
Session = sa.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def MakeIndex(engine, tablename, indexname, cols): 
    cols = ','.join(cols)
    with engine.connect() as con:
        con.execute("""ALTER TABLE """ + tablename + """ ADD FULLTEXT INDEX IF NOT EXISTS """ + indexname +  """fulltextIndex2(""" + cols + """) COMMENT 'tokenizer "TokenMecab"';""")


MakeIndex(engine,'syllabuses','fulltextindex1',['content_j'])
MakeIndex(engine,'syllabuses','fulltextindex2',['lang_of_inst'])
MakeIndex(engine,'syllabuses','fulltextindex7',['schedule'])
MakeIndex(engine,'syllabuses','fulltextindex5',['cno','schedule'])
MakeIndex(engine,'syllabuses','fulltextindex3',['content','content_j'])
MakeIndex(engine,'syllabuses','fulltextindex4',['descreption','descreption_j'])
MakeIndex(engine,'syllabuses','fulltextindex6',['ay', 'term', 'cno', 'title_e', 'title_j', 'lang', 'instructor', 'unit_e', 'koma_lecture_e', 'koma_seminar_e', 'koma_labo_e', 'koma_act_e', 'koma_int_e', 'descreption', 'descreption_j', 'goals', 'goals_j', 'content', 'content_j', 'lang_of_inst', 'pollicy', 'individual_study', 'ref', 'notes', 'schedule', 'url'])



#start=time.time()
## courses = session.query(Course).all()
## for course in courses:
##     print(" - " + course.title_j + ' ' + course.title_e)
#pron=' +ISC +5 +6 +7'
#vars='ay, term, cno, title_e, title_j, lang, instructor, unit_e, koma_lecture_e, koma_seminar_e, koma_labo_e, koma_act_e, koma_int_e, descreption, descreption_j, goals, goals_j, content, content_j, lang_of_inst, pollicy, individual_study, ref, notes, schedule, url'
#sql = """select * from syllabuses where match("""+vars+""") against('"""+pron+"""' in boolean mode);"""
#res = session.execute(sql)
#print('SEARCH:',pron)
#for v in res:
#   print(v.cno,' : ',v.title_j, v.schedule.strip('\n'))
#print("--- %s seconds ---" % (time.time() - start))


def searchFullText(args,feild='ay, term, cno, title_e, title_j, lang, instructor, unit_e, koma_lecture_e, koma_seminar_e, koma_labo_e, koma_act_e, koma_int_e, descreption, descreption_j, goals, goals_j, content, content_j, lang_of_inst, pollicy, individual_study, ref, notes, schedule, url'):

    args = makeKey('+'+args.replace(' ',' +'))
    print('=======START=======')
    sql = """select * from syllabuses where match("""+feild+""") 
    against('"""+args+"""' in boolean mode) LIMIT 10;"""
    print('SEARCH:',makeKey(args))
    res = session.execute(sql)
    
    dictLis = []
    for row in res:
        #print(row.cno,' : ',row.title_j, row.schedule.strip('\n'))
        row_as_dict = row._asdict()
        dictLis.append(row_as_dict)
    return dictLis


