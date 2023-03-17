#!/usr/bin/python3
'''Prints all City objects and their State in a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy import relationship, sessionmaker

from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    user = sys.argv[1]
    pword = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user,
        pword,
        db)
        )
    State.cities = relationship('City', back_populate='state')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    result = session.query(City).order_by(City.id.asc()).all()
    for row in result:
        print('{}: ({}) {}'.format(row.state.name, row.id, row.name)
