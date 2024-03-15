#!/usr/bin/python3
"""
Lists all the states of the database hbtn_0e_0_usa
"""
import sys

import MySQLdb


def mysqlconnect():
    """
    Establiishes connection to the database for querrying
    """

    db_connection = MySQLdb.connect(user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states;")

    for state in cursor.fetchall():
        print(state)

    db_connection.close()


if __name__ == "__main__":
    mysqlconnect()
