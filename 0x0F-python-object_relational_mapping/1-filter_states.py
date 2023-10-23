#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crs = db.cursor()
    crs.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = crs.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    crs.close()
    db.close()
