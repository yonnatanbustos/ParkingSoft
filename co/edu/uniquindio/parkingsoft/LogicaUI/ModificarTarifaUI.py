from PyQt5.QtWidgets import QMainWindow, QMessageBox

from co.edu.uniquindio.parkingsoft.logica import Parqueadero
from co.edu.uniquindio.parkingsoft.ui.VentanaModificarTarifa import Ui_VentanaModificarTarifa


class ModificarTarifaUI(QMainWindow):
    parqueadero: Parqueadero

    def __init__(self, parqueadero: Parqueadero, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_VentanaModificarTarifa()
        self.ui.setupUi(self)
        self.parqueadero = parqueadero
        self.mostrarInformacion()
        self.ui.btnGuardar.clicked.connect(self.cambiarTarifa)

    def mostrarInformacion(self):
        self.ui.txtActualMoto.setText(self.parqueadero.HORA_MOTO)
        self.ui.txtActualCarro.setText(self.parqueadero.HORA_CARRO)

    def cambiarTarifa(self):
        horaCarro = self.ui.txtNuevoCarro.text()
        horaMoto = self.ui.txtActualMoto.text()
        if len(horaCarro) == 0 | len(horaMoto) == 0:
            QMessageBox.warning(self, "Aviso", "Falta alguna tarifa, Moto o de Carro", QMessageBox.Ok)
        else:
            self.parqueadero.modificarTarifa(horaCarro, horaMoto)
            QMessageBox.information(self, "Exito", "Modificado satisfactoriamente", QMessageBox.Yes)
            self.mostrarInformacion()
