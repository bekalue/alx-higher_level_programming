#!/usr/bin/python3
'''Prints all state object in database
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(user, passwd, db)
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(State).all()
    [print('{}: {}'.format(res.id, res.name)) for res in result]
