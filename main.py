from ExportToExcel import ExcelConverter
from notify import emailNotifier

filePath = ExcelConverter.getFilePath(ExcelConverter,'abdullah','1234')
emailNotifier('rowan.hisham133@gmail.com','rowan.hisham133@gmail.com').sendEmail('test','test',filePath,'excelFile.csv')