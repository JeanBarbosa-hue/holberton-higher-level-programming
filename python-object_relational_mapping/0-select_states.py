#!/usr/bin/python3

"""Imports needed for functionality"""
import MySQLdb
import sys

"""Module with function to list all states from db"""


def list_states(mysql_username, mysql_password, database_name):
    # Connect to the MySQL server
    try:
        connection = MySQLdb.connect(
            host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
        cursor = connection.cursor()
    except MySQLdb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

    # Execute the query to list all states sorted by states.id in ascending order
    try:
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        results = cursor.fetchall()
    except MySQLdb.Error as e:
        print(f"Error executing the query: {e}")
        cursor.close()
        connection.close()
        sys.exit(1)

    # Display the results
    for row in results:
        state_id, state_name = row
        print(f"{state_id}: {state_name}")

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py mysql_username mysql_password database_name")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(mysql_username, mysql_password, database_name)
