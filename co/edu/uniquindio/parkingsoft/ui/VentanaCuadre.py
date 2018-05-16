# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaCuadre.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaCuadre(object):
    def setupUi(self, VentanaCuadre):
        VentanaCuadre.setObjectName("VentanaCuadre")
        VentanaCuadre.resize(441, 241)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaCuadre.sizePolicy().hasHeightForWidth())
        VentanaCuadre.setSizePolicy(sizePolicy)
        VentanaCuadre.setMinimumSize(QtCore.QSize(441, 241))
        VentanaCuadre.setMaximumSize(QtCore.QSize(441, 241))
        VentanaCuadre.setSizeIncrement(QtCore.QSize(440, 240))
        VentanaCuadre.setStyleSheet("QLineEdit{\n"
"font: 13px \"Tahoma\";\n"
"font-size: 60px;\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"font: 13pt \"Tahoma\";\n"
"}\n"
"#labelCuadre{\n"
"font-size: 60px;\n"
"}\n"
"QPushButton{\n"
"font: 13pt \"Tahoma\";\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0c80c4;\n"
"}")
        VentanaCuadre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        VentanaCuadre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelCuadre = QtWidgets.QLabel(VentanaCuadre)
        self.labelCuadre.setGeometry(QtCore.QRect(0, 10, 441, 61))
        self.labelCuadre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCuadre.setObjectName("labelCuadre")
        self.txtTotalCuadre = QtWidgets.QLineEdit(VentanaCuadre)
        self.txtTotalCuadre.setGeometry(QtCore.QRect(120, 110, 301, 61))
        self.txtTotalCuadre.setFrame(True)
        self.txtTotalCuadre.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtTotalCuadre.setDragEnabled(False)
        self.txtTotalCuadre.setReadOnly(True)
        self.txtTotalCuadre.setObjectName("txtTotalCuadre")
        self.labelEfectivo = QtWidgets.QLabel(VentanaCuadre)
        self.labelEfectivo.setGeometry(QtCore.QRect(10, 110, 81, 61))
        self.labelEfectivo.setObjectName("labelEfectivo")
        self.btnImprimirCuadre = QtWidgets.QPushButton(VentanaCuadre)
        self.btnImprimirCuadre.setGeometry(QtCore.QRect(290, 180, 131, 51))
        self.btnImprimirCuadre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../images/icon-imprimir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimirCuadre.setIcon(icon)
        self.btnImprimirCuadre.setIconSize(QtCore.QSize(50, 50))
        self.btnImprimirCuadre.setObjectName("btnImprimirCuadre")

        self.retranslateUi(VentanaCuadre)
        QtCore.QMetaObject.connectSlotsByName(VentanaCuadre)

    def retranslateUi(self, VentanaCuadre):
        _translate = QtCore.QCoreApplication.translate
        VentanaCuadre.setWindowTitle(_translate("VentanaCuadre", "Cierre de Caja"))
        self.labelCuadre.setText(_translate("VentanaCuadre", "Cuadre Diario"))
        self.labelEfectivo.setText(_translate("VentanaCuadre", "Efectivo:"))
        self.btnImprimirCuadre.setText(_translate("VentanaCuadre", "Imprimir"))

