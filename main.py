from asyncio.windows_events import NULL
import numpy as np
import torch
from torch import nn
from torchvision import transforms, models
import torchvision.models as models
from PIL import Image
import os
import cv2 
import requests
import imutils
import hashlib
import re
from datetime import datetime  

from ast import main
import sys
from unittest import result
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QColor
import mysql.connector as mc

test_dir = 'dataset/test'

conn = mc.connect(
host="localhost",
user="root",
password="",
database="fruitquality")
cur = conn.cursor(buffered=True)

global lab
global pat 


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("UI/welcomeScreen.ui", self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.clicked.connect(self.loginfunction)
        self.userAdminButton.clicked.connect(self.logAdminWelcomePage)
        self.forgotPass.clicked.connect(self.resetPassPage)

    # log into admin welcome page
    def logAdminWelcomePage(self):
        admin = AdminWelcomePage()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def resetPassPage(self):
        reset = ResetPassPage()
        widget.addWidget(reset)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def mainScreen(self):
        mainm = MainScreen()
        widget.addWidget(mainm)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginfunction(self):
        global usern
        usern = self.lineEdit.text()
        passw = self.lineEdit_2.text()
        result = hashlib.md5(passw.encode())
        encryptLoginPass = result.hexdigest()

        if len(usern) == 0 or len(passw) == 0:
            self.error.setText("Please input all fields")
            self.lineEdit.setFocus()

        else:
            query = "SELECT * FROM userlogin WHERE username = '" + \
                usern + "'  AND password = '" + encryptLoginPass + "'"
            cur.execute(query)
            result = cur.fetchone()
            if result != None:
                main = WelcomeScreen()
                main.mainScreen()
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
            else:
                self.error.setText("Invalid username or password")
                self.lineEdit.setFocus()

        return usern

class ResetPassPage(QDialog):
    def __init__(self):
        super(ResetPassPage, self).__init__()
        loadUi("UI/resetPassScreen.ui", self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.backButton.clicked.connect(self.logUserPage)
        self.submitButton.clicked.connect(self.reset)

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def reset(self):
        validate = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = ""
        password = ""
        confirmPass = ""

        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirmPass = self.lineEdit_3.text()


        if len(email) == 0 or len(password) == 0 or len(confirmPass) == 0 :
            self.error.setText("Please input all fields")
            self.lineEdit.setFocus()

        elif password == confirmPass:
            if(re.fullmatch(validate, email)):
                try:
                    cur.execute("SELECT * FROM userlogin where email = '" + email + "'")
                    result = cur.fetchone()

                    if result != None:
                        password = hashlib.md5(password.encode())
                        encryptResetPass = password.hexdigest()
                        try:
                            query = "UPDATE userlogin SET password = '" + encryptResetPass + "' where email = '" + email + "'"
                            cur.execute(query)
                            conn.commit()

                            QMessageBox.information(QMessageBox(),'Successful', 'Password reset successful')

                            wel = AdminWelcomePage()
                            wel.logUserPage()

                        except mc.Error as e:
                            print(e)
                        
                    elif result == None:
                        QMessageBox.information(QMessageBox(),'Error', 'Wrong Email Address!')

                except Exception:
                    QMessageBox.warning(QMessageBox(),'Error', 'Could not reset password.')
            else:
                QMessageBox.warning(QMessageBox(),'Error', 'Email is not valid.')
                self.lineEdit.setFocus()
        else:
            QMessageBox.warning(QMessageBox(),'Error', 'Password not match.')
            self.lineEdit_2.setFocus()

class AdminWelcomePage(QDialog):
    def __init__(self):
        super(AdminWelcomePage, self).__init__()
        loadUi("UI/welcomeScreenAdmin.ui", self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userAdminButton.clicked.connect(self.logUserPage)
        self.loginButton.clicked.connect(self.loginAdminfunction)

    # log into user welcome page
    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # log into admin page (user information)
    def logAdminPage(self):
        lAdminPage = AdminPage()
        widget.addWidget(lAdminPage)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginAdminfunction(self):
        userAd = self.lineEdit.text()
        passAd = self.lineEdit_2.text()

        if len(userAd) == 0 or len(passAd) == 0:
            self.error.setText("Please input all fields")

        else:
            query = "SELECT * FROM adminlogin WHERE adminName = '" + \
                userAd + "'  AND adminPass = '" + passAd + "'"
            cur.execute(query)
            result = cur.fetchone()
            if result != None:
                main = AdminWelcomePage()
                main.logAdminPage()
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
            else:
                self.error.setText("Invalid username or password")
                self.lineEdit.setFocus()

class AdminPage(QDialog):
   def __init__(self):
        super(AdminPage, self).__init__()
        loadUi("UI/adminScreen.ui", self)
        self.UserInfoTable.setColumnWidth(0, 100)
        self.UserInfoTable.setColumnWidth(1, 200)
        self.UserInfoTable.setColumnWidth(2, 340)
        self.UserInfoTable.setColumnWidth(3, 380)
        self.logoutButton.clicked.connect(self.adminLogout)
        self.addButton.clicked.connect(self.newUser)
        self.loadData()
        self.updateButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.UserInfoTable.clicked.connect(self.on_Click)
        self.deleteButton.clicked.connect(self.deleteData)
        self.updateButton.clicked.connect(self.updateUser)
        self.searchButton.clicked.connect(self.search)


   # Logout

   def adminLogout(self):
        logoutAdmin = AdminWelcomePage()
        widget.addWidget(logoutAdmin)
        widget.setCurrentIndex(widget.currentIndex()+1)

   def updateUser(self):
        updateUser = UpdateUserPage()
        widget.addWidget(updateUser)
        widget.setCurrentIndex(widget.currentIndex()+1)

   # Enter Create New User Page
   def newUser(self):
        newUser = NewUserPage()
        widget.addWidget(newUser)
        widget.setCurrentIndex(widget.currentIndex()+1)

   def search(self):
        searchUser = Search()
        widget.addWidget(searchUser)
        widget.setCurrentIndex(widget.currentIndex()+1)

   # Load data into table
   def loadData(self):

        try:
            cur.execute("SELECT * FROM userlogin")
            result = cur.fetchall()
            self.UserInfoTable.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.UserInfoTable.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.UserInfoTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e)

    # Delete data from table
   def deleteData(self):

        try:
            query = "Delete from userlogin where userID = '" + value + "' OR username = '" + value + "' OR email = '" + value + "' OR password = '" + value + "'"
            cur.execute(query)
            conn.commit()

            cur.execute("SELECT * FROM userlogin")
            result = cur.fetchall()
            self.UserInfoTable.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                self.UserInfoTable.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.UserInfoTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e)

   def on_Click(self):
        self.deleteButton.setEnabled(True)
        self.updateButton.setEnabled(True)
        # selected cell value.
        index=(self.UserInfoTable.selectionModel().currentIndex())
        # print(index)
        global value
        value = index.sibling(index.row(),index.column()).data()

class NewUserPage(QDialog):
   def __init__(self):
        super(NewUserPage, self).__init__()
        loadUi("UI/createUserScreen.ui", self)
        self.insertPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.insertConfirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.backButton.clicked.connect(self.backAdminPage)
        self.submitButton.clicked.connect(self.addNewUser)

   # Back Button
   def backAdminPage(self):
        back = AdminPage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

   def newLoadData(self):
        new = AdminPage()
        widget.addWidget(new)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Add new user to database
   def addNewUser(self):
        validate = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        username = ""
        email = ""
        password = ""
        confirmPass = ""

        username = self.insertUsername.text()
        email = self.insertEmail.text()
        password = self.insertPassword.text()
        confirmPass = self.insertConfirmPass.text()

        if len(username) == 0 or len(email) == 0 or len(password) == 0 or len(confirmPass) == 0:
            self.error.setText("Please input all fields")
            self.insertUsername.setFocus()

        else:
            if(re.fullmatch(validate, email)):
                if len(username) == 0 or len(password) == 0 or len(confirmPass) == 0 :
                    self.error.setText("Please input all fields")
                    self.insetUsername.setFocus()

                elif password == confirmPass:
                    cur.execute("SELECT username FROM userlogin where username = '" + username + "'")
                    result = cur.fetchone()

                    print(result)
                    try:
                        if result != None:
                            QMessageBox.warning(QMessageBox(),'Error', 'Already has this user!')
                            main = NewUserPage()
                            main.newLoadData()
                        elif result == None:
                            password = hashlib.md5(password.encode())
                            encryptRegisterPass = password.hexdigest()
                            cur.execute("INSERT INTO userlogin (username, email, password) VALUES ('" + username + "', '" + email  + "' , '" + encryptRegisterPass + "')")
                            conn.commit()
                            QMessageBox.information(QMessageBox(),'Successful', 'User is added succesfully to the database.')

                            main = NewUserPage()
                            main.newLoadData()

                    except Exception:
                        QMessageBox.warning(QMessageBox(),'Error', 'Could not add user to database.')

                else:
                    QMessageBox.warning(QMessageBox(),'Error', 'Password not match.')
                    self.insertPassword.setFocus()
            else:
                QMessageBox.warning(QMessageBox(),'Error', 'Invalid Email Address.')
                self.insertEmail.setFocus()
    
class UpdateUserPage(QDialog):
   def __init__(self):
        super(UpdateUserPage, self).__init__()
        loadUi("UI/modifyUserScreen.ui", self)
        self.showUserData()
        self.backButton.clicked.connect(self.backAdminPage)
        self.submitButton.clicked.connect(self.modify)

   def showUserData(self):
        try:
            query = "Select * from userlogin where userID = '" + value + "' OR username = '" + value + "' OR email = '" + value + "' OR password = '" + value + "'"
            cur.execute(query)
            result = cur.fetchall()

            for row in result:
                self.insertUsername.setText(row[1])
                self.insertEmail.setText(row[2])
                self.insertPassword.setText(row[3])
                self.insertConfirmPass.setText(row[3])

        except mc.Error as e:
            print(e)

   def backAdminPage(self):
        back = AdminPage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

   def modify(self):
        validate = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        username = ""
        email = ""

        username = self.insertUsername.text()
        email = self.insertEmail.text()

        if len(username) == 0 or len(email) == 0:
            self.error.setText("Please input all fields")
            self.insertUsername.setFocus()

        elif (re.fullmatch(validate, email)):
            
            try:
                query = "UPDATE userlogin SET username = '" + username + "', email = '" + email + "' where userID = '" + value + "' OR username = '" + value + "' OR email = '" + value + "' OR password = '" + value + "'"
                cur.execute(query)
                conn.commit()

                QMessageBox.information(QMessageBox(),'Successful', 'User is updated succesfully to the database.')

                main = NewUserPage()
                main.newLoadData()

            except Exception:
                QMessageBox.warning(QMessageBox(),'Error', 'Could not update database.')

        else:
            QMessageBox.warning(QMessageBox(),'Error', 'Email is not valid.')
            self.insertEmail.setFocus()

class Search(QDialog):
   def __init__(self):
        super(Search, self).__init__()
        loadUi("UI/search.ui", self)
        self.insertSearchUsername.setFocus()
        self.searchButton.clicked.connect(self.searchUser)
        self.searchButton.clicked.connect(self.testSearchData)
        self.backButton.clicked.connect(self.backAdminPage)

   def searchUser(self):
        global searchUsername
        searchUsername = self.insertSearchUsername.text()

   def backAdminPage(self):
        back = AdminPage()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

   def testSearchData(self):

        try:
            cur.execute("SELECT * FROM userlogin where username = '" + searchUsername + "'")
            result = cur.fetchone()

            if result != None:
                search = SearchUserPage()
                widget.addWidget(search)
                widget.setCurrentIndex(widget.currentIndex()+1)
                
            elif result == None:
                QMessageBox.information(QMessageBox(),'Error', 'User not found!')
        except mc.Error as e:
            print(e)

class SearchUserPage(QDialog):
   def __init__(self):
        super(SearchUserPage, self).__init__()
        loadUi("UI/searchUserScreen.ui", self)
        self.UserInfoTable.setColumnWidth(0, 100)
        self.UserInfoTable.setColumnWidth(1, 200)
        self.UserInfoTable.setColumnWidth(2, 340)
        self.UserInfoTable.setColumnWidth(3, 380)
        self.backButton.clicked.connect(self.backSearchUserPage)
        self.addButton.clicked.connect(self.newUser)
        self.loadSearchData()
        self.updateButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.UserInfoTable.clicked.connect(self.on_Click)
        self.deleteButton.clicked.connect(self.deleteData)
        self.updateButton.clicked.connect(self.updateUser)
        self.searchButton.clicked.connect(self.search)

   def backSearchUserPage(self):
        back = Search()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

   def updateUser(self):
        updateUser = UpdateUserPage()
        widget.addWidget(updateUser)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
   def search(self):
        searchUser = Search()
        widget.addWidget(searchUser)
        widget.setCurrentIndex(widget.currentIndex()+1)

   # Enter Create New User Page
   def newUser(self):
        newUser = NewUserPage()
        widget.addWidget(newUser)
        widget.setCurrentIndex(widget.currentIndex()+1)

   # Load data into table
   def loadSearchData(self):

        try:
            cur.execute("SELECT * FROM userlogin where username = '" + searchUsername + "'")
            result = cur.fetchall()

            if result != None:
                self.UserInfoTable.setRowCount(0)

                for row_number, row_data in enumerate(result):
                    self.UserInfoTable.insertRow(row_number)

                    for column_number, data in enumerate(row_data):
                        self.UserInfoTable.setItem(
                            row_number, column_number, QTableWidgetItem(str(data)))
            elif result == None:
                QMessageBox.information(QMessageBox(),'Error', 'User not found!')
                back = Search()
                widget.addWidget(back)
                widget.setCurrentIndex(widget.currentIndex()+1)

        except mc.Error as e:
            print(e)

    # Delete data from table
   def deleteData(self):

        try:
            query = "Delete from userlogin where userID = '" + value + "' OR username = '" + value + "' OR email = '" + value + "' OR password = '" + value + "'"
            cur.execute(query)
            conn.commit()

            cur.execute("SELECT * FROM userlogin")
            result = cur.fetchone()
            self.UserInfoTable.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                self.UserInfoTable.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.UserInfoTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e)

   def on_Click(self):
        self.updateButton.setEnabled(True)
        self.deleteButton.setEnabled(True)
        # selected cell value.
        index=(self.UserInfoTable.selectionModel().currentIndex())
        # print(index)
        global value
        value = index.sibling(index.row(),index.column()).data()

