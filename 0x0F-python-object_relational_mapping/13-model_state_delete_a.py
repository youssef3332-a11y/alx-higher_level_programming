#!/usr/bin/python3
"""
Delete all State objects with a name containing the letter 'a' from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./delete_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine connected to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Use a context manager to handle the session
    session = Session()
    # Query for the State objects where the name contains the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the matched State objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()
