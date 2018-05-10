# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Ui_VentanaLogin(object):
    font: QFont

    def setupUi(self, VentanaLogin):
        VentanaLogin.setObjectName("VentanaLogin")
        VentanaLogin.resize(700, 187)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaLogin.sizePolicy().hasHeightForWidth())
        VentanaLogin.setSizePolicy(sizePolicy)
        VentanaLogin.setMaximumSize(QtCore.QSize(700, 187))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "..\icons\icons-página-principal-.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaLogin.setWindowIcon(icon)
        VentanaLogin.setToolTip("")
        VentanaLogin.setStatusTip("")
        VentanaLogin.setWhatsThis("")
        VentanaLogin.setAccessibleName("")
        VentanaLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        VentanaLogin.setStyleSheet("#VentanaLogin{\n"""
                                   "background-color: rgb(230, 230, 230)\n"
                                   "}\n"
                                   "\n"
                                   "QLabel{\n"
                                   "font: 13pt \"Tahoma\";\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "#labelLogin{\n"
                                   "font-size: 30px;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "QLineEdit, QPushButton{\n"
                                   "font: 13pt \"Tahoma\";\n"
                                   "border: 1px solid black;\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "\n"
                                   "background-color: #0c80c4;\n"
                                   "}\n"
                                   "\n"
                                   "#btnImagen:hover{\n"
                                   "background-color: none;\n"
                                   "}\n"
                                   "#btnImagen{\n"
                                   "border-style:none;\n"
                                   "}")
        VentanaLogin.setWindowFilePath("")
        VentanaLogin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(VentanaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(160, 80, 391, 82))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layoutFormulario = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layoutFormulario.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.layoutFormulario.setContentsMargins(0, 10, 0, 0)
        self.layoutFormulario.setHorizontalSpacing(10)
        self.layoutFormulario.setObjectName("layoutFormulario")
        self.txtUsuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtUsuario.setInputMethodHints(QtCore.Qt.ImhNone)
        self.font = QFont()
        self.font.setCapitalization(QFont.AllUppercase)
        self.txtUsuario.setFont(self.font)
        self.txtUsuario.setInputMask("")
        self.txtUsuario.setText("")
        self.txtUsuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtUsuario.setObjectName("txtUsuario")

        self.layoutFormulario.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUsuario)
        self.labelContrasena = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelContrasena.setFont(font)
        self.labelContrasena.setObjectName("labelContrasena")
        self.layoutFormulario.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelContrasena)
        self.txtContrasena = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtContrasena.setObjectName("txtContrasena")
        self.layoutFormulario.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtContrasena)
        self.labelUsuario = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelUsuario.setFont(font)
        self.labelUsuario.setObjectName("labelUsuario")
        self.layoutFormulario.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUsuario)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutFormulario.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(560, 80, 121, 85))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 9, 0, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnIniciarSesion = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnIniciarSesion.setFont(font)
        self.btnIniciarSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnIniciarSesion.setStyleSheet("")
        self.btnIniciarSesion.setObjectName("btnIniciarSesion")
        self.verticalLayout.addWidget(self.btnIniciarSesion)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btnCancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet("")
        self.btnCancelar.setAutoDefault(False)
        self.btnCancelar.setDefault(False)
        self.btnCancelar.setFlat(False)
        self.btnCancelar.setObjectName("btnCancelar")
        self.verticalLayout.addWidget(self.btnCancelar)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 20, 531, 50))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutTitulo = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutTitulo.setContentsMargins(0, 0, 0, 0)
        self.layoutTitulo.setSpacing(22)
        self.layoutTitulo.setObjectName("layoutTitulo")
        self.labelLogin = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogin.setObjectName("labelLogin")
        self.layoutTitulo.addWidget(self.labelLogin)
        self.btnImagen = QtWidgets.QPushButton(self.centralwidget)
        self.btnImagen.setGeometry(QtCore.QRect(4, 0, 143, 187))
        self.btnImagen.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "..\icons\parking-idea.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImagen.setIcon(icon1)
        self.btnImagen.setIconSize(QtCore.QSize(140, 180))
        self.btnImagen.setObjectName("btnImagen")
        self.formLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.labelLogin.raise_()
        self.btnImagen.raise_()
        VentanaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaLogin)
        QtCore.QMetaObject.connectSlotsByName(VentanaLogin)
        VentanaLogin.setTabOrder(self.txtUsuario, self.txtContrasena)
        VentanaLogin.setTabOrder(self.txtContrasena, self.btnIniciarSesion)
        VentanaLogin.setTabOrder(self.btnIniciarSesion, self.btnCancelar)

    def retranslateUi(self, VentanaLogin):
        _translate = QtCore.QCoreApplication.translate
        VentanaLogin.setWindowTitle(_translate("VentanaLogin", "Parking - Inicio de Sesión"))
        self.labelContrasena.setText(_translate("VentanaLogin", "Contraseña :"))
        self.labelUsuario.setText(_translate("VentanaLogin", "Usuario :"))
        self.btnIniciarSesion.setText(_translate("VentanaLogin", "Entrar"))
        self.btnCancelar.setText(_translate("VentanaLogin", "Salir"))
        self.labelLogin.setText(_translate("VentanaLogin", "PARQUEADERO EL NIÑO JAIR"))
