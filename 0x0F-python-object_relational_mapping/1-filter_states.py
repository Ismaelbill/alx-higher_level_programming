#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":

    import MySQLdb
    import sys

    argv = sys.argv
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY'N%'")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
