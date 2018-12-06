
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Article(Base):
    __tablename__ = 'v_news'
    News_Id = Column(Integer,primary_key=True)
    News_Title = Column(String)
    News_Dt = Column(TIMESTAMP)
    Website_Id = Column(String)
    URL = Column(String)
    Keywords = Column(String)
    Abstract = Column(String)
    Author = Column(String)
    Content = Column(LONGTEXT)
    Image_URL1 = Column(String)
    Image_URL2 = Column(String)
    Image_URL3 = Column(String)
    Image_URL4 = Column(String)
    Original_Flag = Column(Integer)
    Tag_Group = Column(String)
    Update_Tm = Column(TIMESTAMP)