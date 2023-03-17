#!/usr/bin/python3
'''Prints all city objects and their state in a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user,
        passwd,
        db)
        )
    State.cities = relationship('City', back_populates='state')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(City).order_by(City.id.asc()).all()
    for row in result:
        print('{}: ({}) {}'.format(row.state.name, row.id, row.name))
