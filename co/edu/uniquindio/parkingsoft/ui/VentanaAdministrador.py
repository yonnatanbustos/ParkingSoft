# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAdministrador.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# UI de la ventana principal de administrador
class Ui_PrincipalAdministrador(object):
    def setupUi(self, PrincipalAdministrador):
        PrincipalAdministrador.setObjectName("PrincipalAdministrador")
        PrincipalAdministrador.setWindowModality(QtCore.Qt.NonModal)
        PrincipalAdministrador.setEnabled(True)
        PrincipalAdministrador.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PrincipalAdministrador.sizePolicy().hasHeightForWidth())
        PrincipalAdministrador.setSizePolicy(sizePolicy)
        PrincipalAdministrador.setBaseSize(QtCore.QSize(0, 0))
        PrincipalAdministrador.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhPreferUppercase)
        PrincipalAdministrador.setIconSize(QtCore.QSize(0, 0))
        PrincipalAdministrador.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        PrincipalAdministrador.setDocumentMode(False)
        PrincipalAdministrador.setTabShape(QtWidgets.QTabWidget.Triangular)
        PrincipalAdministrador.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        PrincipalAdministrador.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(PrincipalAdministrador)
        self.centralwidget.setObjectName("centralwidget")
        PrincipalAdministrador.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PrincipalAdministrador)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(22)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QtCore.QSize(15, 19))
        self.menubar.setSizeIncrement(QtCore.QSize(16, 9))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.menubar.setFont(font)
        self.menubar.setMouseTracking(True)
        self.menubar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setToolTipDuration(20)
        self.menubar.setStatusTip("")
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuSistema = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuSistema.sizePolicy().hasHeightForWidth())
        self.menuSistema.setSizePolicy(sizePolicy)
        self.menuSistema.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuSistema.setFont(font)
        self.menuSistema.setToolTipDuration(0)
        self.menuSistema.setTearOffEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-sistema.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSistema.setIcon(icon)
        self.menuSistema.setSeparatorsCollapsible(True)
        self.menuSistema.setToolTipsVisible(True)
        self.menuSistema.setObjectName("menuSistema")
        self.menuAydua = QtWidgets.QMenu(self.menubar)
        self.menuAydua.setGeometry(QtCore.QRect(287, 126, 200, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuAydua.sizePolicy().hasHeightForWidth())
        self.menuAydua.setSizePolicy(sizePolicy)
        self.menuAydua.setTitle("Aydua")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-ayuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAydua.setIcon(icon1)
        self.menuAydua.setToolTipsVisible(False)
        self.menuAydua.setObjectName("menuAydua")
        self.menuSalir = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.menuSalir.setFont(font)
        self.menuSalir.setTearOffEnabled(False)
        icon = QtGui.QIcon.fromTheme("Salir")
        self.menuSalir.setIcon(icon)
        self.menuSalir.setSeparatorsCollapsible(False)
        self.menuSalir.setObjectName("menuSalir")
        self.menuAjustes = QtWidgets.QMenu(self.menubar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-ajustes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAjustes.setIcon(icon2)
        self.menuAjustes.setObjectName("menuAjustes")
        PrincipalAdministrador.setMenuBar(self.menubar)
        self.btnParqueadero = QtWidgets.QAction(PrincipalAdministrador)
        self.btnParqueadero.setCheckable(False)
        self.btnParqueadero.setChecked(False)
        self.btnParqueadero.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-sistema.parqueadero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnParqueadero.setIcon(icon3)
        self.btnParqueadero.setIconVisibleInMenu(True)
        self.btnParqueadero.setObjectName("btnParqueadero")
        self.btnInventarioCaja = QtWidgets.QAction(PrincipalAdministrador)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-inventario-caja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInventarioCaja.setIcon(icon4)
        self.btnInventarioCaja.setObjectName("btnInventarioCaja")
        self.btnRegistrarEmpleado = QtWidgets.QAction(PrincipalAdministrador)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-registrar-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegistrarEmpleado.setIcon(icon5)
        self.btnRegistrarEmpleado.setObjectName("btnRegistrarEmpleado")
        self.btnModificarTarifa = QtWidgets.QAction(PrincipalAdministrador)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificarTarifa.setIcon(icon6)
        self.btnModificarTarifa.setObjectName("btnModificarTarifa")
        self.btnManualUsuario = QtWidgets.QAction(PrincipalAdministrador)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("F:/UQ/2018-1/VIII. Ingenieria de Software III/ProyectoFinal/Parqueadero/images/icon-manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnManualUsuario.setIcon(icon7)
        self.btnManualUsuario.setObjectName("btnManualUsuario")
        self.menuSistema.addAction(self.btnParqueadero)
        self.menuSistema.addSeparator()
        self.menuSistema.addAction(self.btnInventarioCaja)
        self.menuSistema.addSeparator()
        self.menuAydua.addAction(self.btnManualUsuario)
        self.menuAjustes.addAction(self.btnRegistrarEmpleado)
        self.menuAjustes.addSeparator()
        self.menuAjustes.addAction(self.btnModificarTarifa)
        self.menubar.addAction(self.menuSistema.menuAction())
        self.menubar.addAction(self.menuAydua.menuAction())
        self.menubar.addAction(self.menuAjustes.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())

        self.retranslateUi(PrincipalAdministrador)
        QtCore.QMetaObject.connectSlotsByName(PrincipalAdministrador)

    def retranslateUi(self, PrincipalAdministrador):
        _translate = QtCore.QCoreApplication.translate
        PrincipalAdministrador.setWindowTitle(_translate("PrincipalAdministrador", "Principal - Adminstrador"))
        self.menuSistema.setTitle(_translate("PrincipalAdministrador", "Sistema"))
        self.menuSalir.setTitle(_translate("PrincipalAdministrador", "Salir"))
        self.menuAjustes.setTitle(_translate("PrincipalAdministrador", "Ajustes"))
        self.btnParqueadero.setText(_translate("PrincipalAdministrador", "Parqueadero"))
        self.btnInventarioCaja.setText(_translate("PrincipalAdministrador", "Inventarios de caja"))
        self.btnRegistrarEmpleado.setText(_translate("PrincipalAdministrador", "Registrar Empleado"))
        self.btnModificarTarifa.setText(_translate("PrincipalAdministrador", "Modificar Tarifa"))
        self.btnManualUsuario.setText(_translate("PrincipalAdministrador", "Manual de Usuario"))

