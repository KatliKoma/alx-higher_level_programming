#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor
    cur = db.cursor()

    # Execute SQL query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Initialize a set to store distinct states
    distinct_states = set()

    # Fetch all rows and print distinct states
    for row in cur.fetchall():
        state_id, state_name = row
        if state_name not in distinct_states:
            print(row)
            distinct_states.add(state_name)

    # Close cursor and database connection
    cur.close()
    db.close()
