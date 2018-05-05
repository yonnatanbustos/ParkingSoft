# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaRA.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaRA(object):
    def setupUi(self, VentanaRA):
        VentanaRA.setObjectName("VentanaRA")
        VentanaRA.resize(800, 600)
        VentanaRA.setMaximumSize(QtCore.QSize(1400, 730))
        VentanaRA.setStyleSheet("QTableWidget{\n"
"font: 13pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit{\n"
"font: 18px \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(VentanaRA)
        self.centralwidget.setObjectName("centralwidget")
        self.tableVehiculos = QtWidgets.QTableWidget(self.centralwidget)
        self.tableVehiculos.setGeometry(QtCore.QRect(30, 80, 741, 501))
        self.tableVehiculos.setLineWidth(1)
        self.tableVehiculos.setAutoScrollMargin(10)
        self.tableVehiculos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableVehiculos.setAlternatingRowColors(True)
        self.tableVehiculos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableVehiculos.setGridStyle(QtCore.Qt.SolidLine)
        self.tableVehiculos.setRowCount(0)
        self.tableVehiculos.setObjectName("tableVehiculos")
        self.tableVehiculos.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableVehiculos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableVehiculos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableVehiculos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        font.setCapitalization(QtGui.QFont.AllUppercase)
        self.tableVehiculos.setHorizontalHeaderItem(3, item)
        self.tableVehiculos.horizontalHeader().setDefaultSectionSize(184)
        self.tableVehiculos.horizontalHeader().setMinimumSectionSize(70)
        self.txtBuscar = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBuscar.setGeometry(QtCore.QRect(30, 29, 741, 31))
        self.txtBuscar.setText("")
        self.txtBuscar.setMaxLength(7)
        self.txtBuscar.setFont(font)
        self.txtBuscar.setObjectName("txtBuscar")
        VentanaRA.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaRA)
        QtCore.QMetaObject.connectSlotsByName(VentanaRA)

    def retranslateUi(self, VentanaRA):
        _translate = QtCore.QCoreApplication.translate
        VentanaRA.setWindowTitle(_translate("VentanaRA", "Lista de Vehiculos"))
        self.tableVehiculos.setSortingEnabled(False)
        item = self.tableVehiculos.horizontalHeaderItem(0)
        item.setText(_translate("VentanaRA", "Placa"))
        item = self.tableVehiculos.horizontalHeaderItem(1)
        item.setText(_translate("VentanaRA", "Hora Entrada"))
        item = self.tableVehiculos.horizontalHeaderItem(2)
        item.setText(_translate("VentanaRA", "Fecha Entrada"))
        item = self.tableVehiculos.horizontalHeaderItem(3)
        item.setText(_translate("VentanaRA", "Tipo Vehiculo"))