class MainScreen(QDialog):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("UI/main.ui", self)
        self.logOutButton.clicked.connect(self.logUserPage)
        self.welcomeName.setText("Welcome Back, " + usern)
        self.startButton.clicked.connect(self.selection)
        self.historyButton.clicked.connect(self.history)

    def history(self):
        history = History()
        widget.addWidget(history)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def selection(self):
        sel = Selection()
        widget.addWidget(sel)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

class SpecificFruitPage(QDialog):
   def __init__(self):
        super(SpecificFruitPage, self).__init__()
        loadUi("UI/specificFruitHistory.ui", self)
        self.showFruitData()
        self.backButton.clicked.connect(self.backfruitHistoryPage)
        self.logOutButton.clicked.connect(self.logUserPage)

   def convert_data(self, data, file_name):
        # Convert binary format to images
        # or files data(with given file_name)
        with open(file_name, 'wb') as file:
            file.write(data)

   def showFruitData(self):
        try:
            query = "SELECT * FROM fruit where fruitname = '" + value + "' OR fruitCondition = '" + value + "' OR fruitSize = '" + value + "'OR fruitTexture = '" + value + "'OR fruitColor = '" + value + "'OR fruitSurvival = '" + value + "'OR dateTime = '" + value + "'"
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                self.label_9.setText(row[3])
                self.label_10.setText(row[4])
                self.label_12.setText(row[5])
                self.label_11.setText(row[6])
                self.label_14.setText(row[7])
                checkTime = str(row[8])
                self.label_16.setText(checkTime)
                self.convert_data(row[2], "DatabaseRetrievedImage/retrievedImage.jpg")
                image = "DatabaseRetrievedImage/retrievedImage.jpg"
                checkImage= QtGui.QPixmap(image)
                checkImage= checkImage.scaled(self.imgWin.width(), self.imgWin.height(), QtCore.Qt.KeepAspectRatio)
                self.imgWin.setPixmap(checkImage)
                self.imgWin.setAlignment(QtCore.Qt.AlignCenter)

        except mc.Error as e:
            print(e)

   def backfruitHistoryPage(self):
        back = FruitHistory()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

   def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

