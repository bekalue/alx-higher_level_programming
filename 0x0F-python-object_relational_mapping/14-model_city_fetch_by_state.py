#!/usr/bin/python3
'''Prints all City objects and their State in a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]
        DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        State.cities = relationship('City', back_populates='state')
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = session.query(City).order_by(City.id.asc()).all()
        for row in result:
            print('{}: ({}) {}'.format(row.state.name, row.id, row.name))
