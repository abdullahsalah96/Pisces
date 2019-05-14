# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from DatabaseClass import Database
from UserClass import User
from TankClass import Tank
from CameraClass import Camera
from notify import emailNotifier
import cv2
import datetime
import random
from PyQt5.QtCore import QTimer
import photos_rc


class Ui_MainWindow(object):
    db = Database()
    camTimer = QTimer()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 840)
        MainWindow.setStyleSheet("border-image: url(:/Resources/whiteBG.png);")
        MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 873))
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setStyleSheet("border-image: url(:/Resources/signInBG.png);")
        self.page_login.setObjectName("page_login")
        self.button_login = QtWidgets.QPushButton(self.page_login)
        self.button_login.setGeometry(QtCore.QRect(340, 530, 320, 44))
        self.button_login.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/signIn.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/signInPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/signInPressed.png);\n"
"}x")
        self.button_login.setText("")
        self.button_login.setObjectName("button_login")
        self.button_createOne = QtWidgets.QPushButton(self.page_login)
        self.button_createOne.setGeometry(QtCore.QRect(340, 650, 320, 44))
        self.button_createOne.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/signUp.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/signUpPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/signUpPressed.png);\n"
"}x")
        self.button_createOne.setText("")
        self.button_createOne.setObjectName("button_createOne")
        self.lineEdit_username_login = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_username_login.setGeometry(QtCore.QRect(310, 341, 381, 31))
        self.lineEdit_username_login.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(130, 130, 144);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_username_login.setObjectName("lineEdit_username_login")
        self.close_4 = QtWidgets.QPushButton(self.page_login)
        self.close_4.setGeometry(QtCore.QRect(940, 30, 21, 21))
        self.close_4.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/exitGrey.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/exitRed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/exitRed.png);\n"
"}x")
        self.close_4.setText("")
        self.close_4.setObjectName("close_4")
        self.lineEdit_password_login = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_password_login.setGeometry(QtCore.QRect(310, 422, 381, 31))
        self.lineEdit_password_login.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(130, 130, 144);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_login.setObjectName("lineEdit_password_login")
        self.button_login_with_faceID = QtWidgets.QPushButton(self.page_login)
        self.button_login_with_faceID.setGeometry(QtCore.QRect(340, 590, 320, 44))
        self.button_login_with_faceID.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/faceID.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/faceIDClicked.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/faceIDClicked.png);\n"
"}x")
        self.button_login_with_faceID.setText("")
        self.button_login_with_faceID.setObjectName("button_login_with_faceID")
        self.label = QtWidgets.QLabel(self.page_login)
        self.label.setGeometry(QtCore.QRect(390, 290, 241, 31))
        self.label.setStyleSheet("border-image: url(:/Resources/semiDarkBG.png);\n"
"color: rgb(245, 29, 69);\n"
"font: 25 10pt \"Roboto Light\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_login)
        self.page_signup = QtWidgets.QWidget()
        self.page_signup.setStyleSheet("border-image: url(:/Resources/signUpBG.png);")
        self.page_signup.setObjectName("page_signup")
        self.button_signup = QtWidgets.QPushButton(self.page_signup)
        self.button_signup.setGeometry(QtCore.QRect(340, 640, 320, 44))
        self.button_signup.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/signUp.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/signUpPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/signUpPressed.png);\n"
"}x")
        self.button_signup.setText("")
        self.button_signup.setObjectName("button_signup")
        self.close_3 = QtWidgets.QPushButton(self.page_signup)
        self.close_3.setGeometry(QtCore.QRect(940, 30, 21, 21))
        self.close_3.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/exitGrey.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/exitRed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/exitRed.png);\n"
