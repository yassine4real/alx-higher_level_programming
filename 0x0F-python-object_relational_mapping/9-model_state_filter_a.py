#!/usr/bin/python3
"""
Lists all State objects that contain the
letter 'a' from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get states
    from the database.
    """
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(
        State.name.like("%a%")
    ).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