class History(QDialog):
    def __init__(self):
        super(History, self).__init__()
        loadUi("UI/historySelectionScreen.ui", self)
        self.logOutButton.clicked.connect(self.logUserPage)
        self.homeButton.clicked.connect(self.home)
        self.fruitSelection_1.clicked.connect(self.fruit1)
        self.fruitSelection_2.clicked.connect(self.fruit2)

    def home(self):
        home = MainScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def fruit1(self):
        global fruitname
        fruitname = self.fruitSelection_1.text()
        fruit1 = FruitHistory()
        widget.addWidget(fruit1)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def fruit2(self):
        global fruitname
        fruitname = self.fruitSelection_2.text()
        fruit2 = FruitHistory()
        widget.addWidget(fruit2)
        widget.setCurrentIndex(widget.currentIndex()+1)

class FruitHistory(QDialog):
    def __init__(self):
        super(FruitHistory, self).__init__()
        loadUi("UI/fruitHistory.ui", self)
        self.label.setText(fruitname)
        global res
        res = fruitname[0].lower() + fruitname[1:]
        self.fruitTable.setColumnWidth(0, 100)
        self.fruitTable.setColumnWidth(1, 280)
        self.fruitTable.setColumnWidth(2, 100)
        self.fruitTable.setColumnWidth(3, 100)
        self.fruitTable.setColumnWidth(4, 240)
        self.fruitTable.setColumnWidth(5, 100)
        self.fruitTable.setColumnWidth(6, 168)
        self.loadFruitData()
        self.deleteButton.setEnabled(False)
        self.fruitTable.clicked.connect(self.on_Click)
        self.deleteButton.clicked.connect(self.deleteData)
        self.logOutButton.clicked.connect(self.logUserPage)
        self.backButton.clicked.connect(self.fruitHistorySel)
        self.searchButton.clicked.connect(self.history)
        self.checkButton.clicked.connect(self.checkData)
        self.checkButton.setEnabled(False)

    def loadFruitData(self):
        try:
            cur.execute("SELECT fruitName, fruitCondition, fruitSize, fruitTexture, fruitColor, fruitSurvival, dateTime FROM fruit WHERE fruitName = '" + res + "'")
            result = cur.fetchall()
            self.fruitTable.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.fruitTable.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.fruitTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e)

    def deleteData(self):

        try:
            query = "Delete from fruit where fruitName = '" + value + "' or fruitCondition = '" + value + "' or fruitSize = '" + value + "' or fruitTexture = '" + value + "' or fruitColor = '" + value + "'  or fruitSurvival = '" + value + "' or dateTime = '" + value + "'"
            cur.execute(query)
            conn.commit()

            cur.execute("SELECT fruitName, fruitCondition, fruitSize, fruitTexture, fruitColor, fruitSurvival, dateTime FROM fruit WHERE fruitName = '" + res + "'")
            result = cur.fetchall()
            self.fruitTable.setRowCount(0)
            self.deleteButton.setEnabled(False)
            self.checkButton.setEnabled(False)
            
            for row_number, row_data in enumerate(result):
                self.fruitTable.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.fruitTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e)

    def checkData(self):
        check = SpecificFruitPage()
        widget.addWidget(check)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def on_Click(self):
        self.checkButton.setEnabled(True)
        self.deleteButton.setEnabled(True)
        # selected cell value.
        index=(self.fruitTable.selectionModel().currentIndex())
        # print(index)
        global value
        value = index.sibling(index.row(),index.column()).data()

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def history(self):
        searchF = SearchFruit()
        widget.addWidget(searchF)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def fruitHistorySel(self):
        history = History()
        widget.addWidget(history)
        widget.setCurrentIndex(widget.currentIndex()+1)

