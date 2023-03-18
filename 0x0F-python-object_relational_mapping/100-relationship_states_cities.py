#!/usr/bin/python3
'''Adds a State object and one of its City object children to a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]
        DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        new_state = State(name='California')
        new_city = City(name='San Francisco')
        new_state.cities.append(new_city)
        session.add(new_state)
        session.commit()
