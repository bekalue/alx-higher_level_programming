#!/usr/bin/python3
'''Prints the first state object in a database
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3])
        )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State).first()
    if result is not None:
        print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')
