"""
Program: read_db.py
Author: Lily Ellison
Last date modified: 04/17/2023

The purpose of this program is to read databases and print out the contents.

"""

import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return: person info
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows # return the rows


def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return: rows with student info
    """
    s_cur = conn.cursor()
    s_cur.execute("SELECT * FROM student")

    s_rows = s_cur.fetchall()

    return s_rows # return the rows


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)

    with conn:
        s_rows = select_all_students(conn)
        for s_row in s_rows:
            print(s_row)
