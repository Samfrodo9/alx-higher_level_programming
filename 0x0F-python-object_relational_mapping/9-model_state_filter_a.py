#!/usr/bin/python3

"""
    A script that list state objects from the
    database hbtn_0e_6_usa filtered to contain
    the letter a
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")
                                        ).order_by(State.id).all()
    for state in states:
        print(f"{state.id} {state.name}")
    session.close()
