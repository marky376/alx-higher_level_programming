#!/usr/bin/python3

"""
    script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
        Create an engine that provides connectivity
        to your MySQL server. create_engine

        Create a Session object which will allow you to
        interact with the database.sessionmaker function

        Use the session to query the State objects.
        You can order the results by states.id using the order_by function.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id)
    for state in results:
        print("{}: {}".format(state.id, state.name))
