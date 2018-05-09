from PyQt5.QtWidgets import QMainWindow

from co.edu.uniquindio.parkingsoft.LogicaUI import ModificarTarifaUI
from co.edu.uniquindio.parkingsoft.logica import Parqueadero, Usuario
from co.edu.uniquindio.parkingsoft.ui.VentanaAdministrador import Ui_PrincipalAdministrador

# UI de la interfaz de inicio del administrador
class AdministradorUI(QMainWindow):
    usuario: Usuario
    parqueadero: Parqueadero

    # contructor de la interfaz
    def __init__(self, parqueadero: Parqueadero, usuario: Usuario, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_PrincipalAdministrador()
        self.ui.setupUi(self)
        self.parqueadero = parqueadero
        self.usuario = usuario
        self.ui.btnModificarTarifa.triggered.connect(self.modificarTarifa)

    # UI para implementar la modificacion de las tarifas
    def modificarTarifa(self):
        self.ventana = ModificarTarifaUI.ModificarTarifaUI(self.parqueadero)
        self.ventana.show()
