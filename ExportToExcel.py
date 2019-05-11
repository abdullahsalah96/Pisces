import csv

from DatabaseClass import Database


class ExcelConverter():

    def getFilePath(self,username,password):

        database = Database()

        data = database.getData(username, password)

        f = open('outfile2.csv', 'w+')
        writer = csv.writer(f)
        for row in data[0]:
            writer.writerow(row)
        for row in data[1]:
            writer.writerow(row)

        return 'outfile2.csv'