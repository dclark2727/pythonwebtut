from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from models import Note
from __init__ import db
import json
from py import getShops


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    data = getShops.getShops()
    
   

    return render_template("/home.html", user=current_user, shopData = data)


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

@views.route('/favorites')
@login_required
def favorites():
 
    return render_template("/favorites.html", user=current_user)

@views.route('/add_favorites')
@login_required
def add_favorites():
    
    print('ayyyy')
    
    return redirect(url_for("views.home"))

