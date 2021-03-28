#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for row in range(rows):
        if row[1][0] == 'N':
            print(cur.fetchone())
    cur.close()
    db.close()
