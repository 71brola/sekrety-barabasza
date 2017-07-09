from flask import Flask

import note


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/note/<note_id>")
def get_note(note_id):
    return note.read_note(note_id)
