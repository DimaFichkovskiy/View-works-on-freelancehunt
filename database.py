import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from config import Config

engine = Config.DB_URI
Base = declarative_base(bind=engine)


class freelancehunt_data(Base):
    __tablename__ = 'freelancehunt_data'

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(20))
    title = db.Column(db.String(120))
    url = db.Column(db.String(200))


class DBDriver:
    @classmethod
    def add_work(cls, works):
        with engine.connect() as connection:
            if not any(works):
                return None
            insert_query = db.insert(freelancehunt_data)
            connection.execute(insert_query, works)


if __name__ == '__main__':
    Base.metadata.create_all()
