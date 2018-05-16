import sys
import time
from threading import Thread
from time import sleep

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from co.edu.uniquindio.parkingsoft.LogicaUI import PagarUI, MensualidadUI, raUI, CuadreUI, CambiarPrecioUI
from co.edu.uniquindio.parkingsoft.excepciones import VehiculoYaExiste
from co.edu.uniquindio.parkingsoft.logica import Usuario, Parqueadero, Vehiculo
from co.edu.uniquindio.parkingsoft.logica.FacturaDia import FacturaDia
from co.edu.uniquindio.parkingsoft.ui.VentanaPrincipal import Ui_Principal


# metodo que crea la conexion a la base de datos
def createConection():
    Principal.db = QSqlDatabase.addDatabase('QMYSQL')
    Principal.db.setHostName(Principal.host)
    Principal.db.setDatabaseName(Principal.nameDataBase)
    Principal.db.setUserName(Principal.nameUser)
    Principal.db.setPassword(Principal.password)
    Principal.db.open()
    print(Principal.db.lastError().text())
    return True


# logica de la UI de la ventana principal
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

    # constructor de la UI
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
        self.ui.btnCambiarPrecio.setEnabled(False)
        self.ui.labelFecha.setText(fecha)
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnEntrada.clicked.connect(self.ingresoVehiculo)
        self.ui.btnSalida.clicked.connect(self.salidaVehicular)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnMensualidad.clicked.connect(self.mensualidad)
        self.ui.btnPagar.clicked.connect(self.abrirPagar)
        self.ui.btnListarVehiculos.clicked.connect(self.reporteAvance)
        self.ui.btnCuadre.clicked.connect(self.abrirCuadre)
        self.ui.btnCambiarPrecio.clicked.connect(self.cambiarPrecio)
        self.ui.radioDescuento.clicked.connect(self.cambiarDescuento)

    # hilo que muestra la hora actual en la UI
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
                    QMessageBox.warning(self, "Error", "Error en la transaccion" + e.args,
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
                self.ui.btnCambiarPrecio.setEnabled(True)
                self.cambiarSalidaEnable(False)

            else:
                QMessageBox.information(self, "aviso", "ERROR VEHICULO", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Error", "Ingrese primero la placa", QMessageBox.Ok)

    # Metodo que genera un cierre de caja al final de la jornada
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

    # metodo que calcula la fecha del dia actual y la muestra en la UI
    def mostrarFechaActual(self):
        fecha = (time.strftime("%d /%m /%Y"))
        self.ui.labelFecha.setText(fecha)

    # metodo que inicializa los atributos del parqueadero
    def inicializarParqueadero(self):
        self.parqueadero.nombre = "parqueadero niño Jair"
        self.parqueadero.horario = "lunes a viernes de 7:00 am a 9:00 pm"
        self.parqueadero.telefono = "7653452"
        self.parqueadero.direccion = "Armenia centro"

    # metodo que devuelve al login
    def salir(self):
        opcion = QMessageBox.question(self, "Salir", "¿Seguro que quiere salir?", QMessageBox.Yes, QMessageBox.No)
        if opcion == QMessageBox.Yes:
            self.isRunning = False
            sys.exit(0)

    def mostrarTotalPagar(self):
        if self.tiquete is not None:
            self.ui.labelTotalPagar.setText("$ " + str(self.tiquete.cobro))
            self.ui.txtValorCobro.setText("$ " + str(self.tiquete.cobro))
        else:
            self.ui.labelTotalPagar.setText("$ 0")

    # metodo que limpia todos los campos de texto
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
        self.ui.btnCambiarPrecio.setEnabled(False)

    # metodo que permite la edicion y ejecucion de funcionalidades bloqueadas
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

    # metodo que abre la ventana de mensualidades
    def mensualidad(self):
        self.ventana = MensualidadUI.MensualidadUI(self.parqueadero)
        self.ventana.showFullScreen()

    # metodo que abre la ventana de cobro
    def abrirPagar(self):
        self.venPagar = PagarUI.PagarUI(self.parqueadero, self.tiquete, self.vehiculo, self)
        self.venPagar.show()

    # metodo que abre la ventana de reportes
    def reporteAvance(self):
        self.ra = raUI.raUI(self.parqueadero, self)
        self.ra.show()

    def cambiarDescuento(self):
        estado = self.ui.radioDescuento.isChecked()
        if estado:
            self.tiquete.descuento = True

        else:
            self.tiquete.descuento = False

    def cambiarPrecio(self):
        self.cambiar_precio = CambiarPrecioUI.CambiarPrecioUI(self.parqueadero, self.tiquete, self)
        self.cambiar_precio.show()

    def abrirCuadre(self):
        self.cuadre = CuadreUI.CuadreUI(self.parqueadero, self)
        self.cuadre.show()


# main de la aplicaacion
if __name__ == '__main__':
    pass
