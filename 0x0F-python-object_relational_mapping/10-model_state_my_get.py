#!/usr/bin/python3
'''Prints the id of a state object with a given name in a database table.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    state_name = sys.argv[4]
    check = map(lambda x: x.isalpha() or (x in (' ', '%', '_')), state_name)
    if not all(check):
        state_name = ''
    DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State).filter(State.name == state_name).first()
    if result is None:
        print('Not found')
    else:
        print(f'{result.id}')
