from notes import db, note
from flask import request, render_template_string, request, send_file


@note.route('/')
@note.route('/index')
def index():
    name = "world"
    template = '''<p> Hi, how are you {{ name }}! </p>'''

    if request.args.get('name'):
        name = request.args.get('name')
    
    return render_template_string(template, name=name)


@note.route('/sitemap.xml', methods=['GET', 'POST'])
def site_map():
    try:
        return send_file('/app/static/sitemap.xml', attachment_filename='sitemap.xml')
    except Exception as e:
        return str(e)


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

