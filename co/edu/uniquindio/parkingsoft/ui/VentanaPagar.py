# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pagar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaPagar(object):
    def setupUi(self, ventanaPagar):
        ventanaPagar.setObjectName("ventanaPagar")
        ventanaPagar.resize(706, 310)
        ventanaPagar.setMaximumSize(QtCore.QSize(706, 310))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-pagar.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventanaPagar.setWindowIcon(icon)
        ventanaPagar.setLayoutDirection(QtCore.Qt.LeftToRight)
        ventanaPagar.setStyleSheet("QLineEdit{\n"
                                   "font: 13px \"Tahoma\";\n"
                                   "border:1px solid black;\n"
                                   "border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "QLabel{\n"
                                   "font: 13pt \"Tahoma\";\n"
                                   "}\n"
                                   "\n"
                                   "#labelTotalPagar{\n"
                                   "background-color: #0c80c4;\n"
                                   "}\n"
                                   "\n"
                                   "#labelValor, #labelTotalPagar{\n"
                                   "font-size: 60px;\n"
                                   "}\n"
                                   "\n"
                                   "#txtValor{\n"
                                   "QPushButton:hover{\n"
                                   "background-color: #0c80c4;\n"
                                   "}")
        self.centralwidget = QtWidgets.QWidget(ventanaPagar)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 210, 341, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtTiempo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtTiempo.setEnabled(False)
        self.txtTiempo.setObjectName("txtTiempo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtTiempo)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtDescuento = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtDescuento.setEnabled(False)
        self.txtDescuento.setObjectName("txtDescuento")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtDescuento)
        self.txtCambio = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCambio.setEnabled(False)
        self.txtCambio.setObjectName("txtCambio")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtCambio)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 119, 661, 78))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelValor = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout_2.addWidget(self.labelValor, 0, 0, 1, 1)
        self.txtValor = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtValor.setObjectName("txtValor")
        self.gridLayout_2.addWidget(self.txtValor, 0, 1, 1, 1)
        self.btnImprimir = QtWidgets.QPushButton(self.centralwidget)
        self.btnImprimir.setGeometry(QtCore.QRect(554, 210, 131, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-imprimir.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimir.setIcon(icon1)
        self.btnImprimir.setIconSize(QtCore.QSize(50, 50))
        self.btnImprimir.setObjectName("btnImprimir")
        self.btnVolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnVolver.setGeometry(QtCore.QRect(20, 10, 121, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVolver.sizePolicy().hasHeightForWidth())
        self.btnVolver.setSizePolicy(sizePolicy)
        self.btnVolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-volver.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVolver.setIcon(icon2)
        self.btnVolver.setIconSize(QtCore.QSize(50, 50))
        self.btnVolver.setObjectName("btnVolver")
        self.labelTotalPagar = QtWidgets.QLabel(self.centralwidget)
        self.labelTotalPagar.setEnabled(True)
        self.labelTotalPagar.setGeometry(QtCore.QRect(170, 10, 511, 89))
        self.labelTotalPagar.setStyleSheet("border:1px solid black;\n"
                                           "border-radius: 5px;")
        self.labelTotalPagar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTotalPagar.setObjectName("labelTotalPagar")
        ventanaPagar.setCentralWidget(self.centralwidget)
        self.actionParqueadero = QtWidgets.QAction(ventanaPagar)
        self.actionParqueadero.setObjectName("actionParqueadero")

        self.retranslateUi(ventanaPagar)
        QtCore.QMetaObject.connectSlotsByName(ventanaPagar)

    def retranslateUi(self, ventanaPagar):
        _translate = QtCore.QCoreApplication.translate
        ventanaPagar.setWindowTitle(_translate("ventanaPagar", "Pagar"))
        self.label_2.setText(_translate("ventanaPagar", "Tiempo :"))
        self.label_3.setText(_translate("ventanaPagar", "Descuento :"))
        self.label_4.setText(_translate("ventanaPagar", "Cambio :"))
        self.labelValor.setText(_translate("ventanaPagar", "Valor :"))
        self.btnImprimir.setText(_translate("ventanaPagar", "Imprimir"))
        self.btnVolver.setText(_translate("ventanaPagar", "Volver"))
        self.labelTotalPagar.setText(_translate("ventanaPagar", "0"))
        self.actionParqueadero.setText(_translate("ventanaPagar", "Parqueadero"))
