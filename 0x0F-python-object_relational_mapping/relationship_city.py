#!/usr/bin/python3
'''A module containing the City model.
'''


from sqlalchamy import Column, Integer, String, ForeignKey
from sqlalchamy.orm import relationship

from relationship_state import Base


class City(Base):
    """Represents every row in a city table database.
    """
    __tablename__ = 'cities'
    id = Column(
            Integer,
            auto_increment=True,
            unique=True,
            nullable=False,
            primary_key=True
            )
    name = Column(
            String(length=128)
            nullable=False
            )
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False
            )
