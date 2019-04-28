import TankClass


class User:
    # userTankList: TankClass

    def __init__(self, firstName, lastName ,username, password, userID, userTankList):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.userID = userID
        self.userTankList = userTankList

    def getFirstName(self):
        '''a function that returns user's first name'''
        return self.firstName

    def getLastName(self):
        '''a function that returns user's last name'''
        return self.lastName

    def getUserID(self):
        '''a function that returns user ID'''
        return self.userID

    def creatTank(self, tankID, typeOfFish, waterQualityThresh, tempUpperThresh, tempLowerThresh):
        '''a function that appends a tank object to the user's tanks list
        and returns this newly created object'''
        newTank = TankClass.Tank(tankID, typeOfFish, waterQualityThresh, tempUpperThresh, tempLowerThresh)
        self.userTankList.append(newTank)
        return newTank

    def getTankList(self):
        '''a function that returns a list of the user's tanks'''
        return self.userTankList

    def removeTank(self, tankID):
        '''a function that checks if the tank id exists and removes it
        returns 0 when the tank removal is successfull
        returns 1 when the tank doesn't exist'''
        tankIndex = -1
        for tank in range(0, len(self.userTankList)):
            if(self.userTankList[i].tankID) == tankID:
                tankIndex = tank
            else:
                tankIndex = -1
        if(tankIndex != -1):
            self.userTankList.remove()
            return 0
        else:
            return 1

    def getWaterQualityHistory(self):
        '''a function that returns a full list of
        all the user's tanks' water quality entries'''
        userWaterQualityHistory = []
        for tank in range(0, len(self.userTankList)):
            for entry in range (0, self.userTankList[tank].numOfWaterQualityEntries):
                userWaterQualityHistory.append(self.userTankList[tank].getWaterQualityHistory)
        return userWaterQualityHistory
