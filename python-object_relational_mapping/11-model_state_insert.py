#!/usr/bin/python3

"""script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name = 'Louisiana'

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name=name)
    session.add(state)
    session.commit()

    print(state.id)

    session.close()
