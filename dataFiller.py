from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Genre, Item

engine = create_engine('sqlite:///gamescatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

actionGenre = Genre(name = 'Action')
session.add(actionGenre)
session.commit()

firstItem = session.query(Genre).first()

print(firstItem.name)