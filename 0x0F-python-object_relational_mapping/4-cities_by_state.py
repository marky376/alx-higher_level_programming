#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            user=argv[1],
            password=argv[2],
            database=argv[3],
            host="localhost",
            port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    result = cursor.fetchall()
    for x in result:
        print(x)
