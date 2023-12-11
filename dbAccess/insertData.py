import os
import scrape
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy import update, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import bindparam
from dotenv import load_dotenv
import time
from tqdm import tqdm
import helper
# Load env variables
load_dotenv()
engine = sa.create_engine(os.environ['MARIADB_ADDRESS'],echo=True)
Base = declarative_base()

class Classrooms(Base):
    __tablename__ = "classrooms"
    room = sa.Column(sa.String(length=10), primary_key=True)
    m1 = sa.Column(sa.Boolean,default = True)
    m2 = sa.Column(sa.Boolean,default = True)
    m3 = sa.Column(sa.Boolean,default = True)
    m4 = sa.Column(sa.Boolean,default = True)
    ml4 = sa.Column(sa.Boolean,default = True)
    m5 = sa.Column(sa.Boolean,default = True)
    m6 = sa.Column(sa.Boolean,default = True)
    m7 = sa.Column(sa.Boolean,default = True)
    m8 = sa.Column(sa.Boolean,default = True)
    tu1 = sa.Column(sa.Boolean,default = True)
    tu2 = sa.Column(sa.Boolean,default = True)
    tu3 = sa.Column(sa.Boolean,default = True)
    tu4 = sa.Column(sa.Boolean,default = True)
    tul4 = sa.Column(sa.Boolean,default = True)
    tu5 = sa.Column(sa.Boolean,default = True)
    tu6 = sa.Column(sa.Boolean,default = True)
    tu7 = sa.Column(sa.Boolean,default = True)
    tu8 = sa.Column(sa.Boolean,default = True)
    w1 = sa.Column(sa.Boolean,default = True)
    w2 = sa.Column(sa.Boolean,default = True)
    w3 = sa.Column(sa.Boolean,default = True)
    w4 = sa.Column(sa.Boolean,default = True)
    wl4 = sa.Column(sa.Boolean,default = True)
    w5 = sa.Column(sa.Boolean,default = True)
    w6 = sa.Column(sa.Boolean,default = True)
    w7 = sa.Column(sa.Boolean,default = True)
    w8 = sa.Column(sa.Boolean,default = True)
    th1 = sa.Column(sa.Boolean,default = True)
    th2 = sa.Column(sa.Boolean,default = True)
    th3 = sa.Column(sa.Boolean,default = True)
    th4 = sa.Column(sa.Boolean,default = True)
    thl4 = sa.Column(sa.Boolean,default = True)
    th5 = sa.Column(sa.Boolean,default = True)
    th6 = sa.Column(sa.Boolean,default = True)
    th7 = sa.Column(sa.Boolean,default = True)
    th8 = sa.Column(sa.Boolean,default = True)
    f1 = sa.Column(sa.Boolean,default = True)
    f2 = sa.Column(sa.Boolean,default = True)
    f3 = sa.Column(sa.Boolean,default = True)
    f4 = sa.Column(sa.Boolean,default = True)
    fl4 = sa.Column(sa.Boolean,default = True)
    f5 = sa.Column(sa.Boolean,default = True)
    f6 = sa.Column(sa.Boolean,default = True)
    f7 = sa.Column(sa.Boolean,default = True)
    f8 = sa.Column(sa.Boolean,default = True)
    sa1 = sa.Column(sa.Boolean,default = True)
    sa2 = sa.Column(sa.Boolean,default = True)
    sa3 = sa.Column(sa.Boolean,default = True)
    sa4 = sa.Column(sa.Boolean,default = True)
    sal4 = sa.Column(sa.Boolean,default = True)
    sa5 = sa.Column(sa.Boolean,default = True)
    sa6 = sa.Column(sa.Boolean,default = True)
    sa7 = sa.Column(sa.Boolean,default = True)
    sa8 = sa.Column(sa.Boolean,default = True)

# class Course(Base):
#     __tablename__ ="syllabuses"
#     __table_args__ = {
#         'mariadb_ENGINE': 'mroonga',
#         'mariadb_DEFAULT_CHARSET': 'utf8mb4'
#     }
#     regno = sa.Column(sa.Integer, primary_key=True)
#     ay = sa.Column(sa.String(length=5))
#     term = sa.Column(sa.String(length=100))
#     cno = sa.Column(sa.String(length=100))
#     title_e = sa.Column(sa.String(length=300))
#     title_j = sa.Column(sa.String(length=300))
#     lang = sa.Column(sa.String(length=300))
#     instructor = sa.Column(sa.String(length=100))
#     unit_e = sa.Column(sa.String(length=100))
#     koma_lecture_e = sa.Column(sa.String(length=10))
#     koma_seminar_e = sa.Column(sa.String(length=10))
#     koma_labo_e = sa.Column(sa.String(length=10))
#     koma_act_e = sa.Column(sa.String(length=10))
#     koma_int_e = sa.Column(sa.String(length=10))
#     descreption = sa.Column(sa.Text)
#     descreption_j = sa.Column(sa.Text)
#     goals = sa.Column(sa.Text)
#     goals_j = sa.Column(sa.Text)
#     content = sa.Column(sa.Text)
#     content_j = sa.Column(sa.Text)
#     lang_of_inst = sa.Column(sa.Text)
#     pollicy = sa.Column(sa.Text)
#     individual_study = sa.Column(sa.Text)
#     ref = sa.Column(sa.Text)
#     notes = sa.Column(sa.Text)
#     schedule = sa.Column(sa.String(length=500))
#     url = sa.Column(sa.String(length=300))

