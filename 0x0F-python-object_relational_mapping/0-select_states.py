#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    c.execute("SELECT * FROM states")
    ans = c.fetchall()
    for row in ans:
        print(row)