"}x")
        self.close_3.setText("")
        self.close_3.setObjectName("close_3")
        self.lineEdit_firstName = QtWidgets.QLineEdit(self.page_signup)
        self.lineEdit_firstName.setGeometry(QtCore.QRect(310, 327, 151, 31))
        self.lineEdit_firstName.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(130, 130, 144);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.lineEdit_lastName = QtWidgets.QLineEdit(self.page_signup)
        self.lineEdit_lastName.setGeometry(QtCore.QRect(540, 327, 141, 31))
        self.lineEdit_lastName.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(130, 130, 144);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.lineEdit_username_signup = QtWidgets.QLineEdit(self.page_signup)
        self.lineEdit_username_signup.setGeometry(QtCore.QRect(310, 490, 371, 21))
        self.lineEdit_username_signup.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(130, 130, 144);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_username_signup.setObjectName("lineEdit_username_signup")
        self.lineEdit_password_signup = QtWidgets.QLineEdit(self.page_signup)
        self.lineEdit_password_signup.setGeometry(QtCore.QRect(310, 570, 371, 21))
        self.lineEdit_password_signup.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(130, 130, 144);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_password_signup.setObjectName("lineEdit_password_signup")
        self.lineEdit_email_signup = QtWidgets.QLineEdit(self.page_signup)
        self.lineEdit_email_signup.setGeometry(QtCore.QRect(310, 410, 371, 21))
        self.lineEdit_email_signup.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(130, 130, 144);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_email_signup.setObjectName("lineEdit_email_signup")
        self.button_backToSignIn = QtWidgets.QPushButton(self.page_signup)
        self.button_backToSignIn.setGeometry(QtCore.QRect(340, 700, 320, 44))
        self.button_backToSignIn.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/backSignInPressed.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/backSignIn.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/backSignIn.png);\n"
"}x")
        self.button_backToSignIn.setText("")
        self.button_backToSignIn.setObjectName("button_backToSignIn")
        self.stackedWidget.addWidget(self.page_signup)
        self.page_mainPage = QtWidgets.QWidget()
        self.page_mainPage.setStyleSheet("border-image: url(:/Resources/mainWidgetBG.png);")
        self.page_mainPage.setObjectName("page_mainPage")
        self.button_logout = QtWidgets.QPushButton(self.page_mainPage)
        self.button_logout.setGeometry(QtCore.QRect(70, 770, 130, 42))
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
        self.stackedWidget_2.setGeometry(QtCore.QRect(290, 0, 711, 851))
        self.stackedWidget_2.setStyleSheet("border-image: url(:/Resources/CreateBG.png);")
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
        self.comboBox.setGeometry(QtCore.QRect(260, 60, 128, 33))
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
"")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_cleaning_2 = QtWidgets.QLabel(self.page_dashboard)
        self.label_cleaning_2.setGeometry(QtCore.QRect(300, 459, 41, 18))
        self.label_cleaning_2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(245, 29, 69);")
        self.label_cleaning_2.setObjectName("label_cleaning_2")
        self.label_holes_2 = QtWidgets.QLabel(self.page_dashboard)
        self.label_holes_2.setGeometry(QtCore.QRect(300, 411, 31, 18))
        self.label_holes_2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(245, 29, 69);")
        self.label_holes_2.setObjectName("label_holes_2")
        self.label_pipes_2 = QtWidgets.QLabel(self.page_dashboard)
        self.label_pipes_2.setGeometry(QtCore.QRect(300, 505, 41, 18))
        self.label_pipes_2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(245, 29, 69);")
        self.label_pipes_2.setObjectName("label_pipes_2")
        self.button_subscribe = QtWidgets.QPushButton(self.page_dashboard)
        self.button_subscribe.setGeometry(QtCore.QRect(350, 770, 127, 33))
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
        self.button_emailPath.setGeometry(QtCore.QRect(200, 770, 127, 33))
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
        self.label_temp = QtWidgets.QLabel(self.page_dashboard)
        self.label_temp.setGeometry(QtCore.QRect(300, 364, 121, 18))
        self.label_temp.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.label_temp.setObjectName("label_temp")
        self.label_pH = QtWidgets.QLabel(self.page_dashboard)
        self.label_pH.setGeometry(QtCore.QRect(300, 320, 121, 18))
        self.label_pH.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.label_pH.setObjectName("label_pH")
        self.label_feedingSchedule = QtWidgets.QLabel(self.page_dashboard)
        self.label_feedingSchedule.setGeometry(QtCore.QRect(300, 270, 121, 18))
        self.label_feedingSchedule.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.label_feedingSchedule.setObjectName("label_feedingSchedule")
        self.label_harvestDate = QtWidgets.QLabel(self.page_dashboard)
        self.label_harvestDate.setGeometry(QtCore.QRect(300, 220, 121, 18))
        self.label_harvestDate.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.label_harvestDate.setObjectName("label_harvestDate")
        self.label_fishType = QtWidgets.QLabel(self.page_dashboard)
        self.label_fishType.setGeometry(QtCore.QRect(300, 176, 121, 18))
        self.label_fishType.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"font: 25 12pt \"Roboto Light\";\n"
