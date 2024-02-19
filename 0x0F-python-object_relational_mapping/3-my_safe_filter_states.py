#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Safe from SQL injections.

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = db.cursor()
    q_statement = SELECT * FROM states\
Where states.name ='{}'".format(sys.argv[4])
    c.execute(q_statement)
    row = c.fetchall()
    for row in rows:
        print(row)
