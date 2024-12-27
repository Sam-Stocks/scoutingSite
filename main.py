from flask import Flask, redirect, request, jsonify, render_template, url_for
from variables import ScoutingForm
#import Counters

import csv
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "AHH"

# defining the variable
autoNotes = 0
autoNotesm = 0

@app.route('/', methods=['GET'])
def index():
    preMatchForm = ScoutingForm()
    return render_template('index.html', preMatchForm=preMatchForm, autoNotes=autoNotes, autoNotesm=autoNotesm)

@app.route('/update_auto_notes', methods=['POST'])
def update_auto_notes():
    global autoNotes, autoNotesm
    data = request.json
    if data.get("action") == "increaseAutoNote":
        autoNotes += 1
    elif data.get("action") == "decreaseAutoNote":
        autoNotes -= 1
    elif data.get("action") == "increaseAutoNoteM":
        autoNotesm += 1
    elif data.get("action") == "decreaseAutoNotem":
        autoNotesm -= 1
    return jsonify({"autoNotes": autoNotes, "autoNotesm": autoNotesm})

if __name__ == "__main__":
    app.run(debug=True)
