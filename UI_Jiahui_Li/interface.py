# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'source.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 0, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(520, 70, 71, 21))
        self.comboBox.setObjectName("comboBox")
        for i in range(0, users_id.shape[0]+1):
            self.comboBox.addItem("")


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(350, 130, 301, 371))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(680, 130, 301, 371))
        self.textBrowser_2.setObjectName("textBrowser_2")

        #MF BELOW
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 500, 1811, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        #NCF BELOW
        self.NCF_label = QtWidgets.QLabel(self.centralwidget)
        self.NCF_label.setGeometry(QtCore.QRect(690, 500, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(12)
        self.NCF_label.setFont(font)
        self.NCF_label.setObjectName("NCF_label")


        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 130, 301, 371))
        self.textBrowser_3.setObjectName("textBrowser_3")

        #rating movies label
        self.RM_label = QtWidgets.QLabel(self.centralwidget)
        self.RM_label.setGeometry(QtCore.QRect(110, 500, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Light")
        font.setPointSize(12)
        self.RM_label.setFont(font)
        self.RM_label.setObjectName("RM_label")
        
        
        
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
        RecommenderSystem.setWindowTitle(_translate("RecommenderSystem", "MainWindow"))
        self.label.setText(_translate("RecommenderSystem", "Recommender System"))
        self.label_2.setText(_translate("RecommenderSystem", "USER ID"))
        for i in range(0, users_id.shape[0]+1):
            self.comboBox.setItemText(i, _translate("MainWindow", str(i+1)))

        self.textBrowser.setText("Matrix Factorization")
        self.textBrowser_2.setText("Neural Collaborative Filtering")

        self.label_3.setText(_translate("RecommenderSystem", "Matrix Factorization"))
        self.NCF_label.setText(_translate("RecommenderSystem", "Neural Collaborative Filtering"))
        self.RM_label.setText(_translate("RecommenderSystem", "Rated Movies"))