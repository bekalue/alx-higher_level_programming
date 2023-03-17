#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
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
            'SELECT * FROM states WHERE name="{}"' +
            'ORDER BY states.id ASC'.format(state_name)
            )
    [print(result) for result in cur.fetchall()]
    cur.close()
    db.close()
