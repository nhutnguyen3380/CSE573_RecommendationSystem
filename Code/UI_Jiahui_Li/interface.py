# -*- coding: utf-8 -*-
"""
Created on April 9th, 2023, 7:17:16 PM

@author: Jiahui Li
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

users_raw = [item.strip().split("::") for item in open('ml-1m/users.dat', 'r').readlines()]
users = pd.DataFrame(users_raw, columns=['UserID','Gender','Age','Occupation','Zip-code'])


users_id = users['UserID']

class Ui_RecommenderSystem(object):
    def setupUi(self, RecommenderSystem):
        RecommenderSystem.setObjectName("RecommenderSystem")
        RecommenderSystem.resize(1000, 600)
        RecommenderSystem.setMinimumSize(QtCore.QSize(1000, 600))
        RecommenderSystem.setMaximumSize(QtCore.QSize(1000, 600))
        RecommenderSystem.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(RecommenderSystem)
        self.centralwidget.setObjectName("centralwidget")

        #TITLE label
        self.TITLE_label = QtWidgets.QLabel(self.centralwidget)
        self.TITLE_label.setGeometry(QtCore.QRect(270, 0, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.TITLE_label.setFont(font)
        self.TITLE_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE_label.setObjectName("TITLE_label")
        
        #USER ID label
        self.USERID_label = QtWidgets.QLabel(self.centralwidget)
        self.USERID_label.setGeometry(QtCore.QRect(400, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(16)
        self.USERID_label.setFont(font)
        self.USERID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.USERID_label.setObjectName("USERID_label")

        #USER ID combobox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(520, 70, 71, 21))
        self.comboBox.setObjectName("comboBox")
        for i in range(0, users_id.shape[0]+1):
            self.comboBox.addItem("")

        #RM text browser
        self.RM_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.RM_browser.setGeometry(QtCore.QRect(20, 130, 301, 371))
        self.RM_browser.setObjectName("RM_browser")

        #MF text browser
        self.MF_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.MF_browser.setGeometry(QtCore.QRect(350, 130, 301, 371))
        self.MF_browser.setObjectName("MF_browser")

        #NCF text browser
        self.NCF_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.NCF_browser.setGeometry(QtCore.QRect(680, 130, 301, 371))
        self.NCF_browser.setObjectName("NCF_browser")

        # RM label
        self.RM_label = QtWidgets.QLabel(self.centralwidget)
        self.RM_label.setGeometry(QtCore.QRect(110, 500, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(12)
        self.RM_label.setFont(font)
        self.RM_label.setObjectName("RM_label")

        #MF label
        self.MF_label = QtWidgets.QLabel(self.centralwidget)
        self.MF_label.setGeometry(QtCore.QRect(410, 500, 1811, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(12)
        self.MF_label.setFont(font)
        self.MF_label.setObjectName("MF_label")

        #NCF label
        self.NCF_label = QtWidgets.QLabel(self.centralwidget)
        self.NCF_label.setGeometry(QtCore.QRect(690, 500, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(12)
        self.NCF_label.setFont(font)
        self.NCF_label.setObjectName("NCF_label")

        RecommenderSystem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RecommenderSystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        RecommenderSystem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RecommenderSystem)

        self.statusbar.setObjectName("statusbar")
        RecommenderSystem.setStatusBar(self.statusbar)
        self.retranslateUi(RecommenderSystem)
        QtCore.QMetaObject.connectSlotsByName(RecommenderSystem)

    def retranslateUi(self, RecommenderSystem):
        _translate = QtCore.QCoreApplication.translate
        RecommenderSystem.setWindowTitle(_translate("RecommenderSystem", "Recommender System"))
        self.TITLE_label.setText(_translate("RecommenderSystem", "Recommender System"))
        self.USERID_label.setText(_translate("RecommenderSystem", "USER ID"))
        for i in range(0, users_id.shape[0]+1):
            self.comboBox.setItemText(i+1, _translate("MainWindow", str(i+1)))


        self.MF_label.setText(_translate("RecommenderSystem", "Matrix Factorization"))
        self.NCF_label.setText(_translate("RecommenderSystem", "Neural Collaborative Filtering"))
        self.RM_label.setText(_translate("RecommenderSystem", "Rated Movies"))
