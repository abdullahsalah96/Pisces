import csv
from DatabaseClass import Database

database = Database()

data = database.printUsers()
f = open('outfile','w+')
writer = csv.writer(f)
for row in data:
    writer.writerow(row)

print(data)
