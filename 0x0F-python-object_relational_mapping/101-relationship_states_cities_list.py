#!/usr/bin/python3

"""
Lists all State objects and corresponding City objects contained in the DB
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).outerjoin(City).order_by(
            State.id, City.id)
    for state in results:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
