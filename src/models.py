import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    favorites = relationship('Favorite', back_populates='user', cascade='all, delete')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)  # Ensure there is a primary key
    name = Column(String(100), nullable=False)
    description = Column(String(500))

    favorites = relationship('Favorite', back_populates='character', cascade='all, delete')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)  # Ensure there is a primary key
    name = Column(String(100), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))

    favorites = relationship('Favorite', back_populates='planet', cascade='all, delete')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)  # Ensure there is a primary key
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'character_id': self.character_id,
            'planet_id': self.planet_id
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
