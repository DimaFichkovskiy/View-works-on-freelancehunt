import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from config import Config

engine = ''
Base = declarative_base(bind=engine)


class Works(Base):
    __tablename__ = 'works'

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(20))
    title = db.Column(db.String(120), unique=True)
    url = db.Column(db.String(200), unique=True)