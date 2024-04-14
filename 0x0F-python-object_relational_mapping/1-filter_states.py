#!/usr/bin/python3
""" script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':

    args = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()

    conn.close()
