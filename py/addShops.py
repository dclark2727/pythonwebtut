import sqlite3 as sql
from __init__ import db
from coffeeScraper import scrapeShops

shops = scrapeShops()

def add_shops(name, image, location, rating, reviews, tags):  
  try:
    # Connecting to database
    connector = sql.connect('database.db')
    # Getting cursor
    c =  connector.cursor() 
    # Adding data
    c.execute("INSERT INTO shops (name, image, location, rating, reviews, tags) VALUES (%s, %s, %s, %s, %s, %s)" %(name, image, location, rating, reviews, tags))
    # Applying changes
    c.commit() 
  except:
    print("An error has occured")



