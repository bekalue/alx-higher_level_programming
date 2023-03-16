#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='bekalue',
            passwd='#Unbeatable2054',
            db='hbtn_0e_0_usa'
            )
    cur = db.cursor()
    state_name = 'Arizona'
    cur.execute(
            'SELECT * FROM states WHERE name="{}"' +
            'ORDER BY states.id ASC'.format(state_name)
            )
    [print(result) for result in cur.fetchall()]
    cur.close()
    db.close()
