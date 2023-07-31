#!/usr/bin/python3

"""Imports needed for functionality"""
import MySQLdb
import sys


def list_states(mysql_username, mysql_password, database_name):
    """Lists all states from the database hbtn_0e_0_usa"""

    """Connects to MySQL database"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    """Creates cursor to execute SQL queries"""
    cur = db.cursor()

    """Executes SQL query to select all states"""
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetches all the rows from the query"""
    rows = cur.fetchall()

    """Prints each row of the query"""
    for row in rows:
        print(row)

    """Closes cursor"""
    cur.close()

    """Closes connection to database"""
    db.close()


if __name__ == "__main__":
    """Take in arguments and passes to list_states"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(mysql_username, mysql_password, database_name)
