#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

dtabase_url = ('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]))

engine = create_engine(dtabase_url)

Session = sessionmaker(bind=engine)
session = Session()

all_states = session.query(State).order_by(State.id).all()

for state in all_states:
    print('{}: {}'.format(state.id, state.name))
