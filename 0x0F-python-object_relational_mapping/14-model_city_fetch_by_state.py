#!/usr/bin/python3
"""
 script that prints prints all City\
     objects from the database hbtn_0e_14_usa:
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    database_url = ('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))

    engine = create_engine(database_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
