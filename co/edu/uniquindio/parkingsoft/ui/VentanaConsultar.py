# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaConsultar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaConsultar(object):
    def setupUi(self, VentanaConsultar):
        VentanaConsultar.setObjectName("VentanaConsultar")
        VentanaConsultar.resize(780, 465)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaConsultar.sizePolicy().hasHeightForWidth())
        VentanaConsultar.setSizePolicy(sizePolicy)
        VentanaConsultar.setMinimumSize(QtCore.QSize(780, 465))
        VentanaConsultar.setMaximumSize(QtCore.QSize(780, 465))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../co/edu/uniquindio/parkingsoft/icons/icon-buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaConsultar.setWindowIcon(icon)
        VentanaConsultar.setStyleSheet("QLabel{\n"
"font: 18pt \"Tahoma\";\n"
"}\n"
"\n"
"QLineEdit, QDateEdit, QPushButton{\n"
"font: 18px \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0c80c4;\n"
"}\n"
"QTableWidget{\n"
"font: 13pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px\n"
"}\n"
"QGroupBox{\n"
"font: 13pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px\n"
"}")
        VentanaConsultar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        VentanaConsultar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableTiquetesSalida = QtWidgets.QTableWidget(VentanaConsultar)
        self.tableTiquetesSalida.setGeometry(QtCore.QRect(10, 121, 761, 341))
        self.tableTiquetesSalida.setObjectName("tableTiquetesSalida")
        self.tableTiquetesSalida.setColumnCount(6)
        self.tableTiquetesSalida.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableTiquetesSalida.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableTiquetesSalida.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableTiquetesSalida.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableTiquetesSalida.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableTiquetesSalida.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableTiquetesSalida.setHorizontalHeaderItem(5, item)
        self.tableTiquetesSalida.horizontalHeader().setCascadingSectionResizes(False)
        self.tableTiquetesSalida.horizontalHeader().setDefaultSectionSize(126)
        self.groupBox = QtWidgets.QGroupBox(VentanaConsultar)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 761, 101))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 551, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtFechaInicial = QtWidgets.QDateEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFechaInicial.sizePolicy().hasHeightForWidth())
        self.txtFechaInicial.setSizePolicy(sizePolicy)
        self.txtFechaInicial.setMinimumDate(QtCore.QDate(2018, 1, 1))
        self.txtFechaInicial.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.txtFechaInicial.setCalendarPopup(True)
        self.txtFechaInicial.setObjectName("txtFechaInicial")
        self.gridLayout.addWidget(self.txtFechaInicial, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.txtFechaFin = QtWidgets.QDateEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtFechaFin.sizePolicy().hasHeightForWidth())
        self.txtFechaFin.setSizePolicy(sizePolicy)
        self.txtFechaFin.setMinimumDate(QtCore.QDate(2018, 1, 1))
        self.txtFechaFin.setCalendarPopup(True)
        self.txtFechaFin.setObjectName("txtFechaFin")
        self.gridLayout.addWidget(self.txtFechaFin, 0, 3, 1, 1)
        self.btnFiltar = QtWidgets.QPushButton(self.groupBox)
        self.btnFiltar.setGeometry(QtCore.QRect(610, 20, 131, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../images/icon-filtro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFiltar.setIcon(icon1)
        self.btnFiltar.setIconSize(QtCore.QSize(50, 50))
        self.btnFiltar.setObjectName("btnFiltar")

        self.retranslateUi(VentanaConsultar)
        QtCore.QMetaObject.connectSlotsByName(VentanaConsultar)

    def retranslateUi(self, VentanaConsultar):
        _translate = QtCore.QCoreApplication.translate
        VentanaConsultar.setWindowTitle(_translate("VentanaConsultar", "Consultar"))
        self.tableTiquetesSalida.setSortingEnabled(False)
        item = self.tableTiquetesSalida.horizontalHeaderItem(0)
        item.setText(_translate("VentanaConsultar", "Numero Factura"))
        item = self.tableTiquetesSalida.horizontalHeaderItem(1)
        item.setText(_translate("VentanaConsultar", "Hora"))
        item = self.tableTiquetesSalida.horizontalHeaderItem(2)
        item.setText(_translate("VentanaConsultar", "Fecha"))
        item = self.tableTiquetesSalida.horizontalHeaderItem(3)
        item.setText(_translate("VentanaConsultar", "Valor"))
        item = self.tableTiquetesSalida.horizontalHeaderItem(4)
        item.setText(_translate("VentanaConsultar", "Cajero"))
        item = self.tableTiquetesSalida.horizontalHeaderItem(5)
        item.setText(_translate("VentanaConsultar", "Seleccionar"))
        self.groupBox.setTitle(_translate("VentanaConsultar", "Filtros"))
        self.label.setText(_translate("VentanaConsultar", "Fecha Inicial:"))
        self.label_2.setText(_translate("VentanaConsultar", "Fecha Fin:"))
        self.btnFiltar.setText(_translate("VentanaConsultar", "Flitar"))

