import mysql.connector
from Main.Modell.Class.recipe import Recipe
from Main.Modell.Class.pump import Pump
from Main.Modell.Class.user import User
from Main.Modell.Class.device import Device
import logging


class Connector:

    def __init__(self, key):
        try:
            self.conn = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="",
              database="barman"
            )
        except:
            logging.warning("Connection to DB could not be established")

        if self.conn.is_connected():
            logging.info("Connection to DB established")
            self.connected = True
            self.key = key


    def getDevice(self):
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT * FROM d_device WHERE k_key = "+self.key+" Limit 1;")
        result = mycursor.fetchone()
        if mycursor.rowcount == 0 or mycursor.rowcount > 1:
            raise ValueError
        else:
            self.device = Device(result[0], result[1], result[2], result[3])
            return self.device

    def getuser(self):
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT * FROM u_user WHERE u_id = "+str(self.device.curuser)+" Limit 1;")
        result = mycursor.fetchone()
        return User(result[0], result[1])

    def getrecipies(self):
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT * FROM r_recipe WHERE r_u_id = "+self.key+" Limit 5;")
        result = mycursor.fetchall()
        recipies = []
        for row in result:
            recipies.append(Recipe(row[0], row[1], row[3]))
        return recipies
    def getthemeMode(self):
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT k_theme FROM d_device WHERE k_key = "+self.key+" Limit 1;")
        result = mycursor.fetchall()
        return result[0][0]
    def getpumpconfiguration(self):
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT * FROM p_pump WHERE p_device = "+self.key+" ;")
        result = mycursor.fetchall()
        pumps = []
        for row in result:
            pumps.append(Pump(row[1], row[2], row[4]))
        return pumps
