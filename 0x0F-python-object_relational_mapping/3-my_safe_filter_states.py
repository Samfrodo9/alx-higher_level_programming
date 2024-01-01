#!/usr/bin/python3
'''this module is a script that lists all
states from the database hbtn_0e_0_usa:'''

import MySQLdb
from sys import argv


def main():
    '''defines the main function'''
    db_pass = argv[2]
    db_usr = argv[1]
    db_name = argv[3]
    db_host = "localhost"
    db_port = 3306
    match = argv[4]
    try:
        connect = MySQLdb.connect(host=db_host, port=db_port, user=db_usr,
                                  db=db_name, passwd=db_pass, charset="utf8")
        cur = connect.cursor()
        query = "SELECT * FROM states WHERE "
        query += "name REGEXP %s ORDER BY id ASC"
        cur.execute(query, (match, ))
        result = cur.fetchall()
        for i in result:
            print(i)
        cur.close()
        connect.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
