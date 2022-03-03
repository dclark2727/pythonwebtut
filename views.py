from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import login_required, current_user
from models import Note
from __init__ import db
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
   
    return render_template("/home.html", user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.userID == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})

