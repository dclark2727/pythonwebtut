import mysql.connector

def getShops():
    try:
        with mysql.connector.connect(
            host="localhost",
            user="admin",
            password="coffeeadmin1",
            database = 'coffeedb'
        ) as coffeeDB:
            print(coffeeDB)
            mycursor = coffeeDB.cursor()
            sql = "SELECT * FROM shops"
            mycursor.execute(sql)
            records = mycursor.fetchall()
            for row in records:
                print(row)


    except mysql.connector.Error as e:
        print(e)

    return records



    