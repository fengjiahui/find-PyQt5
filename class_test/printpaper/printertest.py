# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printertest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(714, 275)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 306, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.numberspinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.numberspinBox.setObjectName("numberspinBox")
        self.gridLayout.addWidget(self.numberspinBox, 0, 1, 1, 1)
        self.stylecomboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.stylecomboBox.setObjectName("stylecomboBox")
        self.stylecomboBox.addItem("")
        self.stylecomboBox.addItem("")
        self.stylecomboBox.addItem("")
        self.gridLayout.addWidget(self.stylecomboBox, 0, 2, 1, 1)
        self.printpushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.printpushButton.setObjectName("printpushButton")
        self.gridLayout.addWidget(self.printpushButton, 0, 4, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 130, 160, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.preiviewpushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.preiviewpushButton.setObjectName("preiviewpushButton")
        self.gridLayout_2.addWidget(self.preiviewpushButton, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 30, 54, 12))
        self.label_4.setObjectName("label_4")
        self.resultlabel = QtWidgets.QLabel(Form)
        self.resultlabel.setGeometry(QtCore.QRect(390, 50, 241, 171))
        self.resultlabel.setText("")
        self.resultlabel.setObjectName("resultlabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "打印控制"))
        self.label_3.setText(_translate("Form", "纸张类型"))
        self.label_2.setText(_translate("Form", "打印份数"))
        self.stylecomboBox.setItemText(0, _translate("Form", "A4"))
        self.stylecomboBox.setItemText(1, _translate("Form", "A3"))
        self.stylecomboBox.setItemText(2, _translate("Form", "A5"))
        self.printpushButton.setText(_translate("Form", "打印"))
        self.preiviewpushButton.setText(_translate("Form", "预览"))
        self.checkBox.setText(_translate("Form", "全屏预览"))
        self.label_4.setText(_translate("Form", "操作结果"))
