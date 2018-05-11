# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mensualidad.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

# UI de la ventana de las mensualidades
class Ui_MainWindow(object):
    font : QFont

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 728)
        MainWindow.setMaximumSize(QtCore.QSize(1400, 732))
        MainWindow.setStyleSheet("QLabel{\n"
"font: 18pt \"Tahoma\";\n"
"}\n"
"\n"
"QLineEdit,QComboBox, QDateEdit, QPushButton{\n"
"font: 18px \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#labelMenusalidad{\n"
"font-size: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0c80c4;\n"
"}\n"
"\n"
"#btnGuardar:hover{\n"
"background-color: #2aff27;\n"
"}\n"
"\n"
"#btnEliminar:hover{\n"
"background-color: #ff0000;\n"
"}\n"
"\n"
"QGroupBox{\n"
"font: 13pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QTableWidget{\n"
"font: 13pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 10, 1181, 74))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelMenusalidad = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelMenusalidad.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMenusalidad.setObjectName("labelMenusalidad")
        self.gridLayout.addWidget(self.labelMenusalidad, 0, 0, 1, 1)
        self.tableMensualidades = QtWidgets.QTableWidget(self.centralwidget)
        self.tableMensualidades.setGeometry(QtCore.QRect(160, 90, 1181, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableMensualidades.sizePolicy().hasHeightForWidth())
        self.tableMensualidades.setSizePolicy(sizePolicy)
        self.tableMensualidades.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableMensualidades.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableMensualidades.setAutoScrollMargin(10)
        self.tableMensualidades.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableMensualidades.setProperty("showDropIndicator", False)
        self.tableMensualidades.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableMensualidades.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableMensualidades.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableMensualidades.setCornerButtonEnabled(True)
        self.tableMensualidades.setObjectName("tableMensualidades")
        self.tableMensualidades.setColumnCount(8)
        self.tableMensualidades.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableMensualidades.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableMensualidades.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableMensualidades.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMensualidades.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableMensualidades.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableMensualidades.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableMensualidades.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        item.setFont(font)
        self.tableMensualidades.setHorizontalHeaderItem(7, item)
        self.tableMensualidades.horizontalHeader().setVisible(True)
        self.tableMensualidades.horizontalHeader().setCascadingSectionResizes(False)
        self.tableMensualidades.horizontalHeader().setDefaultSectionSize(146)
        self.tableMensualidades.horizontalHeader().setMinimumSectionSize(50)
        self.tableMensualidades.verticalHeader().setMinimumSectionSize(30)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 131, 211))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnNuevo = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\icons\icon-agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon)
        self.btnNuevo.setIconSize(QtCore.QSize(50, 50))
        self.btnNuevo.setObjectName("btnNuevo")
        self.gridLayout_3.addWidget(self.btnNuevo, 0, 0, 1, 1)
        self.btnActualizar = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("..\icons\icon-modificar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnActualizar.setIcon(icon1)
        self.btnActualizar.setIconSize(QtCore.QSize(50, 50))
        self.btnActualizar.setObjectName("btnActualizar")
        self.gridLayout_3.addWidget(self.btnActualizar, 1, 0, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("..\icons\icon-eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon2)
        self.btnEliminar.setIconSize(QtCore.QSize(50, 50))
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_3.addWidget(self.btnEliminar, 2, 0, 1, 1)
        self.grupoInformacion = QtWidgets.QGroupBox(self.centralwidget)
        self.grupoInformacion.setGeometry(QtCore.QRect(20, 350, 1321, 331))
        self.grupoInformacion.setFlat(False)
        self.grupoInformacion.setCheckable(False)
        self.grupoInformacion.setObjectName("grupoInformacion")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.grupoInformacion)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 1301, 237))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.txtFechaEntrada = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.txtFechaEntrada.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.txtFechaEntrada.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.txtFechaEntrada.setProperty("showGroupSeparator", False)
        self.txtFechaEntrada.setMinimumDate(QtCore.QDate(2017, 4, 1))
        self.txtFechaEntrada.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.txtFechaEntrada.setCalendarPopup(True)
        self.txtFechaEntrada.setDate(QtCore.QDate(2017, 9, 6))
        self.txtFechaEntrada.setObjectName("txtFechaEntrada")
        self.gridLayout_2.addWidget(self.txtFechaEntrada, 2, 1, 1, 1)
        self.txtFechaSalida = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.txtFechaSalida.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFechaSalida.setAccelerated(False)
        self.txtFechaSalida.setMinimumDate(QtCore.QDate(2017, 4, 1))
        self.txtFechaSalida.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.txtFechaSalida.setCalendarPopup(True)
        self.txtFechaSalida.setCurrentSectionIndex(1)
        self.txtFechaSalida.setTimeSpec(QtCore.Qt.LocalTime)
        self.txtFechaSalida.setObjectName("txtFechaSalida")
        self.gridLayout_2.addWidget(self.txtFechaSalida, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        self.font = QFont()
        self.font.setCapitalization(QFont.AllUppercase)
        self.txtPropietario = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtPropietario.setMaxLength(50)
        self.txtPropietario.setObjectName("txtPropietario")
        self.txtPropietario.setFont(self.font)
        self.gridLayout_2.addWidget(self.txtPropietario, 1, 1, 1, 1)
        self.txtTelefono = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtTelefono.setMaxLength(15)
        self.txtTelefono.setObjectName("txtTelefono")
        self.txtTelefono.setFont(self.font)
        self.gridLayout_2.addWidget(self.txtTelefono, 1, 3, 1, 1)
        self.txtPlaca = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtPlaca.setMaxLength(7)
        self.txtPlaca.setObjectName("txtPlaca")
        self.txtPlaca.setFont(self.font)
        self.gridLayout_2.addWidget(self.txtPlaca, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.comboTipo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboTipo.setObjectName("comboTipo")
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.gridLayout_2.addWidget(self.comboTipo, 0, 3, 1, 1)
        self.btnGuardar = QtWidgets.QPushButton(self.grupoInformacion)
        self.btnGuardar.setGeometry(QtCore.QRect(510, 270, 151, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("..\icons\icon-guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon3)
        self.btnGuardar.setIconSize(QtCore.QSize(50, 50))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnVolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnVolver.setGeometry(QtCore.QRect(10, 12, 131, 71))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("..\icons\icon-volver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVolver.setIcon(icon4)
        self.btnVolver.setIconSize(QtCore.QSize(50, 50))
        self.btnVolver.setObjectName("btnVolver")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelMenusalidad.setText(_translate("MainWindow", "MENSUALIDADES"))
        item = self.tableMensualidades.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.tableMensualidades.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Placa"))
        item = self.tableMensualidades.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tableMensualidades.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Propietario"))
        item = self.tableMensualidades.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tableMensualidades.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.tableMensualidades.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Fecha Entrada"))
        item = self.tableMensualidades.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fecha Salida"))
        self.btnNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.btnActualizar.setText(_translate("MainWindow", "Modificar"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.grupoInformacion.setTitle(_translate("MainWindow", "Información"))
        self.label_3.setText(_translate("MainWindow", "Tipo :"))
        self.label_5.setText(_translate("MainWindow", "Telefono :"))
        self.label_2.setText(_translate("MainWindow", "Placa :"))
        self.label_6.setText(_translate("MainWindow", "Fecha Entrada :"))
        self.label_7.setText(_translate("MainWindow", "Fecha Salida :"))
        self.label_4.setText(_translate("MainWindow", "Propietario :"))
        self.comboTipo.setItemText(0, _translate("MainWindow", "CARRO_MENS"))
        self.comboTipo.setItemText(1, _translate("MainWindow", "MOTO_MENS"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar"))
        self.btnVolver.setText(_translate("MainWindow", "Volver"))

