# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menutoolbar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menueditor = QtWidgets.QMenu(self.menubar)
        self.menueditor.setObjectName("menueditor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionone = QtWidgets.QAction(MainWindow)
        self.actionone.setObjectName("actionone")
        self.actiontwo = QtWidgets.QAction(MainWindow)
        self.actiontwo.setObjectName("actiontwo")
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionopen)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionclose)
        self.menueditor.addAction(self.actionone)
        self.menueditor.addSeparator()
        self.menueditor.addAction(self.actiontwo)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menueditor.menuAction())
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionclose)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionone)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actiontwo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menueditor.setTitle(_translate("MainWindow", "editor"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionone.setText(_translate("MainWindow", "one"))
        self.actiontwo.setText(_translate("MainWindow", "two"))
