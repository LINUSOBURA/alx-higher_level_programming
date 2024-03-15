#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
"""

import sys

import MySQLdb


def mysqlconnect():
    """
    Establishing mysql connection to the database
    """

    db_connection = MySQLdb.connect(user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM states RIGHT JOIN cities ON cities.state_id = states.id"
    )

    for state in cursor.fetchall():
        print(state)

    db_connection.close()


if __name__ == "__main__":
    mysqlconnect()
