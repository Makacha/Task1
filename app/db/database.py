from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

engine = create_engine('postgresql://postgres:Anh260702@localhost:5432/postgres')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