"color: rgb(35, 34, 40);")
        self.label_fishType.setObjectName("label_fishType")
        self.stackedWidget_2.addWidget(self.page_dashboard)
        self.page_analyzeTanks = QtWidgets.QWidget()
        self.page_analyzeTanks.setStyleSheet("border-image: url(:/Resources/AnalyzeBG.png);")
        self.page_analyzeTanks.setObjectName("page_analyzeTanks")
        self.camLabel = QtWidgets.QLabel(self.page_analyzeTanks)
        self.camLabel.setGeometry(QtCore.QRect(91, 205, 533, 260))
        self.camLabel.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);")
        self.camLabel.setText("")
        self.camLabel.setObjectName("camLabel")
        self.close = QtWidgets.QPushButton(self.page_analyzeTanks)
        self.close.setGeometry(QtCore.QRect(640, 20, 21, 21))
        self.close.setStyleSheet("QPushButton{\n"
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
        self.close.setText("")
        self.close.setObjectName("close")
        self.label_holes2 = QtWidgets.QLabel(self.page_analyzeTanks)
        self.label_holes2.setGeometry(QtCore.QRect(310, 600, 101, 21))
        self.label_holes2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"color: rgb(60, 59, 63);\n"
"font: 25 10pt \"Roboto Light\";")
        self.label_holes2.setObjectName("label_holes2")
        self.label_pipe2 = QtWidgets.QLabel(self.page_analyzeTanks)
        self.label_pipe2.setGeometry(QtCore.QRect(310, 692, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_pipe2.setFont(font)
        self.label_pipe2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"color: rgb(60, 59, 63);\n"
"font: 25 10pt \"Roboto Light\";")
        self.label_pipe2.setObjectName("label_pipe2")
        self.label_cleaning2 = QtWidgets.QLabel(self.page_analyzeTanks)
        self.label_cleaning2.setGeometry(QtCore.QRect(310, 645, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_cleaning2.setFont(font)
        self.label_cleaning2.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"color: rgb(60, 59, 63);\n"
"font: 25 10pt \"Roboto Light\";")
        self.label_cleaning2.setObjectName("label_cleaning2")
        self.button_cleaning_2 = QtWidgets.QPushButton(self.page_analyzeTanks)
        self.button_cleaning_2.setGeometry(QtCore.QRect(283, 520, 127, 33))
        self.button_cleaning_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/Cleaning.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/CleaningPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/CleaningPressed.png);\n"
"}x")
        self.button_cleaning_2.setText("")
        self.button_cleaning_2.setObjectName("button_cleaning_2")
        self.button_holes_2 = QtWidgets.QPushButton(self.page_analyzeTanks)
        self.button_holes_2.setGeometry(QtCore.QRect(140, 520, 127, 33))
        self.button_holes_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/Holes.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/HolesPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/HolesPressed.png);\n"
"}x")
        self.button_holes_2.setText("")
        self.button_holes_2.setObjectName("button_holes_2")
        self.button_pipe_2 = QtWidgets.QPushButton(self.page_analyzeTanks)
        self.button_pipe_2.setGeometry(QtCore.QRect(430, 520, 127, 33))
        self.button_pipe_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/Pipes.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/PipesPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/PipesPressed.png);\n"
"}x")
        self.button_pipe_2.setText("")
        self.button_pipe_2.setObjectName("button_pipe_2")
        self.button_pipe_3 = QtWidgets.QPushButton(self.page_analyzeTanks)
        self.button_pipe_3.setGeometry(QtCore.QRect(438, 642, 222, 34))
        self.button_pipe_3.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/predict.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/predictPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/predictPressed.png);\n"
