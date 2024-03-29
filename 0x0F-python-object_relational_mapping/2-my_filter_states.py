#!/usr/bin/python3
"""script that takes in an argument and displays matching name values"""


import sys
import MySQLdb

if __name__ == "__main__":
    """main function that displays matching name values"""
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
    cur.execute("SELECT * FROM states\
                WHERE BINARY name = '{}' ORDER BY id\
                ASC".format(state_name))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
