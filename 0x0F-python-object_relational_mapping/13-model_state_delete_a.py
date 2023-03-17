#!/usr/bin/python3
'''Deletes all state objects with 'a' in its name in a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine("mysql://{]:{}@localhost:3303/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3])
        )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    session.query(State).filter(State.name.like('%a%')).delete(
            synchronize_session=False
            )
    session.commit()
