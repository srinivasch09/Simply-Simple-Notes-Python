import os
import logging
import sqlite3
from sqlite3 import Error


def create_connection(name='notes.db'):
    conn = None

    try:
        conn = sqlite3.connect(name)
        os.chmod(name, 0o777)
    except Error as e:
        logging.error(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_note(conn, notes):
    query = "INSERT INTO notes(data) VALUES(?)"

    cur = conn.cursor()
    cur.execute(query, notes)

    return cur.lastrowid


def delete_note(conn, id):
    query = 'DELETE FROM notes WHERE id=?'
    
    cur = conn.cursor()
    cur.execute(query, (id,))

    conn.commit()

def select_note_by_id(conn, id=None):
    query = "SELECT * FROM notes"

    if id:
        query = query + " WHERE id = '%s'" % id

    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    return rows

def select_note_by_id_vulnerable(conn, id):
    query = "SELECT * FROM notes WHERE id = '%s'" % id

    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    return str(rows)
