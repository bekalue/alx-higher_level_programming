#!/usr/bin/python3
'''Prints all State objects and their City objects in a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
        result = session.query(State).order_by(State.id.asc()).all()
        for state in result:
            print('{}: {}'.format(state.id, state.name))
            for city in state.cities:
                print('\t{}: {}'.format(city.id, city.name))
        session.close()
