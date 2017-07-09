from flask import Flask, render_template

import note


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/note/<note_id>")
def get_note(note_id):
	note_content = note.read_note(note_id)
	return render_template('note.html', note_content=note_content)