def MakeIndex(engine, tablename, indexname, cols): 
    cols = ','.join(cols)
    with engine.connect() as con:
        con.execute("""ALTER TABLE """ + tablename + """ ADD FULLTEXT INDEX IF NOT EXISTS """ + indexname +  """fulltextIndex2(""" + cols + """) COMMENT 'tokenizer "TokenMecab"';""")


Base.metadata.create_all(engine)
Session = sa.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# testdata = scrape.getSyllabus('2022',helper.getCourseInfo())
# for x in tqdm(testdata):
#     newCourse = Course(regno=int(x['regno']),ay=x['ay'],term=x['term'],cno=x['cno'],title_e=x['title_e'],title_j=x['title_j'],lang=x['lang'],instructor=x['instructor'],unit_e=x['unit_e'],koma_lecture_e=x['koma_lecture_e'],koma_seminar_e=x['koma_seminar_e'],koma_labo_e=x['koma_labo_e'],koma_act_e=x['koma_act_e'],koma_int_e=x['koma_int_e'],descreption=x['descreption'],descreption_j=x['descreption_j'],goals=x['goals'],goals_j=x['goals_j'],content=x['content'],content_j=x['content_j'],lang_of_inst=x['lang_of_inst'],pollicy=x['pollicy'],individual_study=x['individual_study'],ref=x['ref'],notes=x['notes'],schedule=x['schedule'],url=x['url'])
#     session.add(newCourse)
    
# MakeIndex(engine,'syllabuses','fulltextindex1',['content_j'])
# MakeIndex(engine,'syllabuses','fulltextindex2',['lang_of_inst'])
# MakeIndex(engine,'syllabuses','fulltextindex3',['content','content_j'])
# MakeIndex(engine,'syllabuses','fulltextindex4',['descreption','descreption_j'])
# session.commit()

# start=time.time()
# courses = session.query(Course).all()
# for course in courses:
#     print(" - " + course.title_j + ' ' + course.title_e)
# print("--- %s seconds ---" % (time.time() - start))

data = helper.getOpenClassrooms()
# items = []
# for entry in data:
#     stmt = insert(Classrooms).values(room = entry['room'],)
# session.execute(Classrooms.__table__.insert(), data)
tags = []
for j in ['m','tu','w','th','f','sa']:
    for i in ['1','2','3','l4','4','5','6','7','8']:    
        tags.append(j+i)
for a in tags:
    print(f'{a} = x["{a}"]',end=', ')
stmt_dict = {}
for tag in tags:
    stmt_dict[tag]=bindparam(tag)


classrooms = Classrooms()

for x in data:
    # stmt = classrooms.update().\
    # where(classrooms.c.room == x['room']).\
    # values(
    #     x
    # )
    # session.execute(stmt, data)
    newClass = Classrooms(m1 = x["m1"], m2 = x["m2"], m3 = x["m3"], ml4 = x["ml4"], m4 = x["m4"], m5 = x["m5"], m6 = x["m6"], m7 = x["m7"], m8 = x["m8"], tu1 = x["tu1"], tu2 = x["tu2"], tu3 = x["tu3"], tul4 = x["tul4"], tu4 = x["tu4"], tu5 = x["tu5"], tu6 = x["tu6"], tu7 = x["tu7"], tu8 = x["tu8"], w1 = x["w1"], w2 = x["w2"], w3 = x["w3"], wl4 = x["wl4"], w4 = x["w4"], w5 = x["w5"], w6 = x["w6"], w7 = x["w7"], w8 = x["w8"], th1 = x["th1"], th2 = x["th2"], th3 = x["th3"], thl4 = x["thl4"], th4 = x["th4"], th5 = x["th5"], th6 = x["th6"], th7 = x["th7"], th8 = x["th8"], f1 = x["f1"], f2 = x["f2"], f3 = x["f3"], fl4 = x["fl4"], f4 = x["f4"], f5 = x["f5"], f6 = x["f6"], f7 = x["f7"], f8 = x["f8"], sa1 = x["sa1"], sa2 = x["sa2"], sa3 = x["sa3"], sal4 = x["sal4"], sa4 = x["sa4"], sa5 = x["sa5"], sa6 = x["sa6"], sa7 = x["sa7"], sa8 = x["sa8"])
    session.add(newClass)