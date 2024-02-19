#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database
"""
import MySQLdb
from sys import argv

# Code shouldn't be executed when imported
if __name__ == '__main__':
    # A connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # The ability to have multiple seperate working environment
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
