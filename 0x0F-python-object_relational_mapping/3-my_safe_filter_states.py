#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in a table of
a database where name matches the argument.
But is safe from MySQL injections!
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    sql = ("SELECT * FROM states WHERE name = '{:s}'ORDER BY id ASC")
    query_rows = cur.execute(sql, (argv[4]))
    for row in query_rows:
        print(cur.fetchone())
    cur.close()
    conn.close()
