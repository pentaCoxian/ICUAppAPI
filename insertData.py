import os
import scrape
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import time
from tqdm import tqdm
# Load env variables
load_dotenv()
engine = sa.create_engine(os.environ['MARIADB_ADDRESS'],echo=True)
Base = declarative_base()



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

def MakeIndex(engine, tablename, indexname, cols): 
    cols = ','.join(cols)
    with engine.connect() as con:
        con.execute("""ALTER TABLE """ + tablename + """ ADD FULLTEXT INDEX IF NOT EXISTS """ + indexname +  """fulltextIndex2(""" + cols + """) COMMENT 'tokenizer "TokenMecab"';""")


Base.metadata.create_all(engine)
Session = sa.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

testdata = scrape.getSyllabus('2022',helper.getCourseInfo())
for x in tqdm(testdata):
    newCourse = Course(regno=int(x['regno']),ay=x['ay'],term=x['term'],cno=x['cno'],title_e=x['title_e'],title_j=x['title_j'],lang=x['lang'],instructor=x['instructor'],unit_e=x['unit_e'],koma_lecture_e=x['koma_lecture_e'],koma_seminar_e=x['koma_seminar_e'],koma_labo_e=x['koma_labo_e'],koma_act_e=x['koma_act_e'],koma_int_e=x['koma_int_e'],descreption=x['descreption'],descreption_j=x['descreption_j'],goals=x['goals'],goals_j=x['goals_j'],content=x['content'],content_j=x['content_j'],lang_of_inst=x['lang_of_inst'],pollicy=x['pollicy'],individual_study=x['individual_study'],ref=x['ref'],notes=x['notes'],schedule=x['schedule'],url=x['url'])
    session.add(newCourse)

    
MakeIndex(engine,'syllabuses','fulltextindex1',['content_j'])
MakeIndex(engine,'syllabuses','fulltextindex2',['lang_of_inst'])
MakeIndex(engine,'syllabuses','fulltextindex3',['content','content_j'])
MakeIndex(engine,'syllabuses','fulltextindex4',['descreption','descreption_j'])
session.commit()

start=time.time()
courses = session.query(Course).all()
for course in courses:
    print(" - " + course.title_j + ' ' + course.title_e)
print("--- %s seconds ---" % (time.time() - start))