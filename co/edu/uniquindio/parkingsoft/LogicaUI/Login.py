import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from pymysql import connect
from pymysql.cursors import Cursor

from co.edu.uniquindio.parkingsoft.LogicaUI import Principal, AdministradorUI
from co.edu.uniquindio.parkingsoft.logica import Parqueadero
from co.edu.uniquindio.parkingsoft.logica.CrearDB import CrearDB
from co.edu.uniquindio.parkingsoft.ui.VentanaLogin import Ui_VentanaLogin


# metodo que genera la conexion con la base de datos.
def crearConection():
    try:
        Login.conect = connect(host=Login.host,
                               user=Login.nameUser,
                               password=Login.password,
                               database=Login.nameDataBase)

        print(Login.conect.open)

        Login.cursor = Login.conect.cursor()
        estado = Login.conect.cursor().connection
        print(estado)
        return estado
    except:
        return False


#  logica de la UI del login
class Login(QMainWindow):
    conect: connect
    cursor: Cursor
    host: str = 'localhost'
    nameDataBase: str = 'parqueadero'
    nameUser: str = 'root'
    password: str = '12345'
    parqueadero: Parqueadero

    # constructor de la clase
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_VentanaLogin()
        self.ui.setupUi(self)
        self.parqueadero = Parqueadero.Parqueadero(self.conect)
        self.ui.btnIniciarSesion.clicked.connect(self.iniciarSesion)
        self.ui.btnCancelar.clicked.connect(self.salir)
        self.principal = None

    # metodo que captura los datos de los campos y llama el metodo logico de iniciar sesion
    def iniciarSesion(self):
        nombreUsuario = self.ui.txtUsuario.text()
        password = self.ui.txtContrasena.text()
        if len(nombreUsuario) == 0 | len(password) == 0:
            QMessageBox.warning(self, "Error", "Ingrese usuario y/o la contraseña", QMessageBox.Ok)
        else:
            usuario = self.parqueadero.iniciarSesion(nombreUsuario, password)
            if usuario is None:
                QMessageBox.warning(self, "Error", "El usuario o la contraseña no son correctos", QMessageBox.Ok)
            else:
                self.abrirPrincipal(usuario)

    # metodo que le permite dar la accion de salir al boton salir
    def salir(self):
        opcion = QMessageBox.question(self, "Mensaje", "¿Desea salir de la aplicación?", QMessageBox.No,
                                      QMessageBox.Yes)
        if opcion == QMessageBox.Yes:
            sys.exit(0)

    # metodo que dependiendo del tipo de usuario abre la respectiva ventana principal
    def abrirPrincipal(self, usuario):
        if usuario.tipo == "EMPLEADO":
            self.principal = Principal.Principal(self.parqueadero, usuario)
            self.principal.showFullScreen()
            self.close()
        elif usuario.tipo == "ADMINISTRADOR":
            self.principal = AdministradorUI.AdministradorUI(self.parqueadero, usuario)
            self.principal.showFullScreen()
            self.close()


# main de la UI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # crearDB = CrearDB.CrearDB()
    try:
        if crearConection():
            myapp = Login()

            myapp.show()
            sys.exit(app.exec_())

        else:
            CrearDB.crearBaseDatos(CrearDB)
            CrearDB.crearTablas(CrearDB)
            crearConection()
            myapp = Login()

            myapp.show()
            sys.exit(app.exec_())

    except Exception as e:
        print("No se pudo establecer una conexion")
        print(e.args)
        sys.exit(1)
