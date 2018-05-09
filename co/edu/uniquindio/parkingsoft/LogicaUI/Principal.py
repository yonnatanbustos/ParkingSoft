import sys
import time
from threading import Thread
from time import sleep

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from co.edu.uniquindio.parkingsoft.LogicaUI import PagarUI, MensualidadUI, raUI
from co.edu.uniquindio.parkingsoft.excepciones import VehiculoYaExiste
from co.edu.uniquindio.parkingsoft.logica import Usuario, Parqueadero, Vehiculo
from co.edu.uniquindio.parkingsoft.logica.FacturaDia import FacturaDia
from co.edu.uniquindio.parkingsoft.ui.VentanaPrincipal import Ui_Principal


def createConection():
    Principal.db = QSqlDatabase.addDatabase('QMYSQL')
    Principal.db.setHostName(Principal.host)
    Principal.db.setDatabaseName(Principal.nameDataBase)
    Principal.db.setUserName(Principal.nameUser)
    Principal.db.setPassword(Principal.password)
    Principal.db.open()
    print(Principal.db.lastError().text())
    return True


# clase principal de la aplicacion
class Principal(QMainWindow):
    db: QSqlDatabase
    host: str = 'localhost'
    nameDataBase: str = 'parqueadero'
    nameUser: str = 'root'
    password: str = '12345'
    parqueadero: Parqueadero
    tiquete: FacturaDia
    vehiculo: Vehiculo
    usuario: Usuario
    thread: Thread
    isRunning = True
    facturas = []  # lista de facturas del parqueadero
    usuarios = []  # lista de usuarios del parqueadero

    # constructor de la clase
    def __init__(self, parqueadero: Parqueadero, usuario: Usuario, parent=None, ):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.parqueadero = parqueadero
        self.usuario = usuario
        self.tiquete = None
        self.vehiculo = None
        fecha = time.strftime("%d/%m/%Y")
        self.thread = Thread(target=self.mostrarHoraActual)
        self.thread.start()
        self.ui.labelCajero.setText(usuario.nombres)
        self.ui.btnPagar.setEnabled(False)
        self.ui.labelFecha.setText(fecha)
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnEntrada.clicked.connect(self.ingresoVehiculo)
        self.ui.btnSalida.clicked.connect(self.salidaVehicular)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnMensualidad.clicked.connect(self.mensualidad)
        self.ui.btnPagar.clicked.connect(self.abrirPagar)
        self.ui.btnListarVehiculos.clicked.connect(self.reporteAvance)

    def mostrarHoraActual(self):
        hora = time.strftime(self.parqueadero.FORMATO_HORA)
        self.ui.labelHora.setText(hora)

        while self.isRunning:
            hora = time.strftime(self.parqueadero.FORMATO_HORA)
            self.ui.labelHora.setText(hora)
            sleep(1)

        # metodo que registra la entrada de un vehiculo

    def ingresoVehiculo(self):

        placa = self.ui.txtPlaca.text()
        tipovehiculo = self.ui.comboTipo.currentText()
        if len(placa) >= 5:
            if tipovehiculo.__eq__("CARRO") | tipovehiculo.__eq__("MOTO"):
                try:
                    (mensaje, estado) = self.parqueadero.ingresoVehicular(placa, tipovehiculo)
                    if estado:
                        QMessageBox.information(self, "Mensaje", mensaje, QMessageBox.Ok)
                    self.ui.txtPlaca.setText("")
                    self.ui.comboTipo.setEditText(self.ui.comboTipo.itemText(0))
                except VehiculoYaExiste:
                    QMessageBox.warning(self, "Error", "El vehicilo ya se encuentra registrado en el parqueadero",
                                        QMessageBox.Ok)
                except Exception as e:
                    QMessageBox.warning(self, "Error", "Error en la transaccion"+ e.args,
                                        QMessageBox.Ok)

            else:
                QMessageBox.warning(self, "Mensaje", "Seleccione tipo de vehiculo", QMessageBox.Ok)
        # metodo que registra la salida de un vehiculo

    def salidaVehicular(self):

        placa = self.ui.txtPlaca.text()
        if len(placa) != 0:
            vehiculo = self.parqueadero.buscarVehiculo(placa)
            descuento = self.ui.radioDescuento.isChecked()
            (ticket, estado) = self.parqueadero.salidaVehiculo(placa, descuento)

            if ticket is not None:
                QMessageBox.information(self, "aviso", "VEHICULO SALIDA", QMessageBox.Yes)
                self.ui.txtFechaEntrada.setText(ticket.fechaEntrada)
                idTiquete = ticket.idTiquete
                self.ui.txtIdFactura.setText(str(idTiquete))
                self.ui.txtHoraEntrada.setText(ticket.horaEntrada)
                self.ui.txtHoraSalida.setText(ticket.horaSalida)
                self.ui.txtFechaSalida.setText(ticket.fechaSalida)
                self.ui.txtTiempo.setText(str(ticket.tiempo))
                cobro = ticket.cobro
                self.ui.txtValorCobro.setText("$ " + str(cobro))
                self.ui.labelTotalPagar.setText("$ " + str(cobro))
                self.ui.comboTipo.setEditText(vehiculo.tipo_vehiculo)
                self.tiquete = ticket
                self.vehiculo = vehiculo
                self.ui.btnPagar.setEnabled(True)
                self.cambiarSalidaEnable(False)

            else:
                QMessageBox.information(self, "aviso", "ERROR VEHICULO", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Error", "Ingrese primero la placa", QMessageBox.Ok)

    # Metodo que genera un cierre de caja

    def cierreDeCaja(self):
        total = 0
        for fact in self.facturas:
            total += fact.totalPagar
        print("el total producido en el dia fue de ", total)

    # metodo que permite registrar un nuevo empleado a la plataforma
    def registarUsuario(self):
        nombre = ""
        apellido = ""
        cedula = ""
        usuario = ""
        contrasena = ""
        correo = ""
        tipo = 0
        u = Usuario.Usuario(nombre, apellido, cedula, usuario, contrasena, correo, tipo)
        self.usuarios.append(u)

    def mostrarFechaActual(self):
        fecha = (time.strftime("%d /%m /%Y"))
        self.ui.labelFecha.setText(fecha)

    def inicializarParqueadero(self):
        self.parqueadero.nombre = "parqueadero niño Jair"
        self.parqueadero.horario = "lunes a viernes de 7:00 am a 9:00 pm"
        self.parqueadero.telefono = "7653452"
        self.parqueadero.direccion = "Armenia centro"

    def salir(self):
        opcion = QMessageBox.question(self, "Salir", "¿Seguro que quiere salir?", QMessageBox.Yes, QMessageBox.No)
        if opcion == QMessageBox.Yes:
            self.isRunning = False
            sys.exit(0)

    def limpiar(self):
        self.ui.txtPlaca.setText("")
        self.ui.txtFechaEntrada.setText("")
        self.ui.txtHoraEntrada.setText("")
        self.ui.txtFechaSalida.setText("")
        self.ui.txtHoraSalida.setText("")
        self.ui.txtTiempo.setText("")
        self.ui.txtIdFactura.setText("")
        self.ui.txtValorCobro.setText("")
        self.ui.comboTipo.setEditText(self.ui.comboTipo.itemText(0))
        self.ui.labelTotalPagar.setText("$ 0")
        self.cambiarSalidaEnable(True)
        self.ui.btnPagar.setEnabled(False)

    def cambiarSalidaEnable(self, estado: bool):
        self.ui.txtPlaca.setEnabled(estado)
        self.ui.comboTipo.setEnabled(estado)
        self.ui.btnSalida.setEnabled(estado)
        self.ui.btnEntrada.setEnabled(estado)
        self.ui.btnConsultar.setEnabled(estado)
        self.ui.btnListarVehiculos.setEnabled(estado)
        self.ui.btnCuadre.setEnabled(estado)
        self.ui.btnMensualidad.setEnabled(estado)
        self.ui.btnInventario.setEnabled(estado)
        self.ui.btnSalir.setEnabled(estado)
        self.ui.comboTipo.setEnabled(estado)

    def mensualidad(self):
        self.ventana = MensualidadUI.MensualidadUI(self.parqueadero)
        self.ventana.showFullScreen()

    def abrirPagar(self):
        self.venPagar = PagarUI.PagarUI(self.parqueadero, self.tiquete, self.vehiculo)
        self.venPagar.show()

    # self.pagar =

    def reporteAvance(self):
        self.ra = raUI.raUI(self.parqueadero, self)
        self.ra.show()


if __name__ == '__main__':
    pass
