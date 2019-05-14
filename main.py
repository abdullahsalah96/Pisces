import datetime
import random

import DatabaseClass
import RandomDataGenerator
import UserClass
from CameraClass import Camera
from DatabaseClass import Database
from ExportToExcel import ExcelConverter
from notify import emailNotifier

# filePath = ExcelConverter.getFilePath(ExcelConverter,'abdullah','1234')
# emailNotifier('rowan.hisham133@gmail.com','rowan.hisham133@gmail.com').sendEmail('test','test',filePath,'excelFile.csv')

# database = DatabaseClass.Database()
# rdg = RandomDataGenerator.RDG()

cameraThread = Camera(0)
cameraThread.run()

# user = database.authenticateLogIn('rowan','1234')
#
# database.deleteTank(user.getTankList()[3])
#print(user.getTankList()[3].getFishType())
