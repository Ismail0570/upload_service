from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class FileMetadata(Base):
    __tablename__ = "file_metadata"

    id = Column(String, primary_key=True, index=True)
    filename = Column(String)
    content_type = Column(String)
    size = Column(Integer)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)