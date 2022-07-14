import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
import scrape

engine = sa.create_engine("mariadb+mariadbconnector://python:pythonAccess56@172.31.54.136:3306/syllabusdb?charset=utf8mb4",echo=True)
Base = declarative_base()

class Course(Base):
    __tablename__ ="testtable"
    __table_args__ = {
        'mariadb_ENGINE': 'mroonga',
        'mariadb_DEFAULT_CHARSET': 'utf8mb4'
    }
    regno = sa.Column(sa.Integer, primary_key=True)
    title_j = sa.Column(sa.String(length=15900))
    title_e = sa.Column(sa.String(length=400))

def MakeIndex(engine, tablename, indexname, cols): 
    cols = ','.join(cols)
    with engine.connect() as con:
        con.execute("""ALTER TABLE """ + tablename + """ ADD FULLTEXT INDEX IF NOT EXISTS """ + indexname +  """fulltextIndex2(""" + cols + """) COMMENT 'tokenizer "TokenMecab"';""")


Base.metadata.create_all(engine)
Session = sa.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

newCourse = Course(regno = 25654,title_j="""SQL 情報管理 言語 システム 解説 利用 マルチメディア データベースシステム データ 的 形態 データベース サービス 情報技術 １つ 中核 技術 ビッグデータ 社会 開発 情報システム 技法 set test WEB 検索 経営 時間 小規模 企業""",title_e="Course")
session.add(newCourse)
MakeIndex(engine,'testtable','fulltextindex',['title_j'])
session.commit()


courses = session.query(Course).all()
for course in courses:
    print(" - " + course.title_j + ' ' + course.title_e)
