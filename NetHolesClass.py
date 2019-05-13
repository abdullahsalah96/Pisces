class netHoles:
    def __init__(self, holesCoord, date, time):
        self.holesCoord = holesCoord
        self.date = date
        self.time = time

    def getHoleCoord(self):
        return str(self.holesCoord)
