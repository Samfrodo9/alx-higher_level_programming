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
        query = "SELECT name FROM cities "
        query += "WHERE state_id = (SELECT id FROM states "
        query += "WHERE name = %s)"
        cur.execute(query, (match, ))
        result = cur.fetchall()
        result_list = []
        for i in result:
            result_list.append(i[0])
        print(", ".join(result_list))
        cur.close()
        connect.close()
    except Exception as e:
        pass

if __name__ == "__main__":
    run()
