import os
from sqlalchemy import create_engine
from app.models import Base   

engine = create_engine(os.getenv("DATABASE_URL"))

Base.metadata.create_all(bind=engine)
