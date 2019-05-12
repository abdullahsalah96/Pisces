import datetime
import random

import DatabaseClass
import RandomDataGenerator
import UserClass
from DatabaseClass import Database
from ExportToExcel import ExcelConverter
from notify import emailNotifier

# filePath = ExcelConverter.getFilePath(ExcelConverter,'abdullah','1234')
# emailNotifier('rowan.hisham133@gmail.com','rowan.hisham133@gmail.com').sendEmail('test','test',filePath,'excelFile.csv')

database = DatabaseClass.Database()
rdg = RandomDataGenerator.RDG()


user = database.authenticateLogIn('rowan','1234')
print(user.userID)