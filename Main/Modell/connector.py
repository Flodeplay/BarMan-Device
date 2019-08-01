import mysql.connector
from Main.Modell.Class.recipe import Recipe

class Connector:
    key = "193101163196977"

    def __init__(self):
        self.conn = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
          database="barman"
        )

    def __verifyKey(self):
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT * FROM k_key WHERE k_key = "+self.key+" Limit 1")
        mycursor.fetchall()
        if mycursor.rowcount == 0 or mycursor.rowcount > 1:
            raise ValueError
        else:
            print("Key verified")

    def getRecipies(self):
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT * FROM r_recipe WHERE r_k_key = "+self.key+" Limit 3")
        result = mycursor.fetchall()
        recipies = []
        for row in result:
            recipies.append(Recipe(row[0], row[1], row[3]))
        return recipies
