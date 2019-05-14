import WaterQualityClass
from WaterQualityClass import waterQuality
import datetime
class Tank:
    def __init__(self, tankID, typeOfFish,feedingSchedule, waterSalinityUpperThresh,waterSalinityLowerThresh, tempUpperThresh, tempLowerThresh,
                 pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing, waterQualityHistory, holesList):
        self.tankID = tankID
        self.typeOfFish = typeOfFish
        self.feedingSchedule = feedingSchedule
        self.waterSalinityUpperThresh = waterSalinityUpperThresh
        self.waterSalinityLowerThresh = waterSalinityLowerThresh
        self.tempUpperThresh = tempUpperThresh
        self.tempLowerThresh = tempLowerThresh
        self.pHUpperThresh = pHUpperThresh
        self.pHLowerThresh = pHLowerThresh
        self.harvestDate = harvestDate
        self.needsCleaning = needsCleaning
        self.needsFixing = needsFixing
        self.waterQualityHistory = waterQualityHistory
        self.holesList = holesList

    def getTankID(self):
        '''a function that returns tank ID'''
        return self.tankID


    def getFishType(self):
        '''a function that returns tank's type of fish'''
        return self.typeOfFish

    def getHarvestDate(self):
        return str(self.harvestDate)

    def getFeedingSchedule(self):
        return str(self.feedingSchedule)

    def getPipeState(self):
        return self.needsFixing

    def getFishnetState(self):
        return self.needsCleaning

    def getWaterQualityHistory(self):
        return self.waterQualityHistory

    def getNetHolesList(self):
        return self.holesList

    def checkWaterSalinity(self, waterSalinity):
        '''a function that returns true if the water quality level is above the specified threshold'''
        if(waterSalinity < self.waterSalinityUpperThresh and waterSalinity > self.waterSalinityLowerThresh  ):
            return True
        else:
            return False

    def checkTemp(self, temp):
        '''a function that returns true if the temperature is within the specified threshold'''
        if(temp > self.tempLowerThresh and temp < self.tempUpperThresh):
            return True
        else:
            return False

    def checkpH(self, pH):
        '''a function that returns true if the pH is within the specified threshold'''
        if(pH > self.pHLowerThresh and pH < self.pHUpperThresh):
            return True
        else:
            return False

    def addWaterQualityEntry(self, date, pH, temperature,waterSalinity):
        '''a function that add an entry to getting water quality and appends it to the history list'''
        waterQEntry = waterQuality(date, pH, temperature,waterSalinity)
        self.waterQualityHistory.append(waterQEntry)

    def getWaterQualityHistory(self):
        '''a function that returns the water quality entries history list'''
        return self.waterQualityHistory
