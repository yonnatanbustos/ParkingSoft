import pymysql.cursors


# Clase para crear la base de datos del parqueadero

class CrearDB():
    # variables para inicializar la base de datos.
    host: str = 'localhost'
    puerto: int = 3306
    nameUser: str = 'root'
    password: str = '12345'
    nameDataBase: str = 'parqueadero'

    # contructor de la clase
    def crearBaseDatos(self):
        estado = False
        sql = "CREATE DATABASE IF NOT EXISTS parqueadero"

        conetion = pymysql.connect(host=self.host,
                                   user=self.nameUser,
                                   password=self.password)

        try:
            with conetion.cursor() as cursor:
                cursor.execute(sql)
                estado = True


        except:
            conetion.close()
        return estado

    # creacion de las tablas de la base de datos
    def crearTablas(self):
        conection = pymysql.connect(host=self.host,
                                    user=self.nameUser,
                                    password=self.password,
                                    database=self.nameDataBase)
        cursor = conection.cursor()

        sql = "CREATE TABLE IF NOT EXISTS usuario (" \
              "idUsuario int NOT NULL UNIQUE AUTO_INCREMENT," \
              "cedula varchar(255) NOT NULL UNIQUE," \
              "nombres varchar(255) NOT NULL," \
              "apellidos varchar (255) NOT NULL," \
              "nombre_usuario varchar(255) NOT NULL UNIQUE," \
              "password varchar(255) NOT NULL," \
              "tipo varchar(255) NOT NULL," \
              "PRIMARY KEY (idUsuario)" \
              ")"
        cursor.execute(sql)
        sql = "SELECT * FROM usuario"
        estado = cursor.execute(sql)
        print(estado)

        if estado == 0:
            sql = "INSERT INTO usuario(idUsuario, cedula, nombres, apellidos, nombre_usuario, password, tipo)" \
                  "VALUES (1, '123', 'yonnatan', 'bustos', 'A', '123', 'ADMINISTRADOR')"
            cursor.execute(sql)

            sql = "INSERT INTO usuario(idUsuario, cedula, nombres, apellidos, nombre_usuario, password, tipo)" \
                  "VALUES (2, '456', 'sebastian', 'alzate', 'b', '123', 'EMPLEADO')"
            cursor.execute(sql)

        sql = "CREATE TABLE IF NOT EXISTS tiquete (" \
              "idTiquete int NOT NULL UNIQUE AUTO_INCREMENT," \
              "horaEntrada varchar(255) NOT NULL," \
              "fechaEntrada varchar(255) NOT NULL," \
              "horaSalida varchar(255)," \
              "fechaSalida varchar(255)," \
              "tiempo varchar(255)," \
              "cobro int," \
              "descuento int," \
              "cancelado int NOT NULL," \
              "PRIMARY KEY (idTiquete)" \
              ")"
        cursor.execute(sql)

        sql = "CREATE TABLE IF NOT EXISTS vehiculo (" \
              "idVehiculo int NOT NULL UNIQUE AUTO_INCREMENT," \
              "placa varchar(255) NOT NULL," \
              "tipoVehiculo varchar(255) NOT NULL," \
              "idTiquete int NOT NULL," \
              "cancelado int NOT NULL," \
              "PRIMARY KEY (idVehiculo)," \
              "FOREIGN KEY (idTiquete) REFERENCES tiquete(idTiquete)" \
              ")"
        cursor.execute(sql)

        sql = "CREATE TABLE IF NOT EXISTS mensualidad (" \
              "idTiquete int NOT NULL UNIQUE AUTO_INCREMENT," \
              "estado int(1) NOT NULL," \
              "placa varchar(255) NOT NULL UNIQUE," \
              "tipoVehiculo varchar(255) NOT NULL," \
              "propietario varchar(255) NOT NULL," \
              "telefono varchar(255)," \
              "valor int NOT NULL," \
              "fechaEntrada varchar(255) NOT NULL," \
              "fechaSalida varchar(255) NOT NULL," \
              "PRIMARY KEY (placa)" \
              ")"

        cursor.execute(sql)

        sql = "CREATE TABLE IF NOT EXISTS cierreCaja (" \
              "idCuadre int NOT NULL UNIQUE AUTO_INCREMENT," \
              "idUsuario int," \
              "fecha varchar(255) NOT NULL," \
              "valor int NOT NULL," \
              "PRIMARY KEY (idCuadre)," \
              "FOREIGN KEY (idUsuario) REFERENCES usuario (idUsuario)" \
              ")"
        cursor.execute(sql)
        cursor.close()
        conection.close()


# main de la clase.
if __name__ == '__main__':
    app = CrearDB()
    estado = app.crearBaseDatos()
    if estado == True:
        app.crearTablas()
