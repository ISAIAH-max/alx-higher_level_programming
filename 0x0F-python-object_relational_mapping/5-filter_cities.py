#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd="Mlewaisaiah1998", db=argv[3], charset="utf8")
    cur = conn.cursor()
    sql= "SELECT * FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC"
    query_rows = cur.execute(sql, (argv[4], ))
    print(', '.join([row[0] for row in cur.fetchall()]))    
    cur.close()
    conn.close()
