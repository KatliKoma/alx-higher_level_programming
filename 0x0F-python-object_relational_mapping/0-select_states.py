#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
