import urllib.request as urllib
import json

class waterQuality:
    def __init__(self, date, time, pH, temperature, waterSalinity):
        self.date = date
        self.time = time
        self.pH = pH
        self.temperature = temperature
        self.waterSalinity = waterSalinity

    def getpH(self):
        return self.pH

    def getTemp(self):
        return self.temperature
