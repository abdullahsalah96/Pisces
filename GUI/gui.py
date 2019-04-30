# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 870)
        MainWindow.setStyleSheet("border-image: url(:/Resources/whiteBG.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 873))
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.layoutWidget = QtWidgets.QWidget(self.page_login)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 160, 200, 55))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_username = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.verticalLayout.addWidget(self.label_username)
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_username_login = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_username_login.setObjectName("lineEdit_username_login")
        self.verticalLayout_2.addWidget(self.lineEdit_username_login)
        self.lineEdit_password_login = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password_login.setObjectName("lineEdit_password_login")
        self.verticalLayout_2.addWidget(self.lineEdit_password_login)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.button_login = QtWidgets.QPushButton(self.page_login)
        self.button_login.setGeometry(QtCore.QRect(280, 230, 75, 23))
        self.button_login.setObjectName("button_login")
        self.label = QtWidgets.QLabel(self.page_login)
        self.label.setGeometry(QtCore.QRect(250, 290, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")
        self.button_createOne = QtWidgets.QPushButton(self.page_login)
        self.button_createOne.setGeometry(QtCore.QRect(280, 320, 75, 23))
        self.button_createOne.setObjectName("button_createOne")
        self.stackedWidget.addWidget(self.page_login)
        self.page_signup = QtWidgets.QWidget()
        self.page_signup.setObjectName("page_signup")
        self.button_signup = QtWidgets.QPushButton(self.page_signup)
        self.button_signup.setGeometry(QtCore.QRect(280, 280, 75, 23))
        self.button_signup.setObjectName("button_signup")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_signup)
        self.layoutWidget1.setGeometry(QtCore.QRect(200, 120, 231, 142))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_9.addWidget(self.label_20)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_firstName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.verticalLayout_10.addWidget(self.lineEdit_firstName)
        self.lineEdit_lastName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.verticalLayout_10.addWidget(self.lineEdit_lastName)
        self.lineEdit_username_signup = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_username_signup.setObjectName("lineEdit_username_signup")
        self.verticalLayout_10.addWidget(self.lineEdit_username_signup)
        self.lineEdit_password_signup = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_password_signup.setObjectName("lineEdit_password_signup")
        self.verticalLayout_10.addWidget(self.lineEdit_password_signup)
        self.lineEdit_email_signup = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_email_signup.setObjectName("lineEdit_email_signup")
        self.verticalLayout_10.addWidget(self.lineEdit_email_signup)
        self.gridLayout_2.addLayout(self.verticalLayout_10, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_signup)
        self.page_mainPage = QtWidgets.QWidget()
        self.page_mainPage.setStyleSheet("border-image: url(:/Resources/mainWidgetBG.png);")
        self.page_mainPage.setObjectName("page_mainPage")
        self.button_logout = QtWidgets.QPushButton(self.page_mainPage)
        self.button_logout.setGeometry(QtCore.QRect(70, 740, 130, 42))
        self.button_logout.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/logoutPressed.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/logout.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/logout.png);\n"
"}x")
        self.button_logout.setText("")
        self.button_logout.setObjectName("button_logout")
        self.label_displayName = QtWidgets.QLabel(self.page_mainPage)
        self.label_displayName.setGeometry(QtCore.QRect(110, 133, 161, 20))
        self.label_displayName.setStyleSheet("border-image: url(:/Resources/blueBG.png);\n"
"font: 25 12pt \"Roboto\";\n"
"color: rgb(235, 235, 235);")
        self.label_displayName.setObjectName("label_displayName")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_mainPage)
        self.stackedWidget_2.setGeometry(QtCore.QRect(330, 0, 661, 851))
        self.stackedWidget_2.setStyleSheet("")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_blank = QtWidgets.QWidget()
        self.page_blank.setStyleSheet("border-image: url(:/Resources/whiteBG.png);")
        self.page_blank.setObjectName("page_blank")
        self.stackedWidget_2.addWidget(self.page_blank)
        self.page_dashboard = QtWidgets.QWidget()
        self.page_dashboard.setStyleSheet("border-image: url(:/Resources/dashboardWidget.png);")
        self.page_dashboard.setObjectName("page_dashboard")
        self.close_button1 = QtWidgets.QPushButton(self.page_dashboard)
        self.close_button1.setGeometry(QtCore.QRect(640, 20, 21, 21))
        self.close_button1.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/exitBlue.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/exitWhiteBlue.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/exitWhiteBlue.png);\n"
