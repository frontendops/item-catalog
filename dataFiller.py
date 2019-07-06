from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Genre, Item

engine = create_engine('sqlite:///gamescatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

allGenres = [
    'Adventure',
    'Puzzle',
    'Sports'
    'Simulator',
    'Multiplayer'
]

def createGenres():
    for genre in allGenres:
        session.add(Genre(name = genre))

createGenres()

session.commit()

games = session.query(Genre).all()

for game in games:
    print game.name
