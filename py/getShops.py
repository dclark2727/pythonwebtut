import sqlite3 as sql
from unicodedata import name
from __init__ import db
from py import coffeeScraper


def getShops():  
    try:
        # Connecting to database
        connector = sql.connect('database.db')
        # Creating cursor
        c =  connector.cursor() 
        
        query = "SELECT * FROM shops"
        c.execute(query)
        shops = c.fetchall()
    
    except:
        print('error')

    return shops

  
