#!/usr/bin/python3
"""this module"""
import MySQLdb
import sys


def list_creates(u, p, d):
    """ this is the description"""
    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=p, db=d)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    list_creates(username, password, db)
