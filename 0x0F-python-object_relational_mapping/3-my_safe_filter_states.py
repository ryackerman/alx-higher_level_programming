#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4], ))
    rows = crs.fetchall()
    for row in rows:
        print(row)
    crs.close()
    db.close()
