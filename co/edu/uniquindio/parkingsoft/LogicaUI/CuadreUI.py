import sys

from PyQt5.QtWidgets import QFrame, QMessageBox

from co.edu.uniquindio.parkingsoft.LogicaUI import Principal
from co.edu.uniquindio.parkingsoft.excepciones.CierreCajaException import CierreCajaException
from co.edu.uniquindio.parkingsoft.logica.Parqueadero import Parqueadero
from co.edu.uniquindio.parkingsoft.ui.VentanaCuadre import Ui_VentanaCuadre


class CuadreUI(QFrame):
    parqueadero: Parqueadero
    principal: Principal

    def __init__(self, parqueadero, principal: Principal, parent=None):
        QFrame.__init__(self, parent)
        self.ui = Ui_VentanaCuadre()
        self.ui.setupUi(self)

        self.parqueadero = parqueadero
        self.principal = principal
        self.mostrarInformacion()
        self.ui.btnImprimirCuadre.clicked.connect(self.imprimirCuadre)

    def mostrarInformacion(self):
        try:
            producido, estado = self.parqueadero.calcularCierreCaja()
            self.ui.txtTotalCuadre.setText("$ " + str(producido))
        except CierreCajaException as e:
            QMessageBox.critical(self, "Error", str(e), QMessageBox.Ok)

    def imprimirCuadre(self):
        mensaje = self.parqueadero.imprimirCuadre()
        QMessageBox.information(self, "Mensaje", mensaje, QMessageBox.Ok)
        self.principal.isRunning = False
        sys.exit(0)
