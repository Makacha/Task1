from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

engine = create_engine('postgresql://postgres:Anh260702@localhost:5432/mydb')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
db = session()
