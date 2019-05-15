import pyodbc
from datetime import datetime

import NetHolesClass
import TankClass
import UserClass
import WaterQualityClass
from array import *


class Database:
    def __init__(self):
        self.server = 'mia-robotics.database.windows.net'
        self.database = 'Aquaculture'
        self.username = 'miaRobotics'
        self.password = 'jungleBoogie123'
        self.driver= '{ODBC Driver 17 for SQL Server}'
        self.cnxn = pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursor = self.cnxn.cursor()


    #checks if user exists in database and returns user object or return None
    def authenticateLogIn(self, username, password):
        userID = self.searchUser(username,password)
        if userID == None:
            return None
        else:
            return self.loadUser(userID)

    #checks if user exists in database and returns user object or return None
    def authenticatePerson(self, faceID):
        userID = self.searchUserFaceID(faceID)
        if userID == None:
            return None
        else:
            return self.loadUser(userID)

    #searches for user in database and if it exists returns its ID
    def searchUser(self, username, password):
        tsql = "SELECT * FROM [User] WHERE username = ? AND password = ?"
        self.cursor.execute(tsql, username, password)
        result_set = self.cursor.fetchall()
        if len(result_set):
            return result_set[0][0]
        else:
            return None

    #searches for user in database and if it exists returns its ID
    def searchUserFaceID(self, faceID):
        tsql = "SELECT * FROM [User] WHERE faceId = ?"
        self.cursor.execute(tsql, faceID)
        result_set = self.cursor.fetchall()
        if len(result_set):
            return result_set[0][0]
        else:
            return None

    def validateUsername(self, username):
        """
        takes username and verifies that it doesn't exist in the database
        if it exists returns false and if it doesn't returns true
        """
        tsql = "SELECT * FROM [User] WHERE username = ?"
        self.cursor.execute(tsql, username)
        result_set = self.cursor.fetchall()
        if len(result_set): #if username exists
            return False
        else:
            return True

    #loads user data from database and returns user object
    def loadUser(self, userID):
        print("LOADING User >>>>>>>>>>>>")
        tsql = "SELECT * FROM [User] WHERE userID = ?"
        self.cursor.execute(tsql, userID)
        result_set = self.cursor.fetchall()
        print( len(result_set))
        row = result_set[0]
        print("Id = ", row[0])
        print("Username = ", row[1])
        print("Password = ", row[2])
        print("FirstName  = ", row[3])
        print("Lastname = ", row[4])
        print("email = " , row[5])
        print("faceID = ", row[6] )
        print("reportLink = ", row[7])
        username =  row[1]
        password =  row[2]
        firstName  =  row[3]
        lastName =  row[4]
        email = row[5]
        faceID = row[6]
        reportLink = row[7]
        tankList = self.loadTankList(userID)
        user = UserClass.User(firstName,lastName,username,password,email,faceID,reportLink,userID,tankList)
        return user

    #load tanks list and returns it
    def loadTankList(self, userID):
        print("LOADING TANK >>>>>>>>>>>>")
        tsql = "SELECT * FROM Tanks WHERE userID = ?"
        self.cursor.execute(tsql, userID)
        result_set = self.cursor.fetchall()
        tankList = []
        print(len(result_set))
        if len(result_set) == 0:
            return None

        for row in result_set:
            print("fishtype = ", row[0])
            # print("feedingSchedule = ", row[1])
            # print("userID = ", row[2])
            # print("tankID  = ", row[3])
            # print("waterSalinityUpperThresh = ", row[4])
            # print("waterSalinityLowerThresh = ", row[5])
            # print("tempLowerThresh = ", row[6])
            # print("tempUpperThresh = ", row[7])
            # print("pHLowerThresh = ", row[8])
            # print("pHUpperThresh = ", row[9])
            # print("harvestDate  = ", row[10])
            # print("needsCleaning  = ", row[11])
            # print("needsFixing  = ", row[12])
            fishType = row[0]
            feedingSchedule = row[1]
            tankID = row[3]
            waterSalinityUpperThresh =  row[4]
            waterSalinityLowerThresh = row[5]
            tempLowerThresh =  row[6]
            tempUpperThresh =  row[7]
            pHLowerThresh = row[8]
            pHUpperThresh = row[9]
            harvestDate = row[10]
            needsCleaning = row[11]
            needsFixing = row[12]
            waterQualityList = self.loadWaterQualityList(tankID)
            netHolesList = self.loadNetHolesList(tankID)
            tank = TankClass.Tank(tankID,fishType,feedingSchedule,waterSalinityUpperThresh,waterSalinityLowerThresh,
                                  tempUpperThresh,tempLowerThresh,pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing,waterQualityList,netHolesList)
            tankList.append(tank)

        return tankList

    # load water quality list and returns it
    def loadWaterQualityList(self, tankID):
        print("LOADING WATER QUALITY >>>>>>>>>>>>")
        tsql = "SELECT * FROM Water_Quality WHERE tankID = ?"
        self.cursor.execute(tsql, tankID)
        result_set = self.cursor.fetchall()
        waterQualityList = []
        if len(result_set) == 0:
            return None
        for row in result_set:
            # print("tankID = ", row[0])
            # print("time = ", row[1])
            # print("date = ", row[2])
            # print("pH  = ", row[3])
            # print("temp  = ", row[4])
            # print("waterQualityLevel = ", row[5])
            time = row[1]
            date = row[2]
            pH = row[3]
            temp = row[4]
            waterQualityLevel = row[5]
            waterQuality = WaterQualityClass.waterQuality(date,time,pH,temp,waterQualityLevel)
            waterQualityList.append(waterQuality)

        return waterQualityList

        # load net holes list
    def loadNetHolesList(self, tankID):
        print("LOADING NetHoles >>>>>>>>>>>>")
        tsql = "SELECT * FROM Holes WHERE tankID = ?"
        self.cursor.execute(tsql, tankID)
        result_set = self.cursor.fetchall()
        holesList = []
        print("ENTRIES = ")
        print(len(result_set))
        if len(result_set) == 0:
            return None

        for row in result_set:
            # print("tankID = ", row[0])
            # print("holesCoord = ", row[1])
            # print("date = ", row[2])
            # print("time  = ", row[3])
            holesCoord = row[1]
            date = row[2]
            time = row[3]
            holeEntry = NetHolesClass.netHoles(holesCoord,date,time)
            holesList.append(holeEntry)

        return holesList

    #take objects as parameter and adds new entry in database
    #returns
    def addNewUser(self, user):
        """
        Takes user object as parameter and adds new entry in database
        returns true if the user was added to the database/ false if it's not added
        """
        if(self.validateUsername(user.username)):
            print ('Inserting a new row into User Table')
            #Insert Query
            tsql = "INSERT INTO [User] (username, password, firstName, lastName, email, faceID, reportLink) VALUES (?,?,?,?,?,?,?);"
            with self.cursor.execute(tsql, user.username, user.password, user.firstName, user.lastName, user.email,user.faceID,user.reportLink):
                print ('Successfully Inserted!')
            return True
        else:
            print('Username already exists!')
            return False

    def addFaceID(self, user):
        """
        takes user object and sets its face ID
        """
        # UPDATE table SET id = id + 1 WHERE id >= 9
        tsql = "UPDATE [User] SET faceId = ? WHERE userID = ?"
        with self.cursor.execute(tsql, user.getFaceID(), user.getUserID()):
            print('Successfully Inserted Face ID!')
        return None
        # tsql = "INSERT INTO [User] WHERE userID = ? (faceID) VALUES (?)"
        # with self.cursor.execute(tsql, user.getUserID(), user.getFaceID()):
        #     print('Successfully Inserted Face ID!')
        # return None

    def addPowerBiReport(self, user):
        tsql = "INSERT INTO [User] WHERE userID = ? (reportLink) VALUES (?)"
        with self.cursor.execute(tsql, user.getUserID(), user.getReportLink()):
            print('Successfully Inserted!')
        return None

    #take objects as parameter and adds new entry in database
    def addNewTank(self, tank, user):
        print ('Inserting a new row into Tank Table')
        #Insert Query
        tsql = "INSERT INTO Tanks (userID, fishType, feedingSchedule, waterSalinityUpperThresh,waterSalinityLowerThresh," \
               "tempLowerThresh, tempUpperThresh, pHLowerThresh, pHUpperThresh, harvest_date, needsCleaning, needsFixing) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"
        with self.cursor.execute(tsql, user.getUserID(), tank.typeOfFish,tank.feedingSchedule, tank.waterSalinityUpperThresh,tank.waterSalinityLowerThresh,
        tank.tempLowerThresh, tank.tempUpperThresh,tank.pHLowerThresh,tank.pHUpperThresh,tank.harvestDate, tank.needsCleaning,tank.needsFixing):
            print ('Successfully Inserted!')
        return None

    #take objects as parameter and adds new entry in database
    def addNewWaterQuality(self, waterQuality, tank):
        print ('Inserting a new row into Water_Quality Table')
        #Insert Query
        tsql = "INSERT INTO Water_Quality (tankID, time, date, pH, temperature, water_salinity) VALUES (?,?,?,?,?,?);"
        with self.cursor.execute(tsql,tank.tankID, waterQuality.time, waterQuality.date, waterQuality.pH, waterQuality.temperature
        , waterQuality.waterSalinity):
            print ('Successfully Inserted!')
        return None

    # take objects as parameter and adds new entry in database
    def addNewNetHoleEntry(self, netHoles,tank):
        print('Inserting a new row Holes Table')
         # Insert Query
        tsql = "INSERT INTO Holes (tankID,holeCoordinates, date, time) VALUES (?,?,?,?);"
        with self.cursor.execute(tsql,tank.tankID, netHoles.holesCoord, netHoles.date, netHoles.time):
            print('Successfully Inserted!')
        return None

    # take objects as parameter and delete entry in database
    def deleteUser(self, user):
        print ('Deleting user', user.getUserID())
        tsql = "DELETE FROM [User] WHERE userID = ?"
        with self.cursor.execute(tsql, user.getUserID()):
            print ('Successfully Deleted!')
        return None

    # take objects as parameter and delete entry in database
    def deleteTank(self, tank):
        print ('Deleting tank', tank.getTankID())
        tsql = "DELETE FROM Tanks WHERE tankID = ?"
        with self.cursor.execute(tsql, tank.getTankID()):
            print ('Successfully Deleted!')
        return None

    def deleteWaterQuality(self, tankID):
        print ('Deleting water quality entry', tankID)
        tsql = "DELETE FROM Water_Quality WHERE tankID = ?"
        with self.cursor.execute(tsql, tankID):
            print ('Successfully Deleted!')
        return None

    def deleteNetHole(self, tankID):
        print ('Deleting water quality entry', tankID)
        tsql = "DELETE FROM Holes WHERE tankID = ?"
        with self.cursor.execute(tsql, tankID):
            print ('Successfully Deleted!')
        return None

    def deleteAllUserData(self, userID):
        print(userID)
        user = self.loadUser(userID)

        for tank in user.getTankList():
            self.deleteWaterQuality( tank.tankID)
            self.deleteNetHole(tank.tankID)
            self.deleteTank(tank)

        self.deleteUser(user)

    def printUsers(self):
        tsql = "SELECT * FROM [User]"
        self.cursor.execute(tsql)
        result_set = self.cursor.fetchall()
        print( str(len(result_set)) + " Entry in Database")
        for row in result_set:
            self.loadUser(row[0])
        return result_set;


    def getData(self,username,password):
        userID = self.searchUser(username, password)
        tsql = "SELECT * FROM Tanks WHERE userID = ?"
        self.cursor.execute(tsql, userID)
        result_set: array = self.cursor.fetchall()

        for row in result_set:
            tsql = "SELECT * FROM Water_Quality WHERE tankID = ?"
            if(len(row)<3):
                break
            self.cursor.execute(tsql, row[3])
            result_set2: array = (self.cursor.fetchall())

        return [result_set,result_set2];