"}x")
        self.close_button1.setText("")
        self.close_button1.setObjectName("close_button1")
        self.comboBox = QtWidgets.QComboBox(self.page_dashboard)
        self.comboBox.setGeometry(QtCore.QRect(230, 60, 128, 33))
        self.comboBox.setStyleSheet("QComboBox {\n"
"border-image: url(:/Resources/comboBoxBG.png);\n"
"    color: black;\n"
"    font: 14px;\n"
"    padding: 1px 0px 1px 3px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    color: red;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}\n"
"\n"
"/* Define a new custom arrow icon for the combo box */\n"
"QComboBox::down-arrow {\n"
"    border-image: url(:/Resources/comboBoxArrow.png);\n"
"    width: 10px;\n"
"    height: 7px;\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.lineEdit_nextFeeding = QtWidgets.QLineEdit(self.page_dashboard)
        self.lineEdit_nextFeeding.setGeometry(QtCore.QRect(270, 270, 100, 18))
        self.lineEdit_nextFeeding.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.lineEdit_nextFeeding.setObjectName("lineEdit_nextFeeding")
        self.lineEdit_fishType_tank = QtWidgets.QLineEdit(self.page_dashboard)
        self.lineEdit_fishType_tank.setGeometry(QtCore.QRect(270, 170, 100, 18))
        self.lineEdit_fishType_tank.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.lineEdit_fishType_tank.setObjectName("lineEdit_fishType_tank")
        self.lineEdit_harvestDate_tank = QtWidgets.QLineEdit(self.page_dashboard)
        self.lineEdit_harvestDate_tank.setGeometry(QtCore.QRect(270, 220, 100, 18))
        self.lineEdit_harvestDate_tank.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.lineEdit_harvestDate_tank.setObjectName("lineEdit_harvestDate_tank")
        self.lineEdit_temp = QtWidgets.QLineEdit(self.page_dashboard)
        self.lineEdit_temp.setGeometry(QtCore.QRect(270, 360, 51, 18))
        self.lineEdit_temp.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.lineEdit_temp.setObjectName("lineEdit_temp")
        self.lineEdit_ph = QtWidgets.QLineEdit(self.page_dashboard)
        self.lineEdit_ph.setGeometry(QtCore.QRect(270, 310, 101, 18))
        self.lineEdit_ph.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.lineEdit_ph.setObjectName("lineEdit_ph")
        self.label_cleaning_2 = QtWidgets.QLabel(self.page_dashboard)
        self.label_cleaning_2.setGeometry(QtCore.QRect(270, 460, 41, 18))
        self.label_cleaning_2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(245, 29, 69);")
        self.label_cleaning_2.setObjectName("label_cleaning_2")
        self.label_holes_2 = QtWidgets.QLabel(self.page_dashboard)
        self.label_holes_2.setGeometry(QtCore.QRect(270, 410, 31, 18))
        self.label_holes_2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(245, 29, 69);")
        self.label_holes_2.setObjectName("label_holes_2")
        self.label_pipes_2 = QtWidgets.QLabel(self.page_dashboard)
        self.label_pipes_2.setGeometry(QtCore.QRect(270, 500, 41, 18))
        self.label_pipes_2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(245, 29, 69);")
        self.label_pipes_2.setObjectName("label_pipes_2")
        self.button_subscribe = QtWidgets.QPushButton(self.page_dashboard)
        self.button_subscribe.setGeometry(QtCore.QRect(340, 790, 127, 33))
        self.button_subscribe.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/subscribe.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/subscribePressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/subscribePressed.png);\n"
"}x")
        self.button_subscribe.setText("")
        self.button_subscribe.setObjectName("button_subscribe")
        self.button_emailPath = QtWidgets.QPushButton(self.page_dashboard)
        self.button_emailPath.setGeometry(QtCore.QRect(190, 790, 127, 33))
        self.button_emailPath.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/EmailButton.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/EmailButtonPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/EmailButtonPressed.png);\n"
