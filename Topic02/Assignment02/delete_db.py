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
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows # return the rows


def select_all_students(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows # return the rows


def delete_person(conn, id):
    """Delete a person by person id
    :param conn: database connection
    :param id: id of the person
    :return:
    """
    sql = 'DELETE FROM person WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_student(conn, id):
    """Delete a student by person id
    :param conn: database connection
    :param id: id of the person
    :return:
    """
    sql = 'DELETE FROM student WHERE id=?'
    s_cur = conn.cursor()
    s_cur.execute(sql, (id,))

def delete_all_person(conn):
    """Delete all rows in the person table
    :param conn: database connection
    :return:
    """
    sql = 'DELETE FROM person'
    cur = conn.cursor()
    cur.execute(sql)


def delete_all_student(conn):
    """Delete all rows in the student table
    :param conn: database connection
    :return:
    """
    sql = 'DELETE FROM student'
    s_cur = conn.cursor()
    s_cur.execute(sql)


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")
    with conn:
        #delete_all_person(conn)
        delete_person(conn, 1)
        rows = select_all_persons(conn)
        for row in rows:
            print(row)
        delete_student(conn, 1)
        #delete_all_student(conn)
        s_rows = select_all_students(conn)
        for s_row in s_rows:
            print(s_row)