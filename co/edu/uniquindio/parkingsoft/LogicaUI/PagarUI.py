from PyQt5.QtWidgets import QMainWindow, QMessageBox

from co.edu.uniquindio.parkingsoft.logica import Parqueadero, FacturaDia, Vehiculo
from co.edu.uniquindio.parkingsoft.ui.VentanaPagar import Ui_ventanaPagar


class PagarUI(QMainWindow):
    parqueadero: Parqueadero
    tiquete: FacturaDia
    vehiculo: Vehiculo

    def __init__(self, parqueadero: Parqueadero, tiquete: FacturaDia, vehiculo: Vehiculo, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_ventanaPagar()
        self.ui.setupUi(self)
        self.ui.txtDescuento.setText("$ 0")
        self.parqueadero = parqueadero
        self.tiquete = tiquete
        self.vehiculo = vehiculo
        self.mostrarInformacion()

        self.ui.btnVolver.clicked.connect(self.volver)
        self.ui.btnImprimir.clicked.connect(self.imprimir)

    def volver(self):
        self.close()

    def imprimir(self):
        valorIngresado = int(float(self.ui.txtValor.text()))
        (resultado, mensaje) = self.parqueadero.pagarSalida(valorIngresado)
        if resultado == 1:
            respuesta = QMessageBox.question(self, "Imprimir", "¿Imprimir el recibo de salida?", QMessageBox.Yes,
                                             QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                QMessageBox.information(self, "Error", mensaje,
                                        "Aceptar")

        elif resultado == 2:
            QMessageBox.warning(self, "Aviso", "El valor ingresado no es valido", QMessageBox.Ok)
        elif resultado == 3:
            QMessageBox.information(self, "Error", "No se pudo completar la transacción, intentelo de nuevo",
                                    QMessageBox.Ok)

    def mostrarInformacion(self):
        cobro = self.tiquete.cobro
        descuento = self.tiquete.descuento
        tiempo = self.tiquete.tiempo

        self.ui.txtTiempo.setText(str(tiempo))
        if descuento:
            if self.vehiculo.tipo_vehiculo == "CARRO":
                self.ui.txtDescuento.setText("$ " + self.parqueadero.HORA_CARRO)
            else:
                self.ui.txtDescuento.setText("$ " + self.parqueadero.HORA_MOTO)
        self.ui.txtValor.setText(str(cobro))
        self.ui.labelTotalPagar.setText("$ " + str(cobro))
