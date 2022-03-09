from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import login_required, current_user
from models import Note
from __init__ import db
import json
from py import getShops


views = Blueprint('views', __name__)

# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')

#         if len(note) < 1:
#             flash('Note is too short.', category='error')
#         else:
#             newNote = Note(data = note, userID=current_user.id)
#             db.session.add(newNote)
#             db.session.commit()
#             flash('Note added!', category='success')

#     return render_template("/home.html", user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    shops = getShops()
  
    return render_template("/home.html", user=current_user, shopData = shops)


@views.route('/get-sdata',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.userID == current_user.id:
            db.session.delete(note)
            db.session.commit() 
            
    return jsonify({})


