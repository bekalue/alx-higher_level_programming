#!/usr/bin/python3
'''prints the id of a state object with a given state name in a database table.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State, Base


if __name__ == "__main__":
    user = sys.argv[1]
    pword = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    chk = map(lambda x: x.isalpha() or (x in (' ', '%', '_')), state_name)
    if not all(chk):
        state_name = ''
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
        user, pword, db_name
        )
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State).filter(State.name == state_name).first()
    if result is not None:
        print('{}'.format(result.id))
    else:
        print('Not found')
