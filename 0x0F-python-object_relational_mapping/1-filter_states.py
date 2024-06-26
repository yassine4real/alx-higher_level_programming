#!/usr/bin/python3
"""lists all states with a name starting with
   N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cur = connection.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                 ORDER BY id ASC""")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    connection.close()
