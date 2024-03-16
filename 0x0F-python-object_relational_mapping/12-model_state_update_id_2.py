#!/usr/bin/python3
"""
 script that changes the name of a State object from the database hbtn_0e_6_usa
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

    # Get data
    state_to_update = session.query(State).filter(State.id == 2).first()
    state_to_update.name = "New Mexico"

    session.commit()

    session.close()