"}x")
        self.button_emailPath.setText("")
        self.button_emailPath.setObjectName("button_emailPath")
        self.stackedWidget_2.addWidget(self.page_dashboard)
        self.page_analyzeTanks = QtWidgets.QWidget()
        self.page_analyzeTanks.setObjectName("page_analyzeTanks")
        self.layoutWidget2 = QtWidgets.QWidget(self.page_analyzeTanks)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 120, 281, 102))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.button_cleaning_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_cleaning_2.setObjectName("button_cleaning_2")
        self.verticalLayout_17.addWidget(self.button_cleaning_2)
        self.button_holes_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_holes_2.setObjectName("button_holes_2")
        self.verticalLayout_17.addWidget(self.button_holes_2)
        self.button_pipe_2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_pipe_2.setObjectName("button_pipe_2")
        self.verticalLayout_17.addWidget(self.button_pipe_2)
        self.gridLayout_10.addLayout(self.verticalLayout_17, 0, 0, 1, 1)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_cleaning2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cleaning2.setFont(font)
        self.label_cleaning2.setText("")
        self.label_cleaning2.setObjectName("label_cleaning2")
        self.verticalLayout_18.addWidget(self.label_cleaning2)
        self.label_holes2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_holes2.setText("")
        self.label_holes2.setObjectName("label_holes2")
        self.verticalLayout_18.addWidget(self.label_holes2)
        self.label_pipe2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_pipe2.setFont(font)
        self.label_pipe2.setText("")
        self.label_pipe2.setObjectName("label_pipe2")
        self.verticalLayout_18.addWidget(self.label_pipe2)
        self.gridLayout_10.addLayout(self.verticalLayout_18, 0, 1, 1, 1)
        self.stackedWidget_2.addWidget(self.page_analyzeTanks)
        self.page_createTank = QtWidgets.QWidget()
        self.page_createTank.setObjectName("page_createTank")
        self.button_main_create = QtWidgets.QPushButton(self.page_createTank)
        self.button_main_create.setGeometry(QtCore.QRect(160, 250, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_main_create.setFont(font)
        self.button_main_create.setObjectName("button_main_create")
        self.layoutWidget_7 = QtWidgets.QWidget(self.page_createTank)
        self.layoutWidget_7.setGeometry(QtCore.QRect(60, 50, 319, 171))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_7)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_7.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_7.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_fishType_create = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_fishType_create.setObjectName("lineEdit_fishType_create")
        self.verticalLayout_8.addWidget(self.lineEdit_fishType_create)
        self.lineEdit_feedingSchedule = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_feedingSchedule.setObjectName("lineEdit_feedingSchedule")
        self.verticalLayout_8.addWidget(self.lineEdit_feedingSchedule)
        self.lineEdit_wqThreshold = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_wqThreshold.setObjectName("lineEdit_wqThreshold")
        self.verticalLayout_8.addWidget(self.lineEdit_wqThreshold)
        self.lineEdit_tempLThreshold = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_tempLThreshold.setObjectName("lineEdit_tempLThreshold")
        self.verticalLayout_8.addWidget(self.lineEdit_tempLThreshold)
        self.lineEdit_tempUThreshold = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_tempUThreshold.setObjectName("lineEdit_tempUThreshold")
        self.verticalLayout_8.addWidget(self.lineEdit_tempUThreshold)
        self.lineEdit_harvestDate_create = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_harvestDate_create.setObjectName("lineEdit_harvestDate_create")
        self.verticalLayout_8.addWidget(self.lineEdit_harvestDate_create)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.stackedWidget_2.addWidget(self.page_createTank)
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setStyleSheet("border-image: url(:/Resources/whiteBG.png);")
        self.page_settings.setObjectName("page_settings")
        self.label_8 = QtWidgets.QLabel(self.page_settings)
        self.label_8.setGeometry(QtCore.QRect(190, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget_2.addWidget(self.page_settings)
        self.label_displayName_2 = QtWidgets.QLabel(self.page_mainPage)
        self.label_displayName_2.setGeometry(QtCore.QRect(47, 137, 41, 31))
        self.label_displayName_2.setStyleSheet("border-image: url(:/Resources/greyBG.png);\n"
"color: rgb(60, 59, 63);\n"
"font: 25 25pt \"Roboto\";")
        self.label_displayName_2.setObjectName("label_displayName_2")
        self.button_dashboard = QtWidgets.QPushButton(self.page_mainPage)
        self.button_dashboard.setGeometry(QtCore.QRect(0, 220, 291, 54))
        self.button_dashboard.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/dasboard.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/dashboardPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/dashboardPressed.png);\n"
"}x")
        self.button_dashboard.setText("")
        self.button_dashboard.setObjectName("button_dashboard")
        self.button_createTank = QtWidgets.QPushButton(self.page_mainPage)
        self.button_createTank.setGeometry(QtCore.QRect(0, 280, 291, 54))
        self.button_createTank.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/create.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/createPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/createPressed.png);\n"
