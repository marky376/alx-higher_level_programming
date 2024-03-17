#!/usr/bin/python3
"""
This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            database=argv[3])
    cursor = connection.cursor()
    state_name = argv[4]
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    cities_list = ', '.join(city[0] for city in results)
    print(cities_list)
