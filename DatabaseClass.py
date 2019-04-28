import pyodbc
from datetime import datetime

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


    #searches for user in database and if it exists returns its ID
    def searchUser(self, username, password):
        tsql = "SELECT * FROM [User] WHERE username = ? AND password = ?"
        self.cursor.execute(tsql, username, password)
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
        tsql = "SELECT * FROM [User] WHERE userID = ?"
        self.cursor.execute(tsql, userID)
        result_set = self.cursor.fetchall()
        print( len(result_set))
        row = result_set[0]
        print("Id = ", row[0])
        print("Username = ", row[1])
        print("Password = ", row[2])
        print("FirstName  = ", row[3])
        print("Lastname = ", row[4], "\n")
        username =  row[1]
        password =  row[2]
        firstName  =  row[3]
        lastName =  row[4]
        tankList = self.loadTankList(userID)
        user = UserClass.User(firstName,lastName,username,password,userID,tankList)
        return user

    #load tanks list and returns it
    def loadTankList(self, userID):
        tsql = "SELECT * FROM Tanks WHERE userID = ?"
        self.cursor.execute(tsql, userID)
        result_set = self.cursor.fetchall()
        tankList = []

        print(len(result_set))
        if len(result_set) == 0:
            return None

        for row in result_set:
            print("fishtype = ", row[0])
            print("feedingSchedule = ", row[1])
            print("userID = ", row[2])
            print("tankID  = ", row[3])
            print("waterQualityThresh = ", row[4])
            print("tempLowerThresh = ", row[5])
            print("tempUpperThresh = ", row[6])
            print("harvestDate  = ", row[7] , "\n")
            fishType = row[0]
            feedingSchedule = row[1]
            tankID = row[3]
            waterQualityThresh =  row[4]
            tempLowerThresh =  row[5]
            tempUpperThresh =  row[6]
            harvestDate = row[7]
            waterQualityList = self.loadWaterQualityList(tankID)
            tank = TankClass.Tank(tankID,fishType,waterQualityThresh,tempUpperThresh,tempLowerThresh,waterQualityList)
            tankList.append(tank)

        return tankList

    # load water quality list and returns it
    def loadWaterQualityList(self, tankID):
        tsql = "SELECT * FROM Water_Quality WHERE tankID = ?"
        self.cursor.execute(tsql, tankID)
        result_set = self.cursor.fetchall()
        waterQualityList = []

        if len(result_set) == 0:
            return None

        for row in result_set:
            print("tankID = ", row[0])
            print("time = ", row[1])
            print("date = ", row[2])
            print("pH  = ", row[3])
            print("temp  = ", row[4])
            print("waterQualityLevel = ", row[5])
            time = row[1]
            date = row[2]
            pH = row[3]
            temp = row[4]
            waterQualityLevel = row[5]
            waterQuality = WaterQualityClass.waterQuality(date,time,pH,temp,waterQualityLevel)
            waterQualityList.append(waterQuality)

        return waterQualityList

    #take objects as parameter and adds new entry in database
    #returns
    def addNewUser(self, user):
        """
        Takes user object as parameter and adds new entry in database
        returns true if the user was added to the database/ false if it's not added
        """
        if(validateUsername(user.username)):
            print ('Inserting a new row into User Table')
            #Insert Query
            tsql = "INSERT INTO [User] (username, password, firstName, lastName) VALUES (?,?,?,?);"
            with self.cursor.execute(tsql, user.username, user.password, user.firstName, user.lastName):
                print ('Successfully Inserted!')
            return True
        else:
            print('Username already exists!')
            return False


    #take objects as parameter and adds new entry in database
    def addNewTank(self, tank, user):
        print ('Inserting a new row into Tank Table')
        #Insert Query
        tsql = "INSERT INTO Tanks (userID, fishType, waterQualityThresh, tempLowerThresh, tempUpperThresh) VALUES (?,?,?,?,?);"
        with self.cursor.execute(tsql, user.getUserID(), tank.typeOfFish, tank.waterQualityThresh,
        tank.tempLowerThresh, tank.tempUpperThresh):
            print ('Successfully Inserted!')
        return None

    #take objects as parameter and adds new entry in database
    def addNewWaterQuality(self, waterQuality):
        print ('Inserting a new row into Water_Quality Table')
        time = datetime.now().time()
        date = datetime.now().date()
        #Insert Query
        tsql = "INSERT INTO Water_Quality (time, date, pH, temperature, water_quality) VALUES (?,?,?,?,?);"
        with self.cursor.execute(tsql, time, date, waterQuality.pH, waterQuality.temperature
        , waterQuality.waterQualityLevel):
            print ('Successfully Inserted!')
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
        tsql = "DELETE FROM Tank WHERE tankID = ?"
        with self.cursor.execute(tsql, tank.getTankID()):
            print ('Successfully Deleted!')
        return None

    def deleteWaterQuality(self, waterQuality):
        print ('Deleting water quality entry', waterQuality.waterQualityLevel)
        tsql = "DELETE FROM Water_Quality WHERE water_quality = ?"
        with self.cursor.execute(tsql, waterQuality.waterQualityLevel):
            print ('Successfully Deleted!')
        return None
