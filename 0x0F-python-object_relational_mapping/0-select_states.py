#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
from sys import argv


if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user="root", passwd="Mlewaisaiah1998", db=argv[3])
    cur = db.cursor()
    rows = cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in range(rows):
        print(cur.fetchone())
    cur.close()
    db.close()
