# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistrarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# UI de la ventana de usuario
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 447)
        MainWindow.setMaximumSize(QtCore.QSize(695, 447))
        MainWindow.setStyleSheet("QLineEdit, QPushButton{\n"
"font: 18px \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"font: 18px \"Tahoma\";\n"
"}\n"
"\n"
"#labelRegistrarEmpleado{\n"
"font-size:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0c80c4;\n"
"}\n"
"\n"
"#btnGuardar:hover{\n"
"background-color: #2aff27;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 100, 641, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 10, 5, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtCedula = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCedula.setMaxLength(15)
        self.txtCedula.setObjectName("txtCedula")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtCedula)
        self.txtNombres = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNombres.setObjectName("txtNombres")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNombres)
        self.txtApellidos = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtApellidos.setObjectName("txtApellidos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtApellidos)
        self.txtNombreUsuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNombreUsuario.setMaxLength(15)
        self.txtNombreUsuario.setObjectName("txtNombreUsuario")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtNombreUsuario)
        self.txtPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPassword.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtPassword.setMaxLength(15)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txtPassword.setObjectName("txtPassword")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtPassword)
        self.txtConfirmPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtConfirmPassword.setMaxLength(15)
        self.txtConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtConfirmPassword)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 20, 491, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelRegistrarEmpleado = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRegistrarEmpleado.sizePolicy().hasHeightForWidth())
        self.labelRegistrarEmpleado.setSizePolicy(sizePolicy)
        self.labelRegistrarEmpleado.setTextFormat(QtCore.Qt.AutoText)
        self.labelRegistrarEmpleado.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRegistrarEmpleado.setObjectName("labelRegistrarEmpleado")
        self.gridLayout.addWidget(self.labelRegistrarEmpleado, 1, 0, 1, 1)
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(260, 330, 141, 61))
        self.btnGuardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/ParkingSoft/co/edu/uniquindio/parkingsoft/icons/icon-guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon)
        self.btnGuardar.setIconSize(QtCore.QSize(50, 50))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnVolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnVolver.setGeometry(QtCore.QRect(20, 20, 141, 51))
        self.btnVolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVolver.setFocusPolicy(QtCore.Qt.WheelFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/ParkingSoft/co/edu/uniquindio/parkingsoft/icons/icon-volver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVolver.setIcon(icon1)
        self.btnVolver.setIconSize(QtCore.QSize(50, 50))
        self.btnVolver.setObjectName("btnVolver")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cedula :"))
        self.label_2.setText(_translate("MainWindow", "Nombres :"))
        self.label_3.setText(_translate("MainWindow", "Apellidos :"))
        self.label_4.setText(_translate("MainWindow", "Nombre de Usuario :"))
        self.label_5.setText(_translate("MainWindow", "Contraseña :"))
        self.label_6.setText(_translate("MainWindow", "Confirmar Contraseña :"))
        self.labelRegistrarEmpleado.setText(_translate("MainWindow", "REGISTRAR UN EMPLEADO"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar"))
        self.btnVolver.setText(_translate("MainWindow", "Volver"))

