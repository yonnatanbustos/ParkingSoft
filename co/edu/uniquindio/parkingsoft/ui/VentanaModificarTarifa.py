# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaModificarTarifa.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaModificarTarifa(object):
    def setupUi(self, VentanaModificarTarifa):
        VentanaModificarTarifa.setObjectName("VentanaModificarTarifa")
        VentanaModificarTarifa.resize(800, 350)
        VentanaModificarTarifa.setMaximumSize(QtCore.QSize(800, 350))
        VentanaModificarTarifa.setStyleSheet("QLabel{\n"
"font: 20pt \"Tahoma\";\n"
"}\n"
"\n"
"QLineEdit, QPushButton{\n"
"font: 20pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#labelModificarTarifa{\n"
"font: 40pt \"Tahoma\";\n"
"}\n"
"\n"
"#labelTarifaActual, #labelNuevaTarifa{\n"
"font: 25pt \"Tahoma\";\n"
"}\n"
"\n"
"#btnGuardar:hover{\n"
"background-color: #2aff27;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(VentanaModificarTarifa)
        self.centralwidget.setObjectName("centralwidget")
        self.labelModificarTarifa = QtWidgets.QLabel(self.centralwidget)
        self.labelModificarTarifa.setGeometry(QtCore.QRect(30, 20, 741, 61))
        self.labelModificarTarifa.setAlignment(QtCore.Qt.AlignCenter)
        self.labelModificarTarifa.setObjectName("labelModificarTarifa")
        self.labelTarifaActual = QtWidgets.QLabel(self.centralwidget)
        self.labelTarifaActual.setGeometry(QtCore.QRect(30, 130, 351, 41))
        self.labelTarifaActual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTarifaActual.setObjectName("labelTarifaActual")
        self.labelNuevaTarifa = QtWidgets.QLabel(self.centralwidget)
        self.labelNuevaTarifa.setGeometry(QtCore.QRect(440, 130, 341, 41))
        self.labelNuevaTarifa.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNuevaTarifa.setObjectName("labelNuevaTarifa")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 190, 351, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtActualCarro = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtActualCarro.setEnabled(False)
        self.txtActualCarro.setObjectName("txtActualCarro")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtActualCarro)
        self.txtActualMoto = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtActualMoto.setEnabled(False)
        self.txtActualMoto.setObjectName("txtActualMoto")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtActualMoto)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(440, 190, 341, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtNuevoCarro = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtNuevoCarro.setMaxLength(5)
        self.txtNuevoCarro.setFrame(False)
        self.txtNuevoCarro.setObjectName("txtNuevoCarro")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtNuevoCarro)
        self.txtNuevoMoto = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtNuevoMoto.setInputMask("")
        self.txtNuevoMoto.setMaxLength(32767)
        self.txtNuevoMoto.setObjectName("txtNuevoMoto")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNuevoMoto)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 130, 20, 211))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(540, 290, 171, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon)
        self.btnGuardar.setIconSize(QtCore.QSize(50, 50))
        self.btnGuardar.setObjectName("btnGuardar")
        VentanaModificarTarifa.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaModificarTarifa)
        QtCore.QMetaObject.connectSlotsByName(VentanaModificarTarifa)

    def retranslateUi(self, VentanaModificarTarifa):
        _translate = QtCore.QCoreApplication.translate
        VentanaModificarTarifa.setWindowTitle(_translate("VentanaModificarTarifa", "Modificar Tarifa"))
        self.labelModificarTarifa.setText(_translate("VentanaModificarTarifa", "MODIFICAR TARIFA"))
        self.labelTarifaActual.setText(_translate("VentanaModificarTarifa", "TARIFA ACTUAL"))
        self.labelNuevaTarifa.setText(_translate("VentanaModificarTarifa", "NUEVA TARIFA"))
        self.label_2.setText(_translate("VentanaModificarTarifa", "CARRO :"))
        self.label_3.setText(_translate("VentanaModificarTarifa", "MOTO :"))
        self.label_5.setText(_translate("VentanaModificarTarifa", "CARRO :"))
        self.label_6.setText(_translate("VentanaModificarTarifa", "MOTO :"))
        self.btnGuardar.setText(_translate("VentanaModificarTarifa", "Guardar"))

