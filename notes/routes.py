from notes import db, note
from flask import request
from flask_wtf.csrf import CSRFProtect


@note.route('/')
@note.route('/index')
@csrf.exempt
def index():
    return "Welcome to your veryyyyy basic NotePad"


@note.route('/add', methods=['POST'])
def add_note():
    data = request.get_json(force=True)
    msg = data.get('message')

    if not msg:
        return "No Message sent in request."

    conn = db.create_connection()
    with conn:
        try:
            db.create_note(conn, (str(msg),))
            return "Note added successfully!"
        except Exception as e:
            return "Failed to add Note: %s" % e


@note.route('/delete', methods=['DELETE'])
def delete_note():
    id = request.args.get('id')

    conn = db.create_connection()
    with conn:
        try:
            db.delete_note(conn, id)
            return "Note deleted successfully!"
        except Exception as e:
            return "Failed to delete Note: %s" % e

@note.route('/get', methods=['GET'])
def get_note():
    id = request.args.get('id')

    conn = db.create_connection()
    with conn:
        return db.select_note_by_id(conn, id)

