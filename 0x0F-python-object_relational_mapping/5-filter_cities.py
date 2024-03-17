#!/usr/bin/python3
"""a script that takes in the name of a state\
   as an argument and lists all cities of that state,\
   using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (state_name,))

    rows = cur.fetchall()

    if rows:
        for index, row in enumerate(rows):
            for city in row:
                if index < len(rows) - 1:
                    print(city, end=', ')
                else:
                    print(city)
    else:
        print()

    cur.close()
    db.close()
