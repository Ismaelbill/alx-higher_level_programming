#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    argv = sys.argv
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT cities.name FROM cities \
                 INNER JOIN states ON states.id = cities.state_id \
                 WHERE states.name = %s", (argv[4], ))

    rows = cur.fetchall()
    strr = ''
    for row in rows:
        strr += ' ' + row[0] + ','
    print(strr[1:-1])
    cur.close()
    con.close()
