from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

base = declarative_base


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable="False")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable="False")
    description = Column(String(250))
    platform = Column(String(250), nullable="False")

    item_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship("Genre", backref=backref("items"))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'platform': self.platform,
        }


engine = create_engine('sqlite:///gamescatalog.db')
base.metadata.create_all(engine)