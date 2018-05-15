# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


# UI de la ventana principal de empleado
class Ui_Principal(object):
    font: QFont

    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.setWindowModality(QtCore.Qt.WindowModal)
        Principal.setEnabled(True)
        Principal.resize(1400, 697)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Principal.sizePolicy().hasHeightForWidth())
        Principal.setSizePolicy(sizePolicy)
        Principal.setMinimumSize(QtCore.QSize(1400, 650))
        Principal.setSizeIncrement(QtCore.QSize(0, 0))
        Principal.setFocusPolicy(QtCore.Qt.NoFocus)
        Principal.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Principal.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\icons\icons-página-principal-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Principal.setWindowIcon(icon)
        Principal.setStyleSheet("QLabel{\n"
                                "font: 18pt \"Tahoma\";\n"
                                "}\n"
                                "\n"
                                "QLineEdit,QComboBox{\n"
                                "font: 18px \"Tahoma\";\n"
                                "border:1px solid black;\n"
                                "border-radius: 5px;\n"
                                "\n"
                                "}\n"
                                "#labelTotalPagar{\n"
                                "background-color: #0c80c4;\n"
                                "}\n"
                                "\n"
                                "#labelPlaca, #labelTotalPagar{\n"
                                "font-size: 60px;\n"
                                "}\n"
                                "\n"
                                "#txtPlaca{\n"
                                "font-size:60px;\n"
                                "border:1px solid black;\n"
                                "border-radius: 5px;\n"
                                "\n"
                                "}\n"
                                "\n"
                                "QPushButton{\n"
                                "font: 13pt \"Tahoma\";\n"
                                "border:1px solid black;\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "\n"
                                "#btnEntrada, #btnSalida{\n"
                                "font: 25pt \"Tahoma\";\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "background-color: #0c80c4;\n"
                                "}\n"
                                "\n"
                                "#layoutGeneral{\n"
                                "border:1px solid black;\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "\n"
                                "#layoutDescuento{\n"
                                "border:1px solid black;\n"
                                "border-radius: 5px\n"
                                "}\n"
                                "\n"
                                "#layoutUsuario{\n"
                                "border:1px solid black;\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "\n"
                                "#radioDescuento{\n"
                                "font: 18pt \"Tahoma\";\n"
                                "}\n"
                                "")
        Principal.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Principal.setDocumentMode(False)
        Principal.setTabShape(QtWidgets.QTabWidget.Rounded)
        Principal.setDockNestingEnabled(False)
        Principal.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPlaca = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelPlaca.setObjectName("labelPlaca")
        self.horizontalLayout.addWidget(self.labelPlaca)
        self.font = QFont()
        self.font.setCapitalization(QFont.AllUppercase)
        self.txtPlaca = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txtPlaca.setObjectName("txtPlaca")
        self.txtPlaca.setMaxLength(7)
        self.txtPlaca.setFont(self.font)
        self.horizontalLayout.addWidget(self.txtPlaca)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(510, 10, 821, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layoutTotalPagar = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layoutTotalPagar.setContentsMargins(0, 0, 0, 0)
        self.layoutTotalPagar.setObjectName("layoutTotalPagar")
        self.labelTotalPagar = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelTotalPagar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTotalPagar.setStyleSheet("border:1px solid black;\n"
                                           "border-radius: 5px;\n"
                                           "")
        self.labelTotalPagar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTotalPagar.setObjectName("labelTotalPagar")
        self.layoutTotalPagar.addWidget(self.labelTotalPagar, 0, 0, 1, 1)
        self.layoutGeneral = QtWidgets.QGroupBox(self.centralwidget)
        self.layoutGeneral.setGeometry(QtCore.QRect(10, 290, 461, 401))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.layoutGeneral.setFont(font)
        self.layoutGeneral.setStyleSheet("")
        self.layoutGeneral.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.layoutGeneral.setObjectName("layoutGeneral")
        self.formLayout = QtWidgets.QFormLayout(self.layoutGeneral)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(5, 20, 5, 20)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutGeneral)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtIdFactura = QtWidgets.QLineEdit(self.layoutGeneral)
        self.txtIdFactura.setEnabled(False)
        self.txtIdFactura.setObjectName("txtIdFactura")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtIdFactura)
        self.label_2 = QtWidgets.QLabel(self.layoutGeneral)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtHoraEntrada = QtWidgets.QLineEdit(self.layoutGeneral)
        self.txtHoraEntrada.setEnabled(False)
        self.txtHoraEntrada.setObjectName("txtHoraEntrada")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtHoraEntrada)
        self.label_3 = QtWidgets.QLabel(self.layoutGeneral)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtFechaEntrada = QtWidgets.QLineEdit(self.layoutGeneral)
        self.txtFechaEntrada.setEnabled(False)
        self.txtFechaEntrada.setObjectName("txtFechaEntrada")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtFechaEntrada)
        self.label_4 = QtWidgets.QLabel(self.layoutGeneral)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtHoraSalida = QtWidgets.QLineEdit(self.layoutGeneral)
        self.txtHoraSalida.setEnabled(False)
        self.txtHoraSalida.setObjectName("txtHoraSalida")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtHoraSalida)
        self.label_5 = QtWidgets.QLabel(self.layoutGeneral)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtFechaSalida = QtWidgets.QLineEdit(self.layoutGeneral)
        self.txtFechaSalida.setEnabled(False)
        self.txtFechaSalida.setObjectName("txtFechaSalida")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtFechaSalida)
        self.label_6 = QtWidgets.QLabel(self.layoutGeneral)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtTiempo = QtWidgets.QLineEdit(self.layoutGeneral)
        self.txtTiempo.setEnabled(False)
        self.txtTiempo.setObjectName("txtTiempo")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtTiempo)
        self.label_7 = QtWidgets.QLabel(self.layoutGeneral)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtValorCobro = QtWidgets.QLineEdit(self.layoutGeneral)
        self.txtValorCobro.setEnabled(False)
        self.txtValorCobro.setObjectName("txtValorCobro")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txtValorCobro)
        self.comboTipo = QtWidgets.QComboBox(self.layoutGeneral)
        self.comboTipo.setEditable(False)
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.setModelColumn(0)
        self.comboTipo.setObjectName("comboTipo")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboTipo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_8 = QtWidgets.QLabel(self.layoutGeneral)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(510, 510, 821, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.layoutBotones = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.layoutBotones.setContentsMargins(0, 0, 0, 0)
        self.layoutBotones.setObjectName("layoutBotones")
        self.btnMensualidad = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMensualidad.sizePolicy().hasHeightForWidth())
        self.btnMensualidad.setSizePolicy(sizePolicy)
        self.btnMensualidad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "..\icons\icon-mensaualidad.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMensualidad.setIcon(icon1)
        self.btnMensualidad.setIconSize(QtCore.QSize(50, 50))
        self.btnMensualidad.setObjectName("btnMensualidad")
        self.layoutBotones.addWidget(self.btnMensualidad, 0, 3, 1, 1)
        self.btnPagar = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPagar.sizePolicy().hasHeightForWidth())
        self.btnPagar.setSizePolicy(sizePolicy)
        self.btnPagar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPagar.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "..\icons\icon-pagar.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPagar.setIcon(icon2)
        self.btnPagar.setIconSize(QtCore.QSize(50, 50))
        self.btnPagar.setObjectName("btnPagar")
        self.layoutBotones.addWidget(self.btnPagar, 1, 0, 1, 1)
        self.btnListarVehiculos = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnListarVehiculos.sizePolicy().hasHeightForWidth())
        self.btnListarVehiculos.setSizePolicy(sizePolicy)
        self.btnListarVehiculos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("..\icons\icon-RA.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListarVehiculos.setIcon(icon3)
        self.btnListarVehiculos.setIconSize(QtCore.QSize(50, 50))
        self.btnListarVehiculos.setObjectName("btnListarVehiculos")
        self.layoutBotones.addWidget(self.btnListarVehiculos, 0, 1, 1, 1)
        self.btnInventario = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInventario.sizePolicy().hasHeightForWidth())
        self.btnInventario.setSizePolicy(sizePolicy)
        self.btnInventario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            "..\icons\icon-inventario.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInventario.setIcon(icon4)
        self.btnInventario.setIconSize(QtCore.QSize(50, 50))
        self.btnInventario.setObjectName("btnInventario")
        self.layoutBotones.addWidget(self.btnInventario, 0, 4, 1, 1)
        self.btnCuadre = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnCuadre.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCuadre.sizePolicy().hasHeightForWidth())
        self.btnCuadre.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnCuadre.setFont(font)
        self.btnCuadre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCuadre.setMouseTracking(False)
        self.btnCuadre.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCuadre.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.btnCuadre.setAcceptDrops(False)
        self.btnCuadre.setToolTip("")
        self.btnCuadre.setInputMethodHints(QtCore.Qt.ImhNone)
        self.btnCuadre.setText("Cuadre")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            "..\icons\icon-cuadre.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCuadre.setIcon(icon5)
        self.btnCuadre.setIconSize(QtCore.QSize(50, 50))
        self.btnCuadre.setShortcut("")
        self.btnCuadre.setCheckable(False)
        self.btnCuadre.setAutoDefault(False)
        self.btnCuadre.setDefault(False)
        self.btnCuadre.setFlat(False)
        self.btnCuadre.setObjectName("btnCuadre")
        self.layoutBotones.addWidget(self.btnCuadre, 1, 1, 1, 1)
        self.btnLimpiar = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiar.sizePolicy().hasHeightForWidth())
        self.btnLimpiar.setSizePolicy(sizePolicy)
        self.btnLimpiar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(
            "..\icons\icons-limpiar.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon6)
        self.btnLimpiar.setIconSize(QtCore.QSize(50, 50))
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.layoutBotones.addWidget(self.btnLimpiar, 0, 0, 1, 1)
        self.btnCambiarPrecio = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCambiarPrecio.sizePolicy().hasHeightForWidth())
        self.btnCambiarPrecio.setSizePolicy(sizePolicy)
        self.btnCambiarPrecio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            "..\icons\icon-editar.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCambiarPrecio.setIcon(icon7)
        self.btnCambiarPrecio.setIconSize(QtCore.QSize(50, 50))
        self.btnCambiarPrecio.setObjectName("btnCambiarPrecio")
        self.layoutBotones.addWidget(self.btnCambiarPrecio, 1, 3, 1, 1)
        self.btnConsultar = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConsultar.sizePolicy().hasHeightForWidth())
        self.btnConsultar.setSizePolicy(sizePolicy)
        self.btnConsultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(
            "..\icons\icon-buscar.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConsultar.setIcon(icon8)
        self.btnConsultar.setIconSize(QtCore.QSize(50, 50))
        self.btnConsultar.setObjectName("btnConsultar")
        self.layoutBotones.addWidget(self.btnConsultar, 1, 4, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap("..\icons\salida.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon9)
        self.btnSalir.setIconSize(QtCore.QSize(50, 50))
        self.btnSalir.setObjectName("btnSalir")
        self.layoutBotones.addWidget(self.btnSalir, 0, 5, 2, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(510, 120, 821, 151))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.layoutUsuario = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.layoutUsuario.setContentsMargins(0, 0, 0, 0)
        self.layoutUsuario.setObjectName("layoutUsuario")
        self.labelFecha = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.labelFecha.setObjectName("labelFecha")
        self.layoutUsuario.addWidget(self.labelFecha, 1, 1, 1, 1)
        self.labelHora = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.labelHora.setEnabled(True)
        self.labelHora.setObjectName("labelHora")
        self.layoutUsuario.addWidget(self.labelHora, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.layoutUsuario.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.layoutUsuario.addWidget(self.label_13, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.layoutUsuario.addWidget(self.label_9, 0, 0, 1, 1)
        self.labelCajero = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.labelCajero.setObjectName("labelCajero")
        self.layoutUsuario.addWidget(self.labelCajero, 0, 3, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 110, 461, 171))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnSalida = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalida.sizePolicy().hasHeightForWidth())
        self.btnSalida.setSizePolicy(sizePolicy)
        self.btnSalida.setIcon(icon9)
        self.btnSalida.setIconSize(QtCore.QSize(50, 50))
        self.btnSalida.setObjectName("btnSalida")
        self.gridLayout_3.addWidget(self.btnSalida, 0, 1, 1, 1)
        self.btnEntrada = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEntrada.sizePolicy().hasHeightForWidth())
        self.btnEntrada.setSizePolicy(sizePolicy)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(
            "..\icons\icon-entrada.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEntrada.setIcon(icon10)
        self.btnEntrada.setIconSize(QtCore.QSize(50, 50))
        self.btnEntrada.setObjectName("btnEntrada")
        self.gridLayout_3.addWidget(self.btnEntrada, 0, 0, 1, 1)
        self.layoutDescuento = QtWidgets.QGroupBox(self.centralwidget)
        self.layoutDescuento.setGeometry(QtCore.QRect(510, 340, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        self.layoutDescuento.setFont(font)
        self.layoutDescuento.setObjectName("layoutDescuento")
        self.radioDescuento = QtWidgets.QRadioButton(self.layoutDescuento)
        self.radioDescuento.setGeometry(QtCore.QRect(20, 40, 221, 31))
        self.radioDescuento.setObjectName("radioDescuento")
        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Prinicipal"))
        self.labelPlaca.setText(_translate("Principal", "Placa:"))
        self.labelTotalPagar.setText(_translate("Principal", "0"))
        self.layoutGeneral.setTitle(_translate("Principal", "General"))
        self.label.setText(_translate("Principal", "Numero de Factura:"))
        self.label_2.setText(_translate("Principal", "Hora de llegada:"))
        self.label_3.setText(_translate("Principal", "Fecha de llegada:"))
        self.label_4.setText(_translate("Principal", "Hora de salida:"))
        self.label_5.setText(_translate("Principal", "Fecha de salida:"))
        self.label_6.setText(_translate("Principal", "Tiempo transcurrido:"))
        self.label_7.setText(_translate("Principal", "Valor cobro:"))
        self.comboTipo.setItemText(0, _translate("Principal", "Seleccionar..."))
        self.comboTipo.setItemText(1, _translate("Principal", "CARRO"))
        self.comboTipo.setItemText(2, _translate("Principal", "MOTO"))
        self.label_8.setText(_translate("Principal", "Tipo de tarifa:"))
        self.btnMensualidad.setText(_translate("Principal", "Mensualidades"))
        self.btnPagar.setText(_translate("Principal", "Pagar"))
        self.btnListarVehiculos.setText(_translate("Principal", "Reporte V. A."))
        self.btnInventario.setText(_translate("Principal", "Inventario"))
        self.btnLimpiar.setText(_translate("Principal", "Limpiar"))
        self.btnCambiarPrecio.setText(_translate("Principal", "Cambiar Precio"))
        self.btnConsultar.setText(_translate("Principal", "Consultar"))
        self.btnSalir.setText(_translate("Principal", "Salir"))
        self.labelFecha.setText(_translate("Principal", "Aqui viene la fecha"))
        self.labelHora.setText(_translate("Principal", "Aqui viene la hora"))
        self.label_10.setText(_translate("Principal", "Fecha:"))
        self.label_13.setText(_translate("Principal", "Cajero:"))
        self.label_9.setText(_translate("Principal", "Hora:"))
        self.labelCajero.setText(_translate("Principal", "aqui viene el nombre del cajero"))
        self.btnSalida.setText(_translate("Principal", "SALIDA"))
        self.btnEntrada.setText(_translate("Principal", "ENTRADA"))
        self.layoutDescuento.setTitle(_translate("Principal", "Descuento"))
        self.radioDescuento.setText(_translate("Principal", "Aplicar descuento"))
