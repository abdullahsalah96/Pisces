import datetime
import random

import NetHolesClass
import TankClass
import UserClass
import WaterQualityClass


class RDG:

    def __init__(self):
        self.FirstNameList = ['Len', 'Shantay', 'Earnestine', 'Alexis', 'Alvin', 'Amanda', 'Hermila', 'Hollie', 'Annabelle',
                         'Anjelica', 'Courtney', 'Jeniffer', 'Marvis', 'Madelaine', 'Edwin', 'Sharleen', 'Syreeta',
                         'Minna', 'Marcell']

        self.LastNameList = ['Geoffrey', 'Seymour', 'Dannie', 'Greg', 'Darrick', 'Danny', 'Jordon', 'Lonnie', 'Abram',
                        'Jonah',
                        'Margarito', 'Sang', 'Buck', 'Rodrick', 'Mel', 'Will', 'Jeramy', 'Dallas', 'Cletus', 'Jarrett ']

        self.FishTypeList = ['Tuna','Salamon', 'Rainbow Trout', 'Pacific Halibut', 'Mackerel', 'Cod', 'Sardines', 'Herring']

    def createRandomUser(self):
        if self.FirstNameList.__len__() == 0 or self.LastNameList.__len__() == 0:
            return None

        firstName = self.FirstNameList.pop( random.randint(0, self.FirstNameList.__len__()) -1)
        lastName = self.LastNameList.pop(random.randint(0, self.FirstNameList.__len__()) -1)
        username = firstName + str(random.randint(1, 999))
        email = username + '.' + lastName + '@gmail.com'
        password = str(random.randint(1000, 9999))

        user = UserClass.User(firstName,lastName,username,password,email,None,None,None,None)

        return user

    def createRandomTank(self):

        currentDT =  datetime.datetime.now() + datetime.timedelta(hours=  random.randint(0,24))

        feedingSchedule =  currentDT.strftime("%H:%M:%S")

        waterSalinityLowerThresh = random.randint(29,32)
        waterSalinityUpperThresh = random.randint(33,35)

        tempUpperThresh = random.randint(16, 20)
        tempLowerThresh = random.randint(10, 15)

        pHUpperThresh = random.randint(6, 8)
        pHLowerThresh = random.randint(4, 5)

        harvestDate = currentDT.strftime("%Y/%m/%d")

        needsCleaning =  random.randint(1, 2)%2
        needsFixing = random.randint(1, 2)%2

        typeOfFish = self.FishTypeList.pop(random.randint(0, len(self.FishTypeList)) - 1)


        tank = TankClass.Tank(None,typeOfFish,feedingSchedule,waterSalinityUpperThresh,waterSalinityLowerThresh,
                              tempUpperThresh,tempLowerThresh,pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing,None,None)

        return tank

    def createRandomWQ(self):
        currentDT =  datetime.datetime.now() + datetime.timedelta(hours=  random.randint(0,24))
        date = currentDT.strftime("%Y/%m/%d")
        time = currentDT.strftime("%H:%M:%S")
        pH = random.randint(2, 9)
        temperature = random.randint(7, 30)
        waterSalinity = random.randint(25, 40)

        WQ = WaterQualityClass.waterQuality(date,time,pH,temperature,waterSalinity)

        return WQ

    def createRandomNetHole(self):
        currentDT = datetime.datetime.now() + datetime.timedelta(hours=random.randint(0, 24))
        date = currentDT.strftime("%Y/%m/%d")
        time = currentDT.strftime("%H:%M:%S")
        holesCoord =str( str(random.randint(1,60)) + '°' + str(random.randint(1,60)) +'’' + str(random.randint(1,60)) + '″N' + '   ' + str(random.randint(1,60)) + '°' + str(random.randint(1,60)) + '’' + str(random.randint(1,60)) + '″E')
        netHole = NetHolesClass.netHoles(holesCoord,date,time)
        return netHole