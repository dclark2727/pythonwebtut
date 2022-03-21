from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from models import Note
from __init__ import db
import json
from py import getShops
import sqlite3 as sql


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    data = getShops.getShops()
    
   

    return render_template("/home.html", user=current_user, shopData = data)



@views.route('/favorites')
@login_required
def favorites():
    connector = sql.connect('database.db')
    c =  connector.cursor() 
    user = current_user.id
    query = "SELECT * FROM favorite_shop WHERE userID = '%s'" % user
    print(query)
    c.execute(query)
    favData = c.fetchall()
    connector.close()

    return render_template("/favorites.html", user=current_user, favData = favData)

@views.route('/add_favorites', methods=['POST'])
@login_required
def add_favorites():

    if request.method == 'POST':
        id = request.form["id"]
        n = request.form["name"]
        im = request.form["image"]
        l = request.form["loc"]
        r = request.form["rating"]
        re = request.form["reviews"]
        t = request.form["tags"]
        user1 = current_user.id
      
    
        # Connecting to database
        connector = sql.connect('database.db')
        c =  connector.cursor() 
        query = "SELECT id FROM favorite_shop WHERE userID = '%s' " % user1
     
        c.execute(query)
        shop = c.fetchall()
        added = []
        for i in shop:
            added.append(str(i[0]))
     
        sID = id
        if sID not in added:
            query2 = "INSERT INTO favorite_shop (id, name , image , loc , rating, reviews, tags, userID) VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (id,n,im,l,r,re,t,user1) 
            print(query2)
            c.execute(query2)
            connector.commit()
            connector.close()
            flash('Shop added to favorites!', category = 'success')
        else:
            flash('Shop already favorited', category='error')
            
    return redirect(url_for('views.home'))




@views.route('/delete_favorites', methods=['POST'])
@login_required
def delete_favorites():

    if request.method == 'POST':
        id = request.form['id']
        query = "DELETE FROM favorite_shop WHERE id = %s" % id
        connector = sql.connect('database.db')
        c =  connector.cursor() 
        c.execute(query)
        connector.commit()
        connector.close()
        flash('Shop removed from favorites', category = 'success')
    return redirect(url_for('views.favorites'))

    

