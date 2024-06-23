#!/usr/bin/python3
""" Cities in state """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if "__main__" == __name__:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State, City).join(State).all()
    for state, city in states:
        print(state.name, city.id, city.name)

    session.close()
