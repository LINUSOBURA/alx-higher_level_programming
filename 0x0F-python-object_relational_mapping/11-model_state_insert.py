#!/usr/bin/python3
"""
 script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # add new state to database
    new_state = State(name='Louisiana')

    session.add(new_state)

    session.commit()

    # Get new state id
    get_a_state = session.query(State).filter(
        State.name == 'Louisiana').first()
    print('{}'.format(get_a_state.id))

    session.close()
