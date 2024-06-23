#!/usr/bin/python3
""" Get a state """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if "__main__" == __name__:
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.like(sys.argv[4])
                                        ).one_or_none()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
