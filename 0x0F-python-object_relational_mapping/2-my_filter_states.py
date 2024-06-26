#!/usr/bin/python3
"""script that takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
                   WHERE name = '{}' ORDER BY id ASC""".format(state_searched))
    
    states = cursor.fetchall()

    for state in states:
        print(state)
    
    cursor.close()
    db.close()
