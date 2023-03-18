#!/usr/bin/python3
'''Prints all rows in the states table of a database.
'''
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM states ORDER BY id ASC;')
        results = cursor.fetchall()
        for result in results:
            print(result)
        db_connection.close()
