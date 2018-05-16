from PyQt5 import QtGui
from PyQt5.QtWidgets import QFrame, QMessageBox

from co.edu.uniquindio.parkingsoft.LogicaUI import Principal
from co.edu.uniquindio.parkingsoft.excepciones.PlacaErrorException import PlacaErrorException
from co.edu.uniquindio.parkingsoft.excepciones.TiqueteException import TiqueteException
from co.edu.uniquindio.parkingsoft.logica import FacturaDia, Parqueadero
from co.edu.uniquindio.parkingsoft.ui.VentanaCambiarPrecio import Ui_VentanaCambiarPrecio


class CambiarPrecioUI(QFrame):
    parqueadero: Parqueadero
    tiquete: FacturaDia
    principal: Principal

    def __init__(self, parqueadero: Parqueadero, tiquete: FacturaDia, principal: Principal, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_VentanaCambiarPrecio()
        self.ui.setupUi(self)
        self.parqueadero = parqueadero
        self.principal = principal
        self.tiquete = tiquete
        self.ui.txtCambiarPrecio.setValidator(QtGui.QDoubleValidator())
        self.ui.btn0.clicked.connect(self.btn0)
        self.ui.btn1.clicked.connect(self.btn1)
        self.ui.btn2.clicked.connect(self.btn2)
        self.ui.btn3.clicked.connect(self.btn3)
        self.ui.btn4.clicked.connect(self.btn4)
        self.ui.btn5.clicked.connect(self.btn5)
        self.ui.btn6.clicked.connect(self.btn6)
        self.ui.btn7.clicked.connect(self.btn7)
        self.ui.btn8.clicked.connect(self.btn8)
        self.ui.btn9.clicked.connect(self.btn9)
        self.ui.txtCambiarPrecio.returnPressed.connect(self.cambiarPrecio)

    def cambiarPrecio(self):
        try:
            nuevo_valor = self.ui.txtCambiarPrecio.text()
            print(nuevo_valor)
            if nuevo_valor == "":
                QMessageBox.warning(self, "Alerta", "Debe de ingresar un valor", QMessageBox.Ok)
            else:
                nuevo_valor = int(nuevo_valor)
                self.parqueadero.cambiarPrecio(nuevo_valor)
                self.principal.mostrarTotalPagar()
                self.close()
        except TiqueteException as e:
            QMessageBox.critical(self, "Error", str(e), QMessageBox.Ok)
        except PlacaErrorException as e:
            QMessageBox.critical(self, "Error", str(e), QMessageBox.Ok)

    def btn0(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "0")

    def btn1(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "1")

    def btn2(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "2")

    def btn3(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "3")

    def btn4(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "4")

    def btn5(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "5")

    def btn6(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "6")

    def btn7(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "7")

    def btn8(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "8")

    def btn9(self):
        self.ui.txtCambiarPrecio.setText(self.ui.txtCambiarPrecio.text() + "9")
