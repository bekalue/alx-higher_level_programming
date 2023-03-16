#!/usr/bin/python3
'''Prints all State objects with a name that conatins 'a' in database table.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State).order_by(State.id.asc()).filter(
            State.name.like('%a%'))
    [print('{}: {}'.format(row.id, row.name)) for row in result]
