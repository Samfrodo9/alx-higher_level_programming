#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv


def run():
    '''defines the main function'''
    db_usr = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    args = argv[4]
    db_host = "localhost"
    db_port = 3306
    try:
        connect = MySQLdb.connect(host=db_host, port=db_port, user=db_usr,
                                  passwd=db_pass, db=db_name, charset="utf8")
        cur = connect.cursor()
        query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC;".format(args)
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            print(i)
        cur.close()
        connect.close()
    except Exception:
        pass


if __name__ == "__main__":
    run()
