#!/usr/bin/python3
'''Adds a state object into database table.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name='Louisiana')
    session.add(new_state)
    try:
        session.flush()
        session.refresh(new_state)
        if new_state.id is not None:
            print(f'{new_state.id}')
    except Exception:
        session.rollback()
    finally:
        session.commit()
