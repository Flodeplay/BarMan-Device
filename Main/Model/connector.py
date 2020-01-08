import mysql.connector
from Main.Model.Class.profile import Profile
from Main.Model.Class.liquidsforbeverages import Liquidforbeverage
from Main.Model.Class.user import User
from Main.Model.Class.device import Device
from Main.Model.Class.beverage import Beverage
from Main.Model.Class.pump import Pump
import logging


class Connector:

    def __init__(self, key):
        try:
            self.conn = mysql.connector.connect(
                host="e67103-mysql.services.easyname.eu",
                user="u100372db2",
                passwd=".2m4f3f9431s",
                database="u100372db2"
            )

            if self.conn and self.conn.is_connected():
                logging.info("Connection to DB established")
                self.connected = True
                self.key = key
            else:
                self.connected = False
        except:
            self.connected = False
            logging.warning("Connection to DB could not be established")

    def set_pin(self,pin):
        self.conn.connect()
        mycursor = self.conn.cursor()
        mycursor.execute(
            "UPDATE d_devices SET d_pin = "+pin+" WHERE d_key = "+self.device.key+";")
        mycursor.close()
        self.conn.close()

    def getdevice(self):
        self.conn.connect()
        mycursor = self.conn.cursor()
        mycursor.execute(
            "SELECT d_key,d_pin,d_ipaddress,d_u_id,d_p_id FROM d_devices WHERE d_key = " + str(self.key) + " Limit 1;")
        result = mycursor.fetchone()
        if mycursor.rowcount == 0 or mycursor.rowcount > 1:
            mycursor.close()
            self.conn.close()
            raise ValueError(mycursor.rowcount)
        else:
            self.device = Device(result[0], result[1], result[2], result[3], result[4])
            mycursor.close()
            self.conn.close()
            return self.device

    def getuser(self):
        self.conn.connect()
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT u_id,u_forename FROM u_users WHERE u_id = " + str(self.device.userid) + " Limit 1;")
        if not mycursor.rowcount == 0 or mycursor.rowcount > 1:
            result = mycursor.fetchone()
            mycursor.close()
            self.conn.close()
            return User(result[0], result[1])
        else:
            mycursor.close()
            self.conn.close()
            return None

    def getprofile(self):
        self.conn.connect()
        mycursor = self.conn.cursor()
        mycursor.execute(
            "SELECT p_id,p_title FROM p_profiles WHERE p_id = " + str(self.device.userprofile) + " Limit 1;")
        if not mycursor.rowcount == 0 or mycursor.rowcount > 1:
            result = mycursor.fetchone()
            mycursor.close()
            self.conn.close()
            return Profile(result[0], result[1], self.getbeverages(result[0]))
        else:
            mycursor.close()
            self.conn.close()
            return None

    def getbeverages(self, p_id):
        self.conn.connect()
        mycursor = self.conn.cursor()
        mycursor.execute("select bb.b_id,bb.b_name from pb_profilebeverages inner join b_beverages bb on"
                         + " pb_profilebeverages.pb_b_id = bb.b_id where pb_p_id =" + str(p_id))
        result = mycursor.fetchall()
        beverages = []
        for row in result:
            beverages.append(Beverage(row[1], self.getpumpsforbeverages(row[0])))
        mycursor.close()
        self.conn.close()
        return beverages

    def getpumpsforbeverages(self, b_id):
        self.conn.connect()
        mycursor = self.conn.cursor()
        mycursor.execute("select ll.l_containerNo,ll.l_name,bl_liquid_volumen from bl_beverageliquids"
                         + " inner join l_liquids ll on bl_beverageliquids.bl_l_id = ll.l_id"
                         + " where bl_b_id =" + str(b_id))
        result = mycursor.fetchall()
        pumps = []
        for row in result:
            pumps.append(Liquidforbeverage(row[0], row[1], row[2]))
        mycursor.close()
        self.conn.close()
        return pumps

    def getpumpconfiguration(self):
        self.conn.connect()
        mycursor = self.conn.cursor()
        mycursor.execute("SELECT l_containerNo, l_name FROM p_profiles"
                            + " INNER JOIN pb_profilebeverages pb on p_profiles.p_id = pb.pb_p_id"
                            + " INNER JOIN bl_beverageliquids bl on pb.pb_b_id = bl.bl_b_id"
                            + " INNER JOIN l_liquids ll on bl.bl_l_id = ll.l_id"
                        + " WHERE p_id = 1"
                        + " GROUP BY l_containerNo"
                        + " ORDER BY l_containerNo DESC")
        result = mycursor.fetchall()
        pumps = []
        for row in result:
            pumps.append(Pump(row[0], row[1]))
        mycursor.close()
        self.conn.close()
        return pumps
