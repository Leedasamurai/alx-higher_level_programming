#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.

import sys
import MySQLdb

#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

