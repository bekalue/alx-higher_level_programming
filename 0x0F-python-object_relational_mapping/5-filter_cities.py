#!/usr/bin/python3
'''Prints all cities of a given state in a database.
'''
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        state_name = sys.argv[4]
        cursor = db_connection.cursor()
        cursor.execute(
            'SELECT cities.name FROM cities' +
            ' INNER JOIN states ON cities.state_id = states.id' +
            ' WHERE CAST(states.name AS BINARY) = %s' +
            ' ORDER BY cities.id ASC;',
            [state_name]
        )
        results = cursor.fetchall()
        print(', '.join(map(lambda x: x[0], results)))
        db_connection.close()
