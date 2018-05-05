import sys

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

from co.edu.uniquindio.parkingsoft.LogicaUI import Principal, AdministradorUI
from co.edu.uniquindio.parkingsoft.logica import Parqueadero
from co.edu.uniquindio.parkingsoft.ui.VentanaLogin import Ui_VentanaLogin


def createConection():
    Login.db = QSqlDatabase.addDatabase('QMYSQL')
    Login.db.setHostName(Login.host)
    Login.db.setDatabaseName(Login.nameDataBase)
    Login.db.setUserName(Login.nameUser)
    Login.db.setPassword(Login.password)
    Login.db.open()
    print(Login.db.lastError().text())
    return True


class Login(QMainWindow):
    db: QSqlDatabase
    host: str = 'localhost'
    nameDataBase: str = 'parqueadero'
    nameUser: str = 'root'
    password: str = '12345'
    parqueadero: Parqueadero

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_VentanaLogin()
        self.ui.setupUi(self)
        self.parqueadero = Parqueadero.Parqueadero(self.db)
        self.ui.btnIniciarSesion.clicked.connect(self.iniciarSesion)
        self.ui.btnCancelar.clicked.connect(self.salir)
        self.principal = None

    def iniciarSesion(self):
        nombreUsuario = self.ui.txtUsuario.text()
        nombreUsuario = nombreUsuario.upper()
        print(nombreUsuario)
        password = self.ui.txtContrasena.text()
        if len(nombreUsuario) == 0 | len(password) == 0:
            QMessageBox.warning(self, "Error", "Ingrese usuario y/o la contraseña", QMessageBox.Ok)
        else:
            usuario = self.parqueadero.iniciarSesion(nombreUsuario, password)
            if usuario is None:
                QMessageBox.warning(self, "Error", "El usuario o la contraseña no son correctos", QMessageBox.Ok)
            else:
                self.abrirPrincipal(usuario)

    def salir(self):
        opcion = QMessageBox.question(self, "Mensaje", "¿Desea salir de la aplicación?", QMessageBox.No,
                                      QMessageBox.Yes)
        if opcion == QMessageBox.Yes:
            sys.exit(0)

    def abrirPrincipal(self, usuario):
        if usuario.tipo == "EMPLEADO":
            self.principal = Principal.Principal(self.parqueadero, usuario)
            self.principal.showFullScreen()
            self.close()
        elif usuario.tipo == "ADMINISTRADOR":
            self.principal = AdministradorUI.AdministradorUI(self.parqueadero, usuario)
            self.principal.showFullScreen()
            self.close()

    def focusOutEvent(self, *args, **kwargs):
        texto = self.ui.txtUsuario.text()
        self.ui.txtUsuario.setText(texto.upper())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not createConection():
        sys.exit(1)
    myapp = Login()
    myapp.show()
    sys.exit(app.exec_())
