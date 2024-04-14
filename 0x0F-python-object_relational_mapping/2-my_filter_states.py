#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to retrieve data from states table
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    try:
        # Execute the SQL command
        cursor.execute(query)
        
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        
        # Print the results
        for row in results:
            print(row)
    except Exception as e:
        print("Error:", e)

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()
