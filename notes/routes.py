import logging
from notes import db, note
from notes.forms import AddForm
from flask import render_template, request, send_file, flash, redirect


@note.route('/', methods=['GET', 'POST'])
@note.route('/index', methods=['GET', 'POST'])
def index():
    items = get_note()
    form = AddForm()

    if form.validate_on_submit():
        add_note(form.add_note.data)
        flash('Note "{}" has been added!'.format(
            form.add_note.data))
        return redirect('/index')

    return render_template('index.html', notes=items, form=form)

@note.route('/sitemap.xml', methods=['GET', 'POST'])
def site_map():
    try:
        return send_file('/app/static/sitemap.xml', attachment_filename='sitemap.xml')
    except Exception as e:
        return str(e)

@note.route('/add', methods=['POST'])
def add_note(msg=""):

    note.logger
    if not msg:
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
        try:
            return db.select_note_by_id(conn, id)
        except Exception as e:
            return "Failed to delete Note: %s" % e
