from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from co.edu.uniquindio.parkingsoft.LogicaUI import Principal
from co.edu.uniquindio.parkingsoft.logica import Parqueadero, FacturaDia, Vehiculo
from co.edu.uniquindio.parkingsoft.ui.VentanaPagar import Ui_ventanaPagar


#  logica de la UI de cobro
class PagarUI(QMainWindow):
    parqueadero: Parqueadero  # parqueadero actual
    tiquete: FacturaDia  # factura del vehiculo a salir
    vehiculo: Vehiculo  # vehiculo a salir
    principal: Principal

    # constructor de la UI
    def __init__(self, parqueadero: Parqueadero, tiquete: FacturaDia, vehiculo: Vehiculo, principal: Principal,
                 parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_ventanaPagar()
        self.ui.setupUi(self)
        self.ui.txtDescuento.setText("$ 0")
        self.parqueadero = parqueadero
        self.tiquete = tiquete
        self.vehiculo = vehiculo
        self.principal = principal
        self.mostrarInformacion()
        self.ui.txtValor.setValidator(QDoubleValidator())
        self.ui.btnVolver.clicked.connect(self.volver)
        self.ui.btnImprimir.clicked.connect(self.imprimir)

    # metodo que devuelve a la UI anterior
    def volver(self):
        self.close()

    # metodo que imprime la informacion sobre el servicio prestado y da opciones de interaccion
    def imprimir(self):
        try:
            valorIngresado = self.ui.txtValor.text()
            valorIngresado = int(valorIngresado)
            (resultado, mensaje) = self.parqueadero.pagarSalida(valorIngresado)
            if resultado == 1:
                respuesta = QMessageBox.question(self, "Imprimir", "¿Imprimir el recibo de salida?", QMessageBox.Yes,
                                                 QMessageBox.No)

                if respuesta == QMessageBox.Yes:
                    QMessageBox.information(self, "Tiquete de Salida", mensaje,
                                            QMessageBox.Ok)
                self.principal.limpiar()
                self.close()
            elif resultado == 2:
                QMessageBox.warning(self, "Aviso", "El valor ingresado no es valido", QMessageBox.Ok)
            elif resultado == 3:
                QMessageBox.critical(self, "Error", "No se pudo completar la transacción, intentelo de nuevo",
                                     QMessageBox.Ok)
            elif resultado == -1:
                QMessageBox.critical(self, "Error", "No se pudo completar la transacción, intentelo de nuevo",
                                     QMessageBox.Ok)
        except:
            QMessageBox.critical(self, "Error", "Ocurrio un error en la transaccion, vuelva a intentarlo",
                                 QMessageBox.Ok)

    # metodo que imprime el total a cobrar
    def mostrarInformacion(self):
        cobro = self.tiquete.cobro
        descuento = self.tiquete.descuento
        tiempo = self.tiquete.tiempo

        self.ui.txtTiempo.setText(str(tiempo))
        if descuento == True:
            if self.vehiculo.tipo_vehiculo == "CARRO":
                self.ui.txtDescuento.setText("$ " + str(self.parqueadero.HORA_CARRO))
                cobro = cobro - self.parqueadero.HORA_CARRO
                if cobro < 0:
                    cobro = 0
                    self.tiquete.cobro = cobro

                    self.ui.txtValor.setText(str("0"))
                else:
                    self.tiquete.cobro = cobro

                    self.ui.txtValor.setText(str(cobro))
            else:
                self.ui.txtDescuento.setText("$ " + str(self.parqueadero.HORA_MOTO))
                cobro = cobro - self.parqueadero.HORA_CARRO
                if cobro < 0:
                    cobro = 0
                    self.tiquete.cobro = cobro
                    self.ui.txtValor.setText(str("0"))
                else:
                    self.tiquete.cobro = cobro
                    self.ui.txtValor.setText(str(cobro))
        else:
            self.ui.txtDescuento.setText("$ 0")
            self.ui.txtValor.setText(str(cobro))

        self.ui.labelTotalPagar.setText("$ " + str(cobro))
