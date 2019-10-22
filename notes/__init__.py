import logging
from flask import Flask

note = Flask(__name__)

from notes import db, routes

sql_create_notes_table = """ CREATE TABLE IF NOT EXISTS notes (
                                        id integer PRIMARY KEY,
                                        data text
                                    ); """

conn = db.create_connection()
if conn is not None:
    db.create_table(conn, sql_create_notes_table)
else:
    logging.error("Error! cannot create the database connection.")

conn.commit()
conn.close()
