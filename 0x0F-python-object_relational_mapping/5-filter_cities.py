#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    sql= "SELECT * FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC"
    query_rows = cur.execute(sql, (argv[4], ))
    rows = cur.fetchall()
    result = []
    x = 0
    for row in rows:
        result.append(rows[x][0])
        x += 1
    print(", ".join(result))
    cur.close()
    conn.close()
