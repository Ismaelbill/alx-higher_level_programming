#!/usr/bin/python3
""" Delete a state """
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
    states = session.query(State).filter(State.name.ilike('%a%')).all()
    for st in states:
        session.delete(st)
    session.commit()
    session.close()
