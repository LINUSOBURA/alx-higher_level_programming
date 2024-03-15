#!/usr/bin/python3
"""
List all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states WHERE name\
        LIKE 'N%' ORDER BY id ASC;")

    for state in cursor.fetchall():
        print(state)

    db_connection.close()


if __name__ == "__main__":
    mysqlconnect()