"}x")
        self.button_createTank.setText("")
        self.button_createTank.setObjectName("button_createTank")
        self.button_analyzeTanks = QtWidgets.QPushButton(self.page_mainPage)
        self.button_analyzeTanks.setGeometry(QtCore.QRect(0, 340, 291, 54))
        self.button_analyzeTanks.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/analyze.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/analyzePressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/analyzePressed.png);\n"
"}x")
        self.button_analyzeTanks.setText("")
        self.button_analyzeTanks.setObjectName("button_analyzeTanks")
        self.button_settings = QtWidgets.QPushButton(self.page_mainPage)
        self.button_settings.setGeometry(QtCore.QRect(0, 400, 291, 54))
        self.button_settings.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/settings.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/settingsPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/settingsPressed.png);\n"
"}x")
        self.button_settings.setText("")
        self.button_settings.setObjectName("button_settings")
        self.label_displayName_3 = QtWidgets.QLabel(self.page_mainPage)
        self.label_displayName_3.setGeometry(QtCore.QRect(110, 160, 161, 20))
        self.label_displayName_3.setStyleSheet("border-image: url(:/Resources/blueBG.png);\n"
"font: 25 10pt \"Roboto\";\n"
"color: rgb(235, 235, 235);")
        self.label_displayName_3.setObjectName("label_displayName_3")
        self.stackedWidget.addWidget(self.page_mainPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(1)
        self.close_button1.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_username.setText(_translate("MainWindow", "Username :"))
        self.label_password.setText(_translate("MainWindow", "Password :"))
        self.button_login.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Don\'t have an account? "))
        self.button_createOne.setText(_translate("MainWindow", "Create one!"))
        self.button_signup.setText(_translate("MainWindow", "Signup"))
        self.label_2.setText(_translate("MainWindow", "First Name:"))
        self.label_3.setText(_translate("MainWindow", "Last Name:"))
        self.label_4.setText(_translate("MainWindow", "Username:"))
        self.label_5.setText(_translate("MainWindow", "Password:"))
        self.label_20.setText(_translate("MainWindow", "Email Address:"))
        self.label_displayName.setText(_translate("MainWindow", "Abdullah Elsheikh"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Tank 1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Tank 1"))
        self.lineEdit_nextFeeding.setText(_translate("MainWindow", "6:00:00"))
        self.lineEdit_fishType_tank.setText(_translate("MainWindow", "Salmon"))
        self.lineEdit_harvestDate_tank.setText(_translate("MainWindow", "2019/12/4"))
        self.lineEdit_temp.setText(_translate("MainWindow", "22"))
        self.lineEdit_ph.setText(_translate("MainWindow", "6.3"))
        self.label_cleaning_2.setText(_translate("MainWindow", "Yes"))
        self.label_holes_2.setText(_translate("MainWindow", "1"))
        self.label_pipes_2.setText(_translate("MainWindow", "Yes"))
        self.button_cleaning_2.setText(_translate("MainWindow", "Inspect fishnet for cleaning"))
        self.button_holes_2.setText(_translate("MainWindow", "Inspect fishnet holes "))
        self.button_pipe_2.setText(_translate("MainWindow", "Inspect pipe"))
        self.button_main_create.setText(_translate("MainWindow", "Create a Tank!"))
        self.label_14.setText(_translate("MainWindow", "Fish type:"))
        self.label_15.setText(_translate("MainWindow", "Feeding schedule:"))
        self.label_16.setText(_translate("MainWindow", "Water quality threshold:"))
        self.label_17.setText(_translate("MainWindow", "Temperature lower threshold:"))
        self.label_18.setText(_translate("MainWindow", "Temperature upper threshold:"))
        self.label_19.setText(_translate("MainWindow", "Harverst date:"))
        self.label_8.setText(_translate("MainWindow", "Settings"))
        self.label_displayName_2.setText(_translate("MainWindow", "A"))
        self.label_displayName_3.setText(_translate("MainWindow", "User"))

import photos_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

