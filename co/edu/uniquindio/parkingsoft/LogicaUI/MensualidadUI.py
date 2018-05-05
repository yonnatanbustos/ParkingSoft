from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore

from co.edu.uniquindio.parkingsoft.logica import Parqueadero
from co.edu.uniquindio.parkingsoft.ui.VentanaMensualida import Ui_MainWindow


class MensualidadUI(QMainWindow):
    parqueadero: Parqueadero

    def __init__(self, parqueadero: Parqueadero, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parqueadero = parqueadero
        self.cambiarEnable(False)
        self.ui.btnNuevo.clicked.connect(self.nuevo)
        self.ui.btnVolver.clicked.connect(self.volver)
        self.ui.btnGuardar.clicked.connect(self.ingresarMensualida)
        self.ui.tableMensualidades.itemClicked.connect(self.seleccionar)
        self.actualizarTabla()

    def ingresarMensualida(self):
        placa = self.ui.txtPlaca.text()
        tipoVehiculo = self.ui.comboTipo.currentText()
        propietario = self.ui.txtPropietario.text()
        telefono = self.ui.txtTelefono.text()
        fechaEntrada = self.ui.txtFechaEntrada.text()
        fechaSalida = self.ui.txtFechaSalida.text()

        estado = self.parqueadero.ingresarMensualida(placa, tipoVehiculo, propietario, telefono, fechaEntrada,
                                                     fechaSalida)
        if estado == 1:
            QMessageBox.information(self, "Notificación", "Registro Exitoso", QMessageBox.Yes)
        elif estado == 4:
            QMessageBox.warning(self, "Aviso", "La fecha de salida debe ser mayor a la fecha de entrada",
                                QMessageBox.Ok)
        elif estado == 3:
            QMessageBox.warning(self, "Aviso", "El tamaño de la placa no es el indicado", QMessageBox.Yes)
        elif estado == 2:
            QMessageBox.warning(self, "Aviso", "El vehiculo ya se encuentra registrado", QMessageBox.Yes)

    def seleccionar(self):
        row = self.ui.tableMensualidades.currentRow()
        placa = self.ui.tableMensualidades.item(row, 1).text()
        tipo = self.ui.tableMensualidades.item(row, 2).text()
        propietario = self.ui.tableMensualidades.item(row, 3).text()
        telefono = self.ui.tableMensualidades.item(row, 4).text()
        valor = self.ui.tableMensualidades.item(row, 5).text()
        fechaEntrada = self.ui.tableMensualidades.item(row, 6).text()
        fechaSalida = self.ui.tableMensualidades.item(row, 7).text()

        self.ui.txtPlaca.setText(placa)
        self.ui.comboTipo.setEditText(tipo)
        self.ui.txtPropietario.setText(propietario)
        self.ui.txtTelefono.setText(telefono)
        # self.ui.txtFechaSalida.setLineEdit(fechaSalida)
        self.cambiarEnable(True)
        self.ui.btnGuardar.setEnabled(False)

    def eliminarMensualidad(self):
        placa = self

        hola = 1

    def volver(self):
        self.close()

    def cambiarEnable(self, estado):
        self.ui.txtPlaca.setEnabled(estado)
        self.ui.txtPropietario.setEnabled(estado)
        self.ui.txtFechaEntrada.setEnabled(estado)
        self.ui.txtFechaSalida.setEnabled(estado)
        self.ui.txtTelefono.setEnabled(estado)
        self.ui.comboTipo.setEnabled(estado)
        self.ui.btnActualizar.setEnabled(estado)
        self.ui.btnEliminar.setEnabled(estado)
        self.ui.btnGuardar.setEnabled(estado)

    def nuevo(self):
        self.cambiarEnable(True)

    def eliminar(self):
        numero = 0
        # numero

    def actualizarTabla(self):
        tabla = self.ui.tableMensualidades
        self.parqueadero.actualizarTablaMensualida(tabla)
