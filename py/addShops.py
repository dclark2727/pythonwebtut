import sqlite3 as sql
from unicodedata import name
from __init__ import db
from py import coffeeScraper


def add_shops(name, image, location, rating, reviews, tags):  
  scraper = coffeeScraper
  shops = scraper.scrapeShops()
  try:
    # Connecting to database
    connector = sql.connect('database.db')
    # Getting cursor
    c =  connector.cursor() 
    for k, v in shops.items():
      name = str(k)
      image = str(v[0])
      location =str(v[1])
      rating = str(v[2])
      reviews = str(v[3])
      tags = str(v[4])

      # table = """ CREATE TABLE SHOPS (
      #       id INT AUTO_INCREMENT PRIMARY KEY,
      #       name VARCHAR(255),
      #       image VARCHAR(255),
      #       location VARCHAR(255),
      #       rating VARCHAR(255),
      #       reviews VARCHAR(255),
      #       tags VARCHAR(255))
      #       """
      
      #sql = 'INSERT INTO shops (name, image, location, rating, reviews, tags) VALUES (\"' + name + '\", \"' + image + '\", \"' + location + '\", \"' + rating + '\", \"' + reviews + '\", \"' + tags + "\")"
     
      #c.execute(sql)
     
    # Applying changes
    connector.commit()
  except:
    print('error')

  print(shops)
  
  