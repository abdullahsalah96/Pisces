import WaterQualityClass
from WaterQualityClass import waterQuality
import datetime
class Tank:
    # waterQualityHistory : WaterQualityClass
    def __init__(self, tankID, typeOfFish, waterQualityThresh, tempUpperThresh, tempLowerThresh, waterQualityHistory):
        self.tankID = tankID
        self.typeOfFish = typeOfFish
        self.waterQualityThresh = waterQualityThresh
        self.tempUpperThresh = tempUpperThresh
        self.tempLowerThresh = tempLowerThresh
        self.waterQualityHistory = waterQualityHistory

    def getTankID(self):
        '''a function that returns tank ID'''
        return self.tankID

    def getFishType(self):
        '''a function that returns tank's type of fish'''
        return self.typeOfFish

    def checkWaterQuality(self, waterQuality):
        '''a function that returns true if the water quality level is above the specified threshold'''
        if(waterQuality > self.waterQualityThresh):
            return True
        else:
            return False

    def checkTemp(self, temp):
        '''a function that returns true if the temperature is within the specified threshold'''
        if(temp > self.tempLowerThresh and temp < self.tempUpperThresh):
            return True
        else:
            return False

    def addWaterQualityEntry(self, date, pH, temperature):
        '''a function that add an entry to getting water quality and appends it to the history list'''
        waterQEntry = waterQuality(date, pH, temperature)
        self.waterQualityHistory.append(waterQEntry)

    def getWaterQualityHistory(self):
        '''a function that returns the water quality entries history list'''
        return self.waterQualityHistory
