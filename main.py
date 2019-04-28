#import CameraClass
import UserClass
import TankClass
import datetime
import pyodbc
# camera = CameraClass.Camera() #Object from camera Class
import WaterQualityClass
from DatabaseClass import Database

wQ = WaterQualityClass.waterQuality(datetime.datetime.now(), 1, 20, 0.5)
wQlist = []
wQlist.append(wQ)
tank = TankClass.Tank("1","a",2,1,3, wQlist)
tanklist = []
tanklist.append(tank)

print("water quality list = " + str(len(tank.getWaterQualityHistory())))
user = UserClass.User("mah","elkara","mahmou","1111","6", tanklist)
print("tank list = " + str(len(user.getTankList())))


#Opening webCam
# camera.openWebCam()
#Opening RovCamera
# camera.openRovCamera()

print(user.getFirstName())
print(user.getLastName())
print(user.getUserID())

tk = TankClass.Tank(5, "a", 10, 20, 30, 5)

db = Database()

# db.addNewUser(user)
db.addNewTank(tk, user)
# db.deleteUser(user)

# server = 'mia-robotics.database.windows.net'
# database = 'Aquaculture'
# username = 'miaRobotics'
# password = 'jungleBoogie123'
# driver= '{ODBC Driver 17 for SQL Server}'
# cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()
#
# print ('Reading data from table')
# tsql = "SELECT username FROM [User];"
# with cursor.execute(tsql):
#     row = cursor.fetchone()
#     while row:
#         print (str(row[0]))
#         row = cursor.fetchone()

# print(user.getTankList())
