import os
import logging
import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None

    try:
        conn = sqlite3.connect('notes.db')
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