"}x")
        self.button_pipe_3.setText("")
        self.button_pipe_3.setObjectName("button_pipe_3")
        self.lineEdit_temp = QtWidgets.QLineEdit(self.page_analyzeTanks)
        self.lineEdit_temp.setGeometry(QtCore.QRect(575, 600, 101, 22))
        self.lineEdit_temp.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"color: rgb(60, 59, 63);\n"
"font: 25 10pt \"Roboto Light\";")
        self.lineEdit_temp.setObjectName("lineEdit_temp")
        self.label_waterSalinity = QtWidgets.QLabel(self.page_analyzeTanks)
        self.label_waterSalinity.setGeometry(QtCore.QRect(580, 692, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_waterSalinity.setFont(font)
        self.label_waterSalinity.setStyleSheet("border-image: url(:/Resources/whiteBG.png);\n"
"color: rgb(60, 59, 63);\n"
"font: 25 10pt \"Roboto Light\";")
        self.label_waterSalinity.setObjectName("label_waterSalinity")
        self.stackedWidget_2.addWidget(self.page_analyzeTanks)
        self.page_createTank = QtWidgets.QWidget()
        self.page_createTank.setObjectName("page_createTank")
        self.button_main_create = QtWidgets.QPushButton(self.page_createTank)
        self.button_main_create.setGeometry(QtCore.QRect(250, 775, 127, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_main_create.setFont(font)
        self.button_main_create.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Resources/createButton.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/createButtonPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/createButtonPressed.png);\n"
"}x")
        self.button_main_create.setText("")
        self.button_main_create.setObjectName("button_main_create")
        self.close_2 = QtWidgets.QPushButton(self.page_createTank)
        self.close_2.setGeometry(QtCore.QRect(640, 20, 21, 21))
        self.close_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/exitWhiteBlue.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/black_blue.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/black_blue.png);\n"
"}x")
        self.close_2.setText("")
        self.close_2.setObjectName("close_2")
        self.lineEdit_fishType_create = QtWidgets.QLineEdit(self.page_createTank)
        self.lineEdit_fishType_create.setGeometry(QtCore.QRect(430, 488, 161, 21))
        self.lineEdit_fishType_create.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(198, 198, 199);\n"
"font: 25 10pt \"Roboto Light\";\n"
"")
        self.lineEdit_fishType_create.setObjectName("lineEdit_fishType_create")
        self.lineEdit_feedingSchedule = QtWidgets.QLineEdit(self.page_createTank)
        self.lineEdit_feedingSchedule.setGeometry(QtCore.QRect(430, 584, 161, 21))
        self.lineEdit_feedingSchedule.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(198, 198, 199);\n"
"font: 25 10pt \"Roboto Light\";\n"
"")
        self.lineEdit_feedingSchedule.setObjectName("lineEdit_feedingSchedule")
        self.lineEdit_wqThreshold = QtWidgets.QLineEdit(self.page_createTank)
        self.lineEdit_wqThreshold.setGeometry(QtCore.QRect(430, 732, 161, 21))
        self.lineEdit_wqThreshold.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(198, 198, 199);\n"
"font: 25 10pt \"Roboto Light\";\n"
"")
        self.lineEdit_wqThreshold.setObjectName("lineEdit_wqThreshold")
        self.lineEdit_tempLThreshold = QtWidgets.QLineEdit(self.page_createTank)
        self.lineEdit_tempLThreshold.setGeometry(QtCore.QRect(430, 632, 171, 21))
        self.lineEdit_tempLThreshold.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(198, 198, 199);\n"
"font: 25 10pt \"Roboto Light\";\n"
"")
        self.lineEdit_tempLThreshold.setObjectName("lineEdit_tempLThreshold")
        self.lineEdit_tempUThreshold = QtWidgets.QLineEdit(self.page_createTank)
        self.lineEdit_tempUThreshold.setGeometry(QtCore.QRect(430, 682, 161, 21))
        self.lineEdit_tempUThreshold.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(198, 198, 199);\n"