class SearchFruit(QDialog):
    def __init__(self):
        super(SearchFruit, self).__init__()
        loadUi("UI/fruitSearch.ui", self)
        self.fruitSearch.setFocus()
        self.searchButton.clicked.connect(self.searchFruitHistory)
        self.searchButton.clicked.connect(self.testSearchData)
        self.logOutButton.clicked.connect(self.logUserPage)
        self.backButton.clicked.connect(self.backHistory)

    def searchFruitHistory(self):
        global fruitKeyword
        fruitKeyword = self.fruitSearch.text()

    def backHistory(self):
        back = FruitHistory()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def testSearchData(self):

        try:
            cur.execute("SELECT fruitName, fruitCondition, fruitSize, fruitTexture, fruitColor, fruitSurvival, dateTime FROM fruit where fruitName = '" + res + "' AND fruitCondition = '" + fruitKeyword + "' OR fruitSize = '" + fruitKeyword + "' OR fruitTexture = '" + fruitKeyword + "' OR fruitColor = '" + fruitKeyword + "' OR fruitSurvival = '" + fruitKeyword + "' OR DATE(dateTime) = '" + fruitKeyword + "'")
            result = cur.fetchone()

            if result != None:
                search = FruitSearchHistory()
                widget.addWidget(search)
                widget.setCurrentIndex(widget.currentIndex()+1)

            elif result == None:
                QMessageBox.information(QMessageBox(),'Error', 'Data not found!')
        except mc.Error as e:
            print(e)

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

