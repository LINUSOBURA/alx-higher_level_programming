#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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

    query = "SELECT cities.name FROM cities INNER JOIN states\
        ON cities.state_id = states.id WHERE states.name = %s"

    cursor.execute(query, (sys.argv[4], ))

    rows = cursor.fetchall()
    result = []
    for i in rows:
        result.append(i[0])
    print(", ".join(result))

    db_connection.close()


if __name__ == "__main__":
    mysqlconnect()
