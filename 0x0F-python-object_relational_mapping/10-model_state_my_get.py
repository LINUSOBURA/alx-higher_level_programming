#!/usr/bin/python3
"""
 script that prints the State object with the name\
     passed as argument from the database hbtn_0e_6_usa
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    database_url = ('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))

    engine = create_engine(database_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    get_a_state = session.query(State).filter(State.name == argv[4]).first()

    if get_a_state:
        print('{}'.format(get_a_state.id))
    else:
        print('Not Found')

    session.close()
