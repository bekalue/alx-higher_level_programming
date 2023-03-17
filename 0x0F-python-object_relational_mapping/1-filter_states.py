#!/usr/bin/python3

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute(
            'SELECT * FROM states WHERE name IS NOT NULL' +
            'AND LEFT(CAST(name AS BINARY), 1) = "N" ORDER BY states.id ASC;')
    [print(result) for result in cur.fetchall()]
    cur.close()
    db.close()
