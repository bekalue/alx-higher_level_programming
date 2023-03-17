#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute(
            'SELECT cities.name FROM cities INNER JOIN states ' +
            'ON cities.state_id = states.id WHERE states.name=%s ' +
            'ORDER BY cities.id ASC;', [state_name]
            )
    result = cur.fetchall()
    print(', '.join(map(lambda x: x[0], result)))
    cur.close()
    db.close()
