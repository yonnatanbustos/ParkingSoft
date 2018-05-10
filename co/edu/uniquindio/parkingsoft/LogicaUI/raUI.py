from PyQt5.QtWidgets import QMainWindow

from co.edu.uniquindio.parkingsoft.LogicaUI import Principal
from co.edu.uniquindio.parkingsoft.logica import Parqueadero
from co.edu.uniquindio.parkingsoft.ui.VentanaRA import Ui_VentanaRA

#  logica de la UI de los reportes avanzados
class raUI(QMainWindow):
    parqueadero: Parqueadero  # parqueadero actual
    principal: Principal  # UI principal de referencia

    # constructor de la UI
    def __init__(self, parqueadero: Parqueadero, principal: Principal, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_VentanaRA()
        self.ui.setupUi(self)
        self.parqueadero = parqueadero
        self.principal = principal
        self.parqueadero.listarVehiculos(self.ui.tableVehiculos)
        self.ui.tableVehiculos.itemClicked.connect(self.seleccionar)

    # metodo que permite la seleccion de un vehiculo de la lista
    def seleccionar(self):
        row = self.ui.tableVehiculos.currentRow()
        placa = self.ui.tableVehiculos.item(row, 0).text()
        self.principal.ui.txtPlaca.setText(placa)
        self.close()
        print(placa)
