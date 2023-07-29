#!/usr/bin/python3

"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=passwd,
        db=db
    )
    cur = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s"

    cur.execute(query, (state_name,))
    cities = cur.fetchall()

    for i, city in enumerate(cities):
        print(city[0], end='')
        if i < len(cities) - 1:
            print(', ', end='')

    cur.close()
    db.close()
