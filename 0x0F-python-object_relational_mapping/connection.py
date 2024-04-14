#!/usr/bin/python3

import MySQLdb

# MySQL connection parameters
host = 'localhost'
port = 3306
user = 'root'
password = 'new_password'
database = 'hbtn_0e_0_usa'

# Establish MySQL connection
try:
    db = MySQLdb.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        db=database
    )
    print("MySQL connection established successfully.")
except MySQLdb.Error as e:
    print("Error connecting to MySQL:", e)