class FruitSearchHistory(QDialog):
    def __init__(self):
        super(FruitSearchHistory, self).__init__()
        loadUi("UI/fruitSearchScreen.ui", self)
        self.label.setText(fruitname)
        global res
        res = fruitname[0].lower() + fruitname[1:]
        self.fruitTable.setColumnWidth(0, 100)
        self.fruitTable.setColumnWidth(1, 280)
        self.fruitTable.setColumnWidth(2, 100)
        self.fruitTable.setColumnWidth(3, 100)
        self.fruitTable.setColumnWidth(4, 240)
        self.fruitTable.setColumnWidth(5, 100)
        self.fruitTable.setColumnWidth(6, 168)
        self.loadFruitData()
        self.deleteButton.setEnabled(False)
        self.fruitTable.clicked.connect(self.on_Click)
        self.deleteButton.clicked.connect(self.deleteData)
        self.logOutButton.clicked.connect(self.logUserPage)
        self.backButton.clicked.connect(self.history)
        self.searchButton.clicked.connect(self.history)
        self.checkButton.clicked.connect(self.checkData)
        self.checkButton.setEnabled(False)

    def loadFruitData(self):
        try:
            cur.execute("SELECT fruitName, fruitCondition, fruitSize, fruitTexture, fruitColor, fruitSurvival, dateTime FROM fruit where fruitName = '" + res + "' AND (fruitCondition = '" + fruitKeyword + "' OR fruitSize = '" + fruitKeyword + "' OR fruitTexture = '" + fruitKeyword + "' OR fruitColor = '" + fruitKeyword + "' OR fruitSurvival = '" + fruitKeyword + "' OR DATE(dateTime) ='" + fruitKeyword + "') ")
            result = cur.fetchall()

            if result != None:
                self.fruitTable.setRowCount(0)

                for row_number, row_data in enumerate(result):
                    self.fruitTable.insertRow(row_number)

                    for column_number, data in enumerate(row_data):
                        self.fruitTable.setItem(
                            row_number, column_number, QTableWidgetItem(str(data)))
            elif result == None:
                QMessageBox.information(QMessageBox(),'Error', 'Data not found!')
                back = SearchFruit()
                widget.addWidget(back)
                widget.setCurrentIndex(widget.currentIndex()+1)

        except mc.Error as e:
            print(e)

    def deleteData(self):

        try:
            query = "Delete from fruit where fruitName = '" + value + "' OR fruitCondition = '" + value + "' OR fruitSize = '" + value + "' OR fruitTexture = '" + value + "' OR fruitColor = '" + value + "' OR fruitSurvival = '" + value + "' OR dateTime = '" + value + "' "
            cur.execute(query)
            conn.commit()

            cur.execute("SELECT fruitName, fruitCondition, fruitSize, fruitTexture, fruitColor, fruitSurvival, dateTime FROM fruit WHERE fruitName = '" + res + "'")
            result = cur.fetchall()
            self.fruitTable.setRowCount(0)
            self.deleteButton.setEnabled(False)
            self.checkButton.setEnabled(False)
            
            for row_number, row_data in enumerate(result):
                self.fruitTable.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.fruitTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e)

    def checkData(self):
        check = SpecificFruitPage()
        widget.addWidget(check)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def on_Click(self):
        self.checkButton.setEnabled(True)
        self.deleteButton.setEnabled(True)
        # selected cell value.
        index=(self.fruitTable.selectionModel().currentIndex())
        # print(index)
        global value
        value = index.sibling(index.row(),index.column()).data()

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def history(self):
        history = SearchFruit()
        widget.addWidget(history)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Selection(QDialog):
    def __init__(self):
        super(Selection, self).__init__()
        loadUi("UI/selection.ui", self)
        self.logOutButton.clicked.connect(self.logUserPage)
        self.backButton.clicked.connect(self.mainScreen)
        self.proceedButton.clicked.connect(self.submit)

    def submit(self):
        global comboSel
        comboSel = 0
        if self.comboBox.currentIndex() == 0:
            comboSel = 0
        elif self.comboBox.currentIndex() == 1:
            comboSel = 1
        
        sub = Submit()
        widget.addWidget(sub)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def mainScreen(self):
        mainm = MainScreen()
        widget.addWidget(mainm)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Submit(QDialog):
    def __init__(self):
        super(Submit, self).__init__()
        loadUi("UI/submit.ui", self)
        global capturetimes
        global uploadtimes
        capturetimes = 0
        uploadtimes = 0
        self.logOutButton.clicked.connect(self.logUserPage)
        self.backButton.clicked.connect(self.selection)
        self.captureButton.clicked.connect(self.capture)
        self.uploadButton.clicked.connect(self.setImage)
        self.calButton.clicked.connect(self.plot_solution)
        self.calButton.clicked.connect(self.result)

    def result(self):
        if flag == True:
            if capturetimes == 1 or uploadtimes == 1:
                resu = Result()
                widget.addWidget(resu)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                QMessageBox.information(QMessageBox(),'Error', 'There are no image uploaded!')
        

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def selection(self):
        sel = Selection()
        widget.addWidget(sel)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def load_checkpoint_condition(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model

    def load_checkpoint_survival_mango(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model

    def load_checkpoint_color_mango(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 6)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model
    
    def load_checkpoint_size_mango(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model

    def load_checkpoint_texture_mango(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model
    
    def load_checkpoint_survival_banana(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model

    def load_checkpoint_color_banana(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model
    
    def load_checkpoint_size_banana(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model

    def load_checkpoint_texture_banana(self,filepath):

        # checkpoint = torch.load(filepath,map_location='cpu') #unka
        checkpoint = torch.load(filepath, map_location=lambda storage, loc: storage)
        
        # model.load_state_dict(checkpoint['state_dict'])
        model = models.resnet34(weights='ResNet34_Weights.DEFAULT')
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 5)
        model.load_state_dict(checkpoint['state_dict'])
        model.class_to_idx = checkpoint['class_to_idx']
        
        return model

    def find_classes_condition(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='dataset/test'
    global classesCondition
    global c_to_idx_condition
    classesCondition, c_to_idx_condition = find_classes_condition(test_dir)

    def find_classes_survival_mango(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='survivalTimeMango/test'
    global classesSurvivalMango
    global c_to_idx_survival_mango
    classesSurvivalMango, c_to_idx_survival_mango = find_classes_survival_mango(test_dir)

    def find_classes_color_mango(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='colorMango/test'
    global classesColorMango
    global c_to_idx_color_mango
    classesColorMango, c_to_idx_color_mango = find_classes_color_mango(test_dir)

    def find_classes_size_mango(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='sizeMango/test'
    global classesSizeMango
    global c_to_idx_size_mango
    classesSizeMango, c_to_idx_size_mango = find_classes_size_mango(test_dir)

    def find_classes_texture_mango(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='textureMango/test'
    global classesTextureMango
    global c_to_idx_texture_mango
    classesTextureMango, c_to_idx_texture_mango = find_classes_texture_mango(test_dir)

    def find_classes_survival_banana(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='survivalTimeBanana/test'
    global classesSurvivalBanana
    global c_to_idx_survival_banana
    classesSurvivalBanana, c_to_idx_survival_banana = find_classes_survival_banana(test_dir)

    def find_classes_color_banana(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='colorBanana/test'
    global classesColorBanana
    global c_to_idx_color_banana
    classesColorBanana, c_to_idx_color_banana = find_classes_color_banana(test_dir)

    def find_classes_size_banana(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='sizeBanana/test'
    global classesSizeBanana
    global c_to_idx_size_banana
    classesSizeBanana, c_to_idx_size_banana = find_classes_size_banana(test_dir)

    def find_classes_texture_banana(dir):

        classes = os.listdir(dir)
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    test_dir='textureBanana/test'
    global classesTextureBanana
    global c_to_idx_texture_banana
    classesTextureBanana, c_to_idx_texture_banana = find_classes_texture_banana(test_dir)

    def process_image(self,image):
    
        # Process a PIL image for use in a PyTorch model

        # Converting image to PIL image using image file path
        pil_im = Image.open(f'{image}' )

        # Building image transform
        transform = transforms.Compose([transforms.Resize((244,244)),
                                        # transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.5, 0.5, 0.5], 
                                                            [0.5, 0.5, 0.5])]) 
        
        # Transforming image for use with network
        pil_tfd = transform(pil_im)
        
        # Converting to Numpy array 
        array_im_tfd = np.array(pil_tfd)
        
        return array_im_tfd  

    def capture(self):
        global capturetimes
        capturetimes = 1
        url = "http://192.168.1.104:8080/shot.jpg"
  
        # While loop to continuously fetching data from the Url
        while True:
            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=1000, height=1800)
            cam = cv2.VideoCapture(url) 
            global pat
            pat = ""
            result, image = cam.read()
        
            break
        if result:
            cv2.imwrite("captureFruit/capture.png", image)
            cv_img = cv2.imread("captureFruit/capture.png")
            qt_img = self.convert_cv_qt(cv_img)
            capturename = "captureFruit/capture.png"
            pat = capturename
            global pixmap
            pixmap = qt_img
            self.imgWin.clear()
            self.imgWin.setPixmap(qt_img)
            self.imgWin.setAlignment(QtCore.Qt.AlignCenter)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.imgWin.width(), self.imgWin.height(), QtCore.Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def setImage(self):
        global uploadtimes
        uploadtimes = 1
        filename,_= QtWidgets.QFileDialog.getOpenFileName(None, "Select  Image", "","Image Files (*.png *.jpg *.jpeg *.bmp)")
        global pat
        pat = ""
        pat = filename
        if filename:

            global pixmap
            pixmap= QtGui.QPixmap(filename)
            pixmap= pixmap.scaled(self.imgWin.width(), self.imgWin.height(), QtCore.Qt.KeepAspectRatio)
            self.imgWin.clear()
            self.imgWin.setPixmap(pixmap)
            self.imgWin.setAlignment(QtCore.Qt.AlignCenter)

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def insertBLOB(self, fruitName, empPicture, condition, size, texture, color, time, dateTime):
        try:
            sql_insert_blob_query = """ INSERT INTO fruit
                            (fruitName, fruitImage, fruitCondition, fruitSize, fruitTexture, fruitColor, fruitSurvival, dateTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

            empPicture = self.convertToBinaryData(empPicture)

            # Convert data into tuple format
            insert_blob_tuple = (fruitName, empPicture, condition, size, texture, color, time, dateTime)
            cur.execute(sql_insert_blob_query, insert_blob_tuple)
            conn.commit()

        except Exception:
            QMessageBox.warning(QMessageBox(),'Error', 'Could not add user to database.')

    def predictCondition(self,image_path, model, topk=2):
        path = "modelPath/modelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_condition(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        conf = np.array(probs_top)[0]
        predicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return conf, predicted

    def predictSurvivalMango(self,image_path, model, topk=4):
        path = "modelPath/survivalTimeMangoModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_survival_mango(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        survivalMangoConf = np.array(probs_top)[0]
        survivalMangoPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return survivalMangoConf, survivalMangoPredicted

    def predictSurvivalBanana(self,image_path, model, topk=4):
        path = "modelPath/survivalTimeBananaModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_survival_banana(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        survivalbananaConf = np.array(probs_top)[0]
        survivalbananaPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return survivalbananaConf, survivalbananaPredicted

    def predictColorMango(self,image_path, model, topk=6):
        path = "modelPath/colorMangoModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_color_mango(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        colorMangoConf = np.array(probs_top)[0]
        colorMangoPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return colorMangoConf, colorMangoPredicted

    def predictColorBanana(self,image_path, model, topk=3):
        path = "modelPath/colorBananaModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_color_banana(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        colorBananaConf = np.array(probs_top)[0]
        colorBananaPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return colorBananaConf, colorBananaPredicted

    def predictSizeMango(self,image_path, model, topk=2):
        path = "modelPath/sizeMangoModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_size_mango(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        sizeMangoConf = np.array(probs_top)[0]
        sizeMangoPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return sizeMangoConf, sizeMangoPredicted

    def predictSizeBanana(self,image_path, model, topk=2):
        path = "modelPath/sizeBananaModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_size_banana(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        sizeBananaConf = np.array(probs_top)[0]
        sizeBananaPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return sizeBananaConf, sizeBananaPredicted

    def predictTextureMango(self,image_path, model, topk=3):
        path = "modelPath/textureMangoModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_size_mango(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        textureMangoConf = np.array(probs_top)[0]
        textureMangoPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return textureMangoConf, textureMangoPredicted

    def predictTextureBanana(self,image_path, model, topk=2):
        path = "modelPath/textureBananaModelFinal.pth"
        img_path = pat
        global loaded_model
        loaded_model = self.load_checkpoint_size_banana(path)
        img = self.process_image(img_path)
        img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
        # Adding dimension to image to comply with (B x C x W x H) input of model
        img_add_dim = img_tensor.unsqueeze_(0)
        # Setting model to evaluation mode and turning off gradients
        loaded_model.eval()
        with torch.no_grad():
            # Running image through network
            output = loaded_model.forward(img_add_dim)
        # conf, predicted = torch.max(output.data, 1)   
        probs_top = output.topk(topk)[0]
        predicted_top = output.topk(topk)[1]
        # Converting probabilities and outputs to lists
        textureBananaConf = np.array(probs_top)[0]
        textureBananaPredicted = np.array(predicted_top)[0]
        # return probs_top_list, index_top_list
        return textureBananaConf, textureBananaPredicted

    def plot_solution(self):
        global flag
        flag = True
        now = datetime.now()
        global dateTime, resuTime
        dateTime = str(now)
        resuTime = now

        if capturetimes == 1 or uploadtimes == 1:
            path = "modelFinal.pth"
            img_path = pat
            conf2, predicted1 = self.predictCondition(img_path, path)
            names = ""
            for i in range(1):
                names += classesCondition[predicted1[i]]
            global lab
            global survival
            survival = ""
            lab = names
            global time 
            time = ""

            if comboSel == 0:
                if "Banana" in lab:
                    QMessageBox.warning(QMessageBox(),'Error', 'This is not Mango!')
                    flag = False
                elif "Mixed" in lab:
                    QMessageBox.warning(QMessageBox(),'Error', 'This is not Mango!')
                    flag = False
                elif "Mango" in lab:
                    fruitName = "Mango"
                    if "Spoiled" in lab:
                        survivalPath = "survivalTimeMangoModelFinal.pth"
                        img_survivalPath = pat
                        conf2, predicted1 = self.predictSurvivalMango(img_survivalPath, survivalPath)
                        names = ""
                        for i in range(1):
                            names += classesSurvivalMango[predicted1[i]]
                        survival = "/" + names
                    else:
                        survival = ""

                    colorPath = "modelPath/colorMangoModelFinal.pth"
                    img_colorPath = pat
                    conf2, predicted1 = self.predictColorMango(img_colorPath, colorPath)
                    names = ""
                    for i in range(1):
                        names += classesColorMango[predicted1[i]]
                    global color
                    color = names 

                    sizePath = "modelPath/sizeMangoModelFinal.pth"
                    img_sizePath = pat
                    conf2, predicted1 = self.predictSizeMango(img_sizePath, sizePath)
                    names = ""
                    for i in range(1):
                        names += classesSizeMango[predicted1[i]]
                    global size
                    size = names 

                    texturePath = "modelPath/textureMangoModelFinal.pth"
                    img_texturePath = pat
                    conf2, predicted1 = self.predictTextureMango(img_texturePath, texturePath)
                    names = ""
                    for i in range(1):
                        names += classesTextureMango[predicted1[i]]
                    global texture
                    texture = names 
                    
                    if "100%" in survival:
                        time = "0 Day"
                    elif "75%" in survival:
                        time = "1 Day"
                    elif "50%" in survival:
                        time = "2 Day"
                    elif "25%" in survival:
                        time = "3 Day"
                    elif color == "85" + "%" + "-100% Yellow":
                        time = "4 Day"
                    elif color == "85" + "%" +"-100% Yellow-orange":
                        time = "5 Day"
                    elif color == "50" + "%"+" Green 50% Orange":
                        time = "6 Day"
                    elif color == "85" +"%" + "-100" +"%"+" Green":
                        time = "7 Day"

                    condition = lab + survival
                    self.insertBLOB(fruitName, pat, condition, size, texture, color, time, dateTime)

            elif comboSel == 1:
                if "Mango" in lab:
                    QMessageBox.warning(QMessageBox(),'Error', 'This is not Banana!')
                    flag = False
                elif "Mixed" in lab:
                    QMessageBox.warning(QMessageBox(),'Error', 'This is not Banana!')
                    flag = False
                elif "Banana" in lab:
                    fruitName = "Banana"
                    if "Spoiled" in lab:
                        survivalPath = "survivalTimeBananaModelFinal.pth"
                        img_survivalPath = pat
                        conf2, predicted1 = self.predictSurvivalMango(img_survivalPath, survivalPath)
                        names = ""
                        for i in range(1):
                            names += classesSurvivalBanana[predicted1[i]]
                        survival = "/" + names
                    else:
                        survival = ""

                    colorPath = "modelPath/colorBananaModelFinal.pth"
                    img_colorPath = pat
                    conf2, predicted1 = self.predictColorBanana(img_colorPath, colorPath)
                    names = ""
                    for i in range(1):
                        names += classesColorBanana[predicted1[i]]
                    
                    color = names 

                    sizePath = "modelPath/sizeBananaModelFinal.pth"
                    img_sizePath = pat
                    conf2, predicted1 = self.predictSizeBanana(img_sizePath, sizePath)
                    names = ""
                    for i in range(1):
                        names += classesSizeBanana[predicted1[i]]
                
                    size = names 

                    texturePath = "modelPath/textureBananaModelFinal.pth"
                    img_texturePath = pat
                    conf2, predicted1 = self.predictTextureBanana(img_texturePath, texturePath)
                    names = ""
                    for i in range(1):
                        names += classesTextureBanana[predicted1[i]]
                
                    texture = names 

                    if "100%" in survival:
                        time = "0 Day"
                    elif "75%" in survival:
                        time = "1 Day"
                    elif "50%" in survival:
                        time = "2 Day"
                    elif "25%" in survival:
                        time = "3 Day"
                    elif "85" + "%" + "-100% Yellow" in color:
                        time = "5 Day"

                    condition = lab + survival
                    self.insertBLOB(fruitName, pat, condition, size, texture, color, time, dateTime)

class Result(QDialog):
    def __init__(self):
        super(Result, self).__init__()
        loadUi("UI/result.ui", self)
        currentTime = str(resuTime.strftime("%Y-%m-%d %H:%M:%S"))
        self.imgWin.setPixmap(pixmap)
        self.label_9.setText(lab + survival)
        self.label_10.setText(size)
        self.label_11.setText(color)
        self.label_12.setText(texture)
        self.label_14.setText(time)
        self.label_16.setText(currentTime)
        self.logOutButton.clicked.connect(self.logUserPage)
        self.homeButton.clicked.connect(self.home)
        self.uploadNewButton.clicked.connect(self.submit)
        main = NewUserPage()
        main.newLoadData()


    def home(self):
        home = MainScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def logUserPage(self):
        user = WelcomeScreen()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def submit(self):
        sub = Submit()
        widget.addWidget(sub)
        widget.setCurrentIndex(widget.currentIndex()+1)

# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setWindowTitle("Fruit Quality Sorting System")
widget.setWindowIcon(QtGui.QIcon('img/fruits.png'))
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")