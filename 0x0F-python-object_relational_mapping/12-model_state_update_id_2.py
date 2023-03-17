#!/usr/bin/pyhton3
'''Updates a State object in a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format('bekalue', '#Unbeatable2054', 'hbtn_0e_6_usa'))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    session.query(State).filter(State.id == 2).update({State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()
