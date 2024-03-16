#!/usr/bin/python3
"""
 takes in an argument and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.
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

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(
        sys.argv[4]))

    for state in cursor.fetchall():
        print(state)

    db_connection.close()


if __name__ == "__main__":
    mysqlconnect()