"font: 25 10pt \"Roboto Light\";\n"
"")
        self.lineEdit_tempUThreshold.setObjectName("lineEdit_tempUThreshold")
        self.lineEdit_harvestDate_create = QtWidgets.QLineEdit(self.page_createTank)
        self.lineEdit_harvestDate_create.setGeometry(QtCore.QRect(430, 535, 161, 22))
        self.lineEdit_harvestDate_create.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);\n"
"color: rgb(198, 198, 199);\n"
"font: 25 10pt \"Roboto Light\";\n"
"")
        self.lineEdit_harvestDate_create.setObjectName("lineEdit_harvestDate_create")
        self.stackedWidget_2.addWidget(self.page_createTank)
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setStyleSheet("border-image: url(:/Resources/whiteBG.png);")
        self.page_settings.setObjectName("page_settings")
        self.button_open_cam = QtWidgets.QPushButton(self.page_settings)
        self.button_open_cam.setGeometry(QtCore.QRect(200, 550, 127, 33))
        self.button_open_cam.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/openCam.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/openCamPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/openCamPressed.png);\n"
"}x")
        self.button_open_cam.setText("")
        self.button_open_cam.setObjectName("button_open_cam")
        self.button_capture = QtWidgets.QPushButton(self.page_settings)
        self.button_capture.setGeometry(QtCore.QRect(340, 550, 127, 33))
        self.button_capture.setStyleSheet("QPushButton{\n"
"border-image: url(:/Resources/capture.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/Resources/capturePressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-image: url(:/Resources/capturePressed.png);\n"
"}x")
        self.button_capture.setText("")
        self.button_capture.setObjectName("button_capture")
        self.camLabel_2 = QtWidgets.QLabel(self.page_settings)
        self.camLabel_2.setGeometry(QtCore.QRect(70, 250, 533, 260))
        self.camLabel_2.setStyleSheet("border-image: url(:/Resources/darkBlackBG.png);")
        self.camLabel_2.setText("")
        self.camLabel_2.setObjectName("camLabel_2")
        self.stackedWidget_2.addWidget(self.page_settings)
        self.label_displayName_2 = QtWidgets.QLabel(self.page_mainPage)
        self.label_displayName_2.setGeometry(QtCore.QRect(47, 137, 41, 31))
        self.label_displayName_2.setStyleSheet("border-image: url(:/Resources/greyBG.png);\n"
"color: rgb(60, 59, 63);\n"
"font: 25 25pt \"Roboto\";")
        self.label_displayName_2.setObjectName("label_displayName_2")
        self.button_dashboard = QtWidgets.QPushButton(self.page_mainPage)
        self.button_dashboard.setGeometry(QtCore.QRect(0, 220, 290, 54))
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
        self.button_createTank.setGeometry(QtCore.QRect(0, 280, 290, 54))
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
        self.button_analyzeTanks.setGeometry(QtCore.QRect(0, 340, 290, 54))
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
        self.button_settings.setGeometry(QtCore.QRect(0, 400, 290, 54))
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

        self.buttonsConnections()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.close_button1.clicked.connect(MainWindow.close)
        self.close_2.clicked.connect(MainWindow.close)
        self.close_3.clicked.connect(MainWindow.close)
        self.close_4.clicked.connect(MainWindow.close)
        self.close.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_username_login.setText(_translate("MainWindow", "Username"))
        self.lineEdit_password_login.setText(_translate("MainWindow", "Password"))
        self.lineEdit_firstName.setText(_translate("MainWindow", "First Name"))
        self.lineEdit_lastName.setText(_translate("MainWindow", "Last Name"))
        self.lineEdit_username_signup.setText(_translate("MainWindow", "Username"))
        self.lineEdit_password_signup.setText(_translate("MainWindow", "Password"))
        self.lineEdit_email_signup.setText(_translate("MainWindow", "Email"))
        self.label_displayName.setText(_translate("MainWindow", "Abdullah Elsheikh"))
        self.comboBox.setProperty("currentText", _translate("MainWindow", "Tank 1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Tank 1"))
        self.label_cleaning_2.setText(_translate("MainWindow", "Yes"))
        self.label_holes_2.setText(_translate("MainWindow", "1"))
        self.label_pipes_2.setText(_translate("MainWindow", "Yes"))
        self.label_temp.setText(_translate("MainWindow", "22"))
        self.label_pH.setText(_translate("MainWindow", "6.2"))
        self.label_feedingSchedule.setText(_translate("MainWindow", "6:00:00"))
        self.label_harvestDate.setText(_translate("MainWindow", "2019/8/12"))
        self.label_fishType.setText(_translate("MainWindow", "Salmon"))
        self.label_holes2.setText(_translate("MainWindow", "No"))
        self.label_pipe2.setText(_translate("MainWindow", "Yes"))
        self.label_cleaning2.setText(_translate("MainWindow", "No"))
        self.lineEdit_temp.setText(_translate("MainWindow", "Enter Temp"))
        self.label_waterSalinity.setText(_translate("MainWindow", "--"))
        self.lineEdit_fishType_create.setText(_translate("MainWindow", "Fish Type"))
        self.lineEdit_feedingSchedule.setText(_translate("MainWindow", "H:M:S"))
        self.lineEdit_wqThreshold.setText(_translate("MainWindow", "0"))
        self.lineEdit_tempLThreshold.setText(_translate("MainWindow", "Celsius"))
        self.lineEdit_tempUThreshold.setText(_translate("MainWindow", "Celsius"))
        self.lineEdit_harvestDate_create.setText(_translate("MainWindow", "YY-MM-DD"))
        self.label_displayName_2.setText(_translate("MainWindow", "A"))
        self.label_displayName_3.setText(_translate("MainWindow", "User"))


    def loginIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(1)
        username_login=self.lineEdit_username_login.text()
        password_login=self.lineEdit_password_login.text()
        self.user = self.db.authenticateLogIn(username_login, password_login)
        if(self.user):
            self.updateDashboard()
            self.camera = Camera(camAddress = 0)
            self.camera.setDaemon(True)
            self.camera.start()
            self.camTimer.timeout.connect(lambda: self.camFeed())
            self.camTimer.start(200)
            self.stackedWidget.setCurrentIndex(2)
            firstName = self.user.getFirstName()
            firstLetter = firstName[0]
            lastName = self.user.getLastName()
            self.label_displayName.setText(firstName + " " + lastName)
            self.label_displayName_2.setText(firstLetter)
        else:
            self.label.setText("Invalid Username or password")

    def updateDashboard(self):
         if(self.user.getTankList() is not None):
             self.tank = self.user.getTankList()
             self.comboBox.clear()
             tanks_list = []
             self.numberOfTanks = len(self.tank)
             print("tanks: ", len(self.tank))
             for num in range(len(self.tank)):
                 tanks_list.append("Tank " + str(num+1))
                 print(self.tank[num].getFishType())
             self.comboBox.addItems(tanks_list)
         else:
             self.label_fishType.setText("-")
             self.label_harvestDate.setText("-")
             self.label_feedingSchedule.setText("-")
             self.label_temp.setText("-")
             self.label_pH.setText("-")
             self.label_holes_2.setText("-")
             self.label_cleaning_2.setText("-")
             self.label_pipes_2.setText("-")


    def loadTankData(self):
         for tankIndex in range(len(self.tank)):
                if (self.comboBox.currentIndex() == tankIndex):
                        WQ = self.user.getTankList()[tankIndex].getWaterQualityHistory()
                        holes = self.user.getTankList()[tankIndex].getNetHolesList()
                        if (holes):
                                self.label_holes_2.setText(str(len(holes)))
                                for i in range(len(holes)):
                                        print(i, holes[i].getHoleCoord())
                        else:
                                self.label_holes_2.setText(str(0))
                        self.label_fishType.setText(self.tank[tankIndex].getFishType())
                        self.label_harvestDate.setText(self.tank[tankIndex].getHarvestDate())
                        self.label_feedingSchedule.setText(self.tank[tankIndex].getFeedingSchedule())
                        if (WQ):
                                self.label_pH.setText(str(WQ[len(WQ) - 1].getpH()))
                                self.label_temp.setText(str(WQ[len(WQ) - 1].getTemp()))
                                self.label_cleaning_2.setText(str(self.tank[tankIndex].getFishnetState()))
                                self.label_pipes_2.setText(str(self.tank[tankIndex].getPipeState()))
                        else:
                                self.label_pH.setText("--")
                                self.label_temp.setText("--")
                                self.label_cleaning_2.setText(str(self.tank[tankIndex].getFishnetState()))
                                self.label_pipes_2.setText(str(self.tank[tankIndex].getPipeState()))



    def createTank(self):
        #change feeding schedule and harvest date
        fishType = self.lineEdit_fishType_create.text()
        feedingSchedule = self.lineEdit_feedingSchedule.text()
        waterQualityThreshold = self.lineEdit_wqThreshold.text()
        temperatureLowerThreshold = self.lineEdit_tempLThreshold.text()
        temperatureUpperThreshold = self.lineEdit_tempUThreshold.text()
        harvestDate = self.lineEdit_harvestDate_create.text()
        currentDT =  datetime.datetime.now() + datetime.timedelta(hours=  random.randint(0,24))
        newTank = Tank(None, fishType, currentDT.strftime("%H:%M:%S"), waterQualityThreshold,
         waterQualityThreshold, temperatureLowerThreshold, temperatureUpperThreshold,
         '20', '20', currentDT.strftime("%Y/%m/%d"), False, False, None, None)
        self.db.addNewTank(newTank, self.user)
        self.updateDashboard()
        self.numberOfTanks=self.numberOfTanks+1


    def sendEmail(self):
       email = "No-Reply@Pisces.com"
       notifier = emailNotifier(email, self.user)
       notifier.sendEmail()

    def camFeed(self):
        """
        a function to show cam feed on cam label
        """
        if(cv2.waitKey == 27): #if the ESC button is pressed
            cv2.destroyAllWindows()
            self.camTimer.stop()
        else:
            #cv2.imshow('frame', self.camera.getFrame())
            frame = self.camera.getFrame()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(img)
            self.camLabel.setScaledContents(True)
            self.camLabel_2.setScaledContents(True)
            self.camLabel.setPixmap(pix)
            self.camLabel_2.setPixmap(pix)

    def createOneIsClicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def signupIsClicked(self):
        firstName = self.lineEdit_firstName.text()
        lastName = self.lineEdit_lastName.text()
        username = self.lineEdit_username_signup.text()
        password = self.lineEdit_password_signup.text()
        email = self.lineEdit_email_signup.text()
        newUser = User(firstName, lastName, username, password, email, None, None, None)
        self.db.addNewUser(newUser)
        self.stackedWidget.setCurrentIndex(0)

    def getBackToLogin(self):
        self.stackedWidget.setCurrentIndex(0)

    def analyzeTanksIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(2)
        print("here")

    def createTankIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(3)

    def settingsIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(4)

    def dashboardIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def getBackToMainPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def updateReadings(self):
        temp=self.lineEdit_temp.text()
        ph=self.lineEdit_ph.text()

    def subscribeIsClicked(self):
        ##open power bi link
        webbrowser.open_new(self.user.reportLink)



    def backToSignIn(self):
        self.stackedWidget.setCurrentIndex(0)

    def buttonsConnections(self):
        self.button_login.clicked.connect(self.loginIsClicked)
        self.button_createOne.clicked.connect(self.createOneIsClicked)
        self.button_signup.clicked.connect(self.signupIsClicked)
        self.button_logout.clicked.connect(self.getBackToLogin)
        self.button_analyzeTanks.clicked.connect(self.analyzeTanksIsClicked)
        self.button_createTank.clicked.connect(self.createTankIsClicked)
        self.button_settings.clicked.connect(self.settingsIsClicked)
        self.button_dashboard.clicked.connect(self.dashboardIsClicked)
        self.button_main_create.clicked.connect(self.createTank)
        self.button_subscribe.clicked.connect(self.subscribeIsClicked)
        self.button_backToSignIn.clicked.connect(self.backToSignIn)
        self.comboBox.currentIndexChanged.connect(self.loadTankData)
        self.button_emailPath.clicked.connect(self.sendEmail)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
