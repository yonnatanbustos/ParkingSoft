# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaContrasena.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaContrasena(object):
    def setupUi(self, VentanaContrasena):
        VentanaContrasena.setObjectName("VentanaContrasena")
        VentanaContrasena.resize(400, 98)
        VentanaContrasena.setMaximumSize(QtCore.QSize(400, 98))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../co/edu/uniquindio/parkingsoft/icons/icon-password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaContrasena.setWindowIcon(icon)
        VentanaContrasena.setStyleSheet("QLineEdit{\n"
"font: 13px \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"font: 13pt \"Tahoma\";\n"
"}\n"
"QPushButton{\n"
"font: 13pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0c80c4;\n"
"}")
        self.btnIngresar = QtWidgets.QPushButton(VentanaContrasena)
        self.btnIngresar.setGeometry(QtCore.QRect(314, 40, 81, 41))
        self.btnIngresar.setObjectName("btnIngresar")
        self.label = QtWidgets.QLabel(VentanaContrasena)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 20))
        self.label.setObjectName("label")
        self.txtPasswordSeguridad = QtWidgets.QLineEdit(VentanaContrasena)
        self.txtPasswordSeguridad.setGeometry(QtCore.QRect(12, 40, 291, 41))
        self.txtPasswordSeguridad.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPasswordSeguridad.setObjectName("txtPasswordSeguridad")

        self.retranslateUi(VentanaContrasena)
        QtCore.QMetaObject.connectSlotsByName(VentanaContrasena)

    def retranslateUi(self, VentanaContrasena):
        _translate = QtCore.QCoreApplication.translate
        VentanaContrasena.setWindowTitle(_translate("VentanaContrasena", "Contraseña de Seguridad"))
        self.btnIngresar.setText(_translate("VentanaContrasena", "Ingresar"))
        self.label.setText(_translate("VentanaContrasena", "Contraseña de Seguridad:"))

