import time
from datetime import datetime, timedelta

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from pymysql import connect

from co.edu.uniquindio.parkingsoft.excepciones.CierreCajaException import CierreCajaException
from co.edu.uniquindio.parkingsoft.excepciones.MensualidadException import MensualidadException
from co.edu.uniquindio.parkingsoft.excepciones.PlacaErrorException import PlacaErrorException
from co.edu.uniquindio.parkingsoft.excepciones.TiqueteException import TiqueteException
from co.edu.uniquindio.parkingsoft.excepciones.VehiculoYaExiste import VehiculoYaExiste
from co.edu.uniquindio.parkingsoft.logica import Usuario, FacturaDia, Vehiculo, Mensualidad, Cuadre


# clase que modela un objeto tipo parqueadero.


class Parqueadero():
    # Declaracion de los atributos del parqueadero
    HORA_MOTO = 600
    HORA_CARRO: int = 1700
    CARRO_MENS: int = 85000
    MOTO_MENS: int = 20000
    FORMATO_HORA = "%H:%M:%S"
    FORMATO_FECHA = "%d/%m/%Y"
    lista_vehiculos: ()  # lista de vehiculos en el parqueadero
    listaUsuarios: ()
    listaFacturas: ()
    listaMensualidades: ()
    listaCuadres: ()
    NOMBRE: str = "EL PARQUEADERO EL ÑINO JAIR"
    direccion: str = "Calle 18 #17-47"
    telefono: str = "Armenia"
    horario: str = "Lunes a Sabado 7:30am-7:30pm\n" \
                   "Domingos y Festivos 8am-2:30pm"
    NIT: str = "1038405474-5"
    REGIMEN: str = "SIMPLIFICADO"
    conect: connect

    db: QSqlDatabase
    tiquete: FacturaDia
    vehiculo: Vehiculo
    usuario: Usuario

    # constructor de la clase
    def __init__(self, conect: connect):
        self.lista_vehiculos = []
        self.listaUsuarios = []
        self.listaFacturas = []
        self.listaMensualidades = []
        self.listaCuadres = []
        print(conect.open)
        self.conect = conect
        print(self.conect.open)
        self.tiquete = None
        self.vehiculo = None
        self.usuario = None
        self.consultas()

    # consultas para llenar las listas de los vehiculos y usuarios
    def consultas(self):
        try:
            # llenando la lista de usuarios
            with self.conect.cursor() as cursor:
                sql = "SELECT * FROM usuario"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                for u in resultados:
                    cedula = u[1]
                    print("cedula ", cedula)
                    nombres = u[2]
                    apellidos = u[3]
                    nombre_usuario = u[4]
                    password = u[5]
                    tipo = u[6]
                    usuario = Usuario.Usuario(cedula, nombres, apellidos, nombre_usuario, password, tipo)
                    self.listaUsuarios.append(usuario)

            # llenando la lista de los vehiculos
            with self.conect.cursor() as cursor:
                sql = "SELECT * FROM vehiculo"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                for v in resultados:
                    placa = v[1]
                    tipoVehiculo = v[2]
                    idTiquete = v[3]
                    cancelado = v[4]
                    if cancelado == 0:
                        vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                        vehiculo.idTiquete = idTiquete
                        self.lista_vehiculos.append(vehiculo)

            # llenando la lista de los tiquetes
            with self.conect.cursor() as  cursor:
                sql = "SELECT * FROM tiquete"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                for t in resultados:
                    idTiquete = t[0]
                    horaEntrada = t[1]
                    fechaEntrada = t[2]
                    horaSalida = t[3]
                    fechaSalida = t[4]
                    tiempo = t[5]
                    cobro = t[6]
                    descuento = t[7]
                    cancelado = t[8]
                    if cancelado == 0:
                        tiquete = FacturaDia.FacturaDia(self, idTiquete, horaEntrada, fechaEntrada)
                        tiquete.horaSalida = horaSalida
                        tiquete.fechaSalida = fechaSalida
                        tiquete.tiempo = tiempo
                        tiquete.cobro = cobro
                        tiquete.descuento = descuento
                        self.listaFacturas.append(tiquete)

            # llenando la lista de las mensualidades
            with self.conect.cursor() as cursor:
                sql = "SELECT * FROM mensualidad"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                for m in resultados:
                    estado = int(m[1])
                    placa = m[2]
                    tipoVehiculo = m[3]
                    vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                    propietario = m[4]
                    telefono = m[5]
                    fechaEntrada = m[7]
                    fechaSalida = m[8]
                    mensualidad = Mensualidad.Mensualidad(self, vehiculo, propietario, telefono, fechaEntrada,
                                                          fechaSalida, estado)

                    self.listaMensualidades.append(mensualidad)
        except:
            print()

    # metodo que permite el registro de un usuario
    # cedula: cedula del usuario a registrar
    # nombres: nombres del usuario a registrar
    # apellidos: apellidos  del usuario a registrar
    # nombre_usuario: nombre de usuario  del usuario a registrar
    # password: contraseña  del usuario a registrar
    # tipo: tipo del usuario a registrar (administrador o empleado)
    def registrarUsuario(self, cedula: str, nombres: str, apellidos: str, nombre_usuario: str, password, tipo: str):
        nombres = nombres.upper()
        apellidos = apellidos.upper()
        nombre_usuario = nombre_usuario.upper()
        tipo = tipo.upper()

        if self.buscarUsuario(nombre_usuario) == None:
            if self.buscarUsuarioCedula(cedula) == None:
                nuevoUsuario = Usuario.Usuario(cedula, nombres, apellidos, nombre_usuario, password, tipo)
                self.listaUsuarios.append(nuevoUsuario)
                return True
            else:
                return False
        else:
            return False

    # metodo que permite veriricar si un usuario existe en la base de datos por su cedula
    # cedula: cedula de la persona a buscar
    def buscarUsuarioCedula(self, cedula):

        for u in self.listaUsuarios:
            if u.cedula == cedula:
                return u
        return None

    # metodo que permite el inicio de sesion
    # nombre usuario: nombre de usuario de la persona a ingresar
    # password: contraseña de la persona a ingresar.
    def iniciarSesion(self, nombreUsuario, password):
        nombreUsuario = nombreUsuario.upper()
        self.usuario = self.buscarUsuario(nombreUsuario)
        if self.usuario is not None:
            if self.usuario.password == password:
                return self.usuario
            else:
                return self.usuario
        else:
            return self.usuario

    def buscarUsuario(self, nombre_usuario):
        for i in self.listaUsuarios:
            if i.nombre_usuario == nombre_usuario:
                return i
        return None

    # metodo que registra la entrada de un vehiculo
    # placa: placa del vehiculo que ingreso al parqueadero.
    # tipoVehiculo: tipo del vehiculo que ingreso (carro o moto)
    def ingresoVehicular(self, placa: str, tipoVehiculo: str):
        placa = placa.upper()
        estado = False
        mensaje = "None"
        if len(placa) >= 5:
            vehiculo = self.buscarVehiculo(placa)

            if vehiculo is None:
                try:
                    vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                    factura = self.registrarFactura()
                    print(factura)
                    vehiculo.setIdTiquete(factura.idTiquete)
                    self.lista_vehiculos.append(vehiculo)
                    print(vehiculo.idTiquete)
                    sql = "INSERT INTO vehiculo (placa, tipoVehiculo, idTiquete, cancelado) " \
                          "VALUES ('%s', '%s', %d, %d)" % (
                              vehiculo.placa, vehiculo.tipo_vehiculo, vehiculo.idTiquete, 0)
                    with self.conect.cursor() as cursor:
                        cursor.execute(sql)
                        self.conect.commit()
                        mensaje = self.mostrarTiqueteEntrada(vehiculo, factura)
                        sql = "INSERT INTO prediccion (fechaEntrada, horaEntrada, tipoVehiculo) VALUES ('%s', '%s', '%s')" % (
                            factura.fechaEntrada,
                            factura.horaEntrada,
                            tipoVehiculo)
                        cursor.execute(sql)
                        self.conect.commit()
                        estado = True
                except Exception as e:
                    self.lista_vehiculos.remove(vehiculo)
                    self.conect.rollback()
                    print(e)
                    estado = False
            else:
                raise VehiculoYaExiste()
        else:
            print("Placa < 5")
        return mensaje, estado

    # metodo que ayuda a generar los id de los tiquetes automaticamente dependiendo del ultimo tiquete generado
    def obtenerIdTiquete(self):
        idTiquete = -1
        try:
            with self.conect.cursor() as cursor:
                sql = "SELECT idTiquete FROM tiquete ORDER BY idTiquete DESC LIMIT 1"
                cursor.execute(sql)
                resultado = cursor.fetchone()
                idTiquete = int(resultado[0])
        except:
            self.conect.rollback()
        return idTiquete

    # metodo que permite generar un factura de ingreso
    def registrarFactura(self):
        factura = None
        try:
            with self.conect.cursor() as cursor:
                print(cursor.connection)

                horaEntrada = time.strftime(self.FORMATO_HORA)
                fechaEntrada = time.strftime(self.FORMATO_FECHA)
                sql = "INSERT INTO tiquete (horaEntrada, fechaEntrada, cancelado) VALUES ('%s', '%s', %d)" % (
                    horaEntrada, fechaEntrada, 0)
                cursor.execute(sql)
                self.conect.commit()
                idTiquete = self.obtenerIdTiquete()

                factura = FacturaDia.FacturaDia(self, idTiquete, horaEntrada, fechaEntrada)
                self.listaFacturas.append(factura)
        except Exception as e:
            self.conect.rollback()
            print(e)
        return factura

    # metodo que busca un vehiculo dentro del parqueadero
    # placa: placa del vehiculo a buscar
    def buscarVehiculo(self, placa):
        for p in self.lista_vehiculos:
            if p.placa == placa:
                return p
        return None

    # metodo que permite la salida de un vehiculo
    # placa: placa del vehiculo que sale del parqueadero
    # descuento: booleano que permite saber si el cobro a realizar tiene descuento o no
    def salidaVehiculo(self, placa, descuento):
        placa = placa.upper()
        self.vehiculo = self.buscarVehiculo(placa)
        estado = False

        if self.vehiculo is not None:
            self.tiquete = self.buscarTiquete(self.vehiculo.idTiquete)
            if self.tiquete is not None:
                try:
                    fechaSalida = time.strftime(self.FORMATO_FECHA)
                    horaSalida = time.strftime(self.FORMATO_HORA)
                    self.tiquete.horaSalida = horaSalida
                    self.tiquete.fechaSalida = fechaSalida
                    if descuento == True:
                        self.tiquete.descuento = True
                    else:
                        self.tiquete.descuento = False

                    tiempo = self.calcularTiempo(self.tiquete)
                    self.tiquete.tiempo = tiempo
                    cobro = self.calcularCobro(tiempo, self.vehiculo.tipo_vehiculo)
                    self.tiquete.cobro = cobro
                    self.listaFacturas.remove(self.tiquete)
                    self.listaFacturas.append(self.tiquete)

                    estado = True
                except:
                    print("error de tiempo o cobro")
            else:
                print("el vehiculo no esta en el parqueadero")
                estado = False
        else:
            print("error salida")
            estado = False
        return self.tiquete, estado

    # Metodo para calcular el total a pagar de un vehiculo
    # tiempo: total de tiempo que estuvo ell vehiculo en el parqueadero
    # tipoVehiculo: tipo del vehiculo al que se le va a cobrar(carro o moto)
    def calcularCobro(self, tiempo, tipoVehiculo):
        tiempo = str(tiempo)
        totalCobro = 0
        dias = 0
        if tiempo.__contains__(","):
            dias = str(tiempo).split(",")
            tiempo = dias[1]
            print("tiempo es", tiempo)
            dias = str(dias[0]).split(" ")
            print(dias)
            dias = int(dias[0])
            print(dias)

        aux = str(tiempo).split(":")
        horas = int(aux[0])
        minutos = int(aux[1])
        if dias != 0:
            totalCobro = dias * 24

        if tipoVehiculo == "CARRO":
            totalCobro = totalCobro * self.HORA_CARRO + (horas * self.HORA_CARRO)
            if minutos > 30:
                totalCobro = totalCobro + self.HORA_CARRO
            else:
                totalCobro = totalCobro + int(self.HORA_CARRO / 2)

            return totalCobro
        else:
            totalCobro = totalCobro * self.HORA_MOTO + (horas * self.HORA_MOTO)
            if minutos > 30:
                totalCobro = totalCobro + self.HORA_MOTO
            else:
                totalCobro = totalCobro + int(self.HORA_MOTO / 2)

        return totalCobro

    # Metodo para buscar un tiquete registrado en el parqueadero
    # idTiquete: id del tiquete a buscar
    def buscarTiquete(self, idTiquete):
        for t in self.listaFacturas:
            if t.idTiquete == idTiquete:
                return t
        return None

    # Metodo para calcular el total de tiempo transcurrido de un vehiculo
    # tiquete: tiquete de ingreso para saber la hora de ingreso del vehiculo
    def calcularTiempo(self, tiquete: FacturaDia):
        retorno: str
        diferenciaHora = 0
        if tiquete is not None:
            try:
                fechaEntrada = datetime.strptime(tiquete.fechaEntrada, self.FORMATO_FECHA)
                fechaSalida = datetime.strptime(tiquete.fechaSalida, self.FORMATO_FECHA)
                horaEntrada = datetime.strptime(tiquete.horaEntrada, self.FORMATO_HORA)
                horaSalida = datetime.strptime(tiquete.horaSalida, self.FORMATO_HORA)

                diferenciaHora = horaSalida - horaEntrada
                diferenciaFecha = fechaSalida - fechaEntrada

                if diferenciaFecha.days > 0:
                    dias = diferenciaFecha.days * 24
                    retorno = diferenciaHora + timedelta(hours=dias)
                    print(retorno, " total tiempo")
                    return retorno
                return diferenciaHora
            except:
                print("hubo error al calcular el tiempo")

        return diferenciaHora

    # Metodo para registrar una mensualida al parqueadero
    # return -1 - las fechas de entrada y salida, estan por fuera de la fecha actual
    # return 1 - se registro la mensualidad satisfactoriamente
    # retrun 2 - el vehiculo ya esta registrado en la mensualidad
    # return 3 - la placa del vehciulo es menor a 5
    # return 4 - la dias de la mensualidad no se encuentra en el rago de pago (rango de dias: 15-31 dias)
    # return 5 - la fecha de entrada es mayor a la fecha de salida
    # placa: placa del vehiculo a registrar la mensualidad
    # tipoVehiculo: tipo del vehiculo a registrar
    # propietario: nombre del proopietario del vehiculo
    # telefono: telefono del propietario del vehiculo
    # fechaEntrada: fecha de la iniciacion de la mensualidad
    # fechaSalida: fecha de finaliacion de mensualidad
    def ingresarMensualida(self, placa, tipoVehiculo, propietario, telefono, fechaEntrada, fechaSalida):
        # definir la condicion de que la fechaEntrada sea menor a la fechaSalida
        try:
            fechaEntradaAux = datetime.strptime(fechaEntrada, self.FORMATO_FECHA)
            fechaSalidaAux = datetime.strptime(fechaSalida, self.FORMATO_FECHA)
        except:
            raise MensualidadException(
                "El formato de la fecha de entrada o la fecha de salida no son los adecuados")

        fechaActual = datetime.today()
        if fechaActual > fechaSalidaAux and fechaActual > fechaEntradaAux:
            return -1

        resultado = fechaSalidaAux - fechaEntradaAux
        resultado = resultado.days

        if fechaSalidaAux > fechaEntradaAux:
            if resultado >= 15 & resultado <= 31:
                if len(placa) >= 5:
                    vehiculo = self.buscarVehiculoMensualida(placa)
                    if vehiculo is None:
                        try:
                            with self.conect.cursor() as cursor:
                                vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                                mensualida = Mensualidad.Mensualidad(self, vehiculo, propietario, telefono,
                                                                     fechaEntrada,
                                                                     fechaSalida, 1)
                                self.listaMensualidades.append(mensualida)
                                valor = 0
                                if vehiculo.tipo_vehiculo == "CARRO_MENS":
                                    valor = self.CARRO_MENS
                                else:
                                    valor = self.MOTO_MENS

                                sql = "INSERT INTO mensualidad (estado, placa, tipoVehiculo, propietario, telefono, valor, fechaEntrada, fechaSalida)" \
                                      "VALUES (%d, '%s', '%s', '%s', '%s', %d, '%s', '%s')" % (
                                          1, placa, tipoVehiculo, propietario, telefono, valor,
                                          fechaEntrada,
                                          fechaSalida)

                                cursor.execute(sql)
                                self.conect.commit()
                                return 1
                        except:
                            self.conect.rollback()
                            self.listaMensualidades.remove(mensualida)
                            return 0
                    else:
                        return 2
                else:
                    return 3
            else:
                return 4

        else:
            return 5

    # Metodo para buscar vehiculos de mensualida en el parqueadero
    # placa: placa del vehiculo a buscar
    def buscarVehiculoMensualida(self, placa):
        for m in self.listaMensualidades:
            if m.vehiculo.placa == placa:
                return m
        return None

    # metodo que permite la modificacion de una mensualidad
    # placaAnterior: placa a reemplazar
    # placaNueva: placa nueva
    # tipoVehiculo: tipo del vehiculo registrado
    # propietario: nombre del propietario dle vehiculo
    # telefono: telefono del propietario del vehiculo
    # fechaEntrada: fecha del ingreso de mensualidad
    # fechaSalida: fecha de finalizacion de la mensualidad
    def modificarMensualidad(self, placaAnterior: str, placaNueva, tipoVehiculo, propietario, telefono, fechaEntrada,
                             fechaSalida):
        mensualidad: Mensualidad = self.buscarVehiculoMensualida(placaAnterior)
        if mensualidad is not None:
            estado = self.ingresarMensualida(placaNueva, tipoVehiculo, propietario, telefono, fechaEntrada, fechaSalida)
            if estado == 1:
                self.listaMensualidades.remove(mensualidad)
            else:
                raise MensualidadException.MensualidadException("Error en la modificacion de la mensualidad")

    # Metodo para listar todas las mensualidades del parqueadero
    # tabla: tabla actal de las mensualidades
    def actualizarTablaMensualida(self, tabla: QTableWidget):
        row = 0
        cantidad = tabla.rowCount()
        print(cantidad)
        for i in range(cantidad + 1):
            print(i)
            tabla.removeRow(i)
        header = tabla.horizontalHeader()
        for m in self.listaMensualidades:
            tabla.insertRow(row)
            if m.estado == 0:
                estado = QTableWidgetItem("Vencido")
                estado.setBackground(QtGui.QColor(255, 0, 0))
            else:
                estado = QTableWidgetItem("Al Dia")
                estado.setBackground(QtGui.QColor(42, 255, 39))
            placa = QTableWidgetItem(str(m.vehiculo.placa))
            tipo = QTableWidgetItem(str(m.vehiculo.tipo_vehiculo))
            propietario = QTableWidgetItem(str(m.propietario))
            telefono = QTableWidgetItem(str(m.telefono))
            valor = QTableWidgetItem(str(m.valor))
            fechaEntrada = QTableWidgetItem(str(m.fechaEntrada))
            fechaSalida = QTableWidgetItem(str(m.fechaSalida))
            tabla.setItem(row, 0, estado)
            tabla.setItem(row, 1, placa)
            tabla.setItem(row, 2, tipo)
            tabla.setItem(row, 3, propietario)
            tabla.setItem(row, 4, telefono)
            tabla.setItem(row, 5, valor)
            tabla.setItem(row, 6, fechaEntrada)
            tabla.setItem(row, 7, fechaSalida)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

            row += 1

    def eliminarMensualidad(self, placa: str):
        mensualidad = self.buscarVehiculoMensualida(placa)
        if mensualidad is not None:
            self.listaMensualidades.remove(mensualidad)

    # metodo que lista los vehiculos que estan en el parqueadero actualmente
    # tabla: tabla de los vehiculos que estan dentro del parqueadero actualmente
    def listarVehiculos(self, tabla):
        row = 0
        for v in self.lista_vehiculos:
            tabla.insertRow(row)
            placa = QTableWidgetItem(str(v.placa))
            tipoVehiculo = QTableWidgetItem(str(v.tipo_vehiculo))
            tiquete = self.buscarTiquete(v.idTiquete)
            horaEntrada = QTableWidgetItem(str(tiquete.horaEntrada))
            fechaEntrada = QTableWidgetItem(str(tiquete.fechaEntrada))
            tabla.setItem(row, 0, placa)
            tabla.setItem(row, 1, horaEntrada)
            tabla.setItem(row, 2, fechaEntrada)
            tabla.setItem(row, 3, tipoVehiculo)
            row = row + 1

    # Metodo para pagar de un vehiculo, le da una salida definitiva del sistema
    # return 1 - si el metodo se cumple satisfactoriamente
    # return 2 - si el valorIngresado es menor al cobro total
    # return 3 - si el tiquete no existe en el sistema
    # valorIngresado: cantidad a cobrar al propietario del vehiculo
    def pagarSalida(self, valorIngresado):
        mensaje = "None"
        if self.tiquete is not None:
            if valorIngresado >= self.tiquete.cobro:
                try:
                    with self.conect.cursor() as cursor:
                        self.lista_vehiculos.remove(self.vehiculo)
                        placa = self.vehiculo.placa
                        sql = "UPDATE vehiculo SET cancelado = 1 WHERE placa =('%s')" % (placa)
                        cursor.execute(sql)
                        self.conect.commit()
                        if self.tiquete.descuento:
                            descuento = 1
                        else:
                            descuento = 0

                        sql = "UPDATE tiquete SET horaSalida =('%s'), fechaSalida =('%s'), tiempo =('%s'), cobro =(%i), descuento =(%i), cancelado = 1 WHERE idTiquete = (%i)" % (
                            self.tiquete.horaSalida, self.tiquete.fechaSalida, self.tiquete.tiempo,
                            self.tiquete.cobro,
                            descuento, self.tiquete.idTiquete)
                        cursor.execute(sql)
                        self.conect.commit()
                        mensaje = self.mostrarTiqueteSalida(self.vehiculo, self.tiquete)
                        self.vehiculo = None
                        self.tiquete = None
                        return 1, mensaje
                except:
                    self.conect.rollback()
                    return -1, mensaje


            else:
                return 2, mensaje
        else:
            return 3, mensaje

    # metodo que permite realizar un cierre de caja al final de la jornada
    def calcularCierreCaja(self):
        producido: int = 0
        estado = False
        fechaActual = datetime.today()
        fechaActualAux = fechaActual.strftime(self.FORMATO_FECHA)

        try:
            with self.conect.cursor() as cursor:
                sql = "SELECT SUM(cobro) FROM tiquete WHERE fechaSalida =('%s') AND cancelado = (%d)" % (
                    fechaActualAux, 1)
                cursor.execute(sql)
                self.conect.commit()
                resultado = cursor.fetchone()
                if resultado[0] is None:
                    producido = 0
                else:
                    producido = resultado[0]
                estado = True

        except:
            raise CierreCajaException("Ocurrio un error con la transacción, vuelva a interlo mas tarde")

        return producido, estado

    def guardarCuadre(self):
        producido, estado = self.calcularCierreCaja()
        fechaActual = datetime.today()
        fechaActualAux = fechaActual.strftime(self.FORMATO_FECHA)
        idCuadre = -1
        cuadre = None
        try:
            with self.conect.cursor() as cursor:
                sql = "SELECT idUsuario FROM usuario WHERE cedula = ('%s')" % (self.usuario.cedula)
                cursor.execute(sql)
                resultado = cursor.fetchone()
                idUsuario = resultado[0]

                sql = "INSERT INTO cierrecaja (idUsuario, fecha, valor) VALUES (%d, '%s', %d)" % (
                    idUsuario, fechaActualAux, producido)
                cursor.execute(sql)
                self.conect.commit()
                sql = "SELECT idCuadre FROM cierrecaja ORDER BY idCuadre DESC LIMIT 1"
                cursor.execute(sql)
                resultado = cursor.fetchone()
                idCuadre = resultado[0]
                cuadre = Cuadre.Cuadre(self, idCuadre, self.usuario, fechaActualAux, producido)
                self.listaCuadres.append(cuadre)
        except:
            raise CierreCajaException("Error al calcular el cuadre, vuelva a intentarlo mas tarde")

        return cuadre

    def imprimirCuadre(self):
        cuadre: Cuadre = self.guardarCuadre()

        mensaje = "CUADRE DIARIO\n"
        mensaje += self.NOMBRE + "\n"
        mensaje += "Regimen: " + self.REGIMEN + "   " + self.NIT + "\n"
        mensaje += "Direccion: " + self.direccion + "  Telefono: " + self.telefono + "\n"
        mensaje += "Numero de Factura: " + str(cuadre.idCuadre) + "\n"
        mensaje += "Fecha: " + cuadre.fecha + "\n"
        mensaje += "Cajero: " + self.usuario.nombres + " " + self.usuario.apellidos + "\n"
        mensaje += "----------------------------------------\n"
        mensaje += "Total Producido: " + str(cuadre.valor) + "\n"
        mensaje += "----------------------------------------\n"
        return mensaje

    """metodo que permite modificar la tarifa de los vehiculos
    hora_carro: nueva tarifa del carro
    hora_moto: nueva tarifa de la moto
    caro_mensualidad: nueva tarifa de mensualidad carro
    moto_mensualidad: nueva tarifa de mensualidad moto
    
    """

    def modificarTarifa(self, hora_carro, hora_moto, caro_mensualidad, moto_mensualidad):
        self.HORA_MOTO = hora_moto
        self.HORA_CARRO = hora_carro
        self.CARRO_MENS = caro_mensualidad
        self.MOTO_MENS = moto_mensualidad

    def cambiarPrecio(self, nuevo_cobro: int):

        if self.vehiculo is not None:
            if self.tiquete is not None:
                if nuevo_cobro >= 0:
                    self.tiquete.cobro = nuevo_cobro
                else:
                    raise Exception("El valor ingresado debe ser positivo")
            else:
                raise TiqueteException("El tiquete no es valido")
        else:
            raise PlacaErrorException("El vehculo no se encuentra en el parqueadero")

    # Metodo para imprimir la informacion en el tiquete
    # vehiculo: vehiculo que ingresa al parqueadero
    # tiquete: tiquete asignado al ingreso del vehiculo
    def mostrarTiqueteEntrada(self, vehiculo: Vehiculo, tiquete: FacturaDia):
        mensaje = "TIQUETE DE ENTRADA"
        mensaje += self.NOMBRE + "\n"
        mensaje += "Regimen: " + self.REGIMEN + "   " + self.NIT + "\n"
        mensaje += "Direccion: " + self.direccion + "Telefono: " + self.telefono + "\n"
        mensaje += "Atendido por: " + self.usuario.nombres + "\n"
        mensaje += "------------------------------------------\n\n"
        mensaje += "Placa: " + vehiculo.placa + "\n\n"
        mensaje += "--------------------------------------------\n"
        mensaje += "Numero de Factura: " + str(tiquete.idTiquete) + "\n"
        mensaje += "Hora Entrada: " + tiquete.horaEntrada + "\n"
        mensaje += "Fecha Entrada: " + tiquete.fechaEntrada + "\n"
        mensaje += "Tipo Vehiculo: " + vehiculo.tipo_vehiculo + "\n"
        if vehiculo.tipo_vehiculo == "CARRO":
            mensaje += "Valor Hora: " + str(self.HORA_CARRO) + "\n"
        else:
            mensaje += "Valor Hora: " + str(self.HORA_MOTO) + "\n"
        mensaje += "------------------------------------------\n"
        mensaje += "Horario:\n"
        mensaje += self.horario

        return mensaje

    # metodo para imprimir la informacion del tiquete de salida de un vehiculo
    # vehiculo: vehiculo que sale del parqueadero
    # tiquete: tiquete de la entrada del vehiculo
    def mostrarTiqueteSalida(self, vehiculo: Vehiculo, tiquete: FacturaDia):
        mensaje = "TIQUETE DE SALIDA" + "\n"
        mensaje += self.NOMBRE + "\n"
        mensaje += "Regimen: " + self.REGIMEN + "   " + self.NIT + "\n"
        mensaje += "Direccion: " + self.direccion + "Telefono: " + self.telefono + "\n"
        mensaje += "================================================================\n"
        mensaje += "Numero de Factura: " + str(tiquete.idTiquete) + "\n"
        mensaje += "Hora: " + tiquete.horaSalida + "   Fecha: " + tiquete.fechaSalida + "\n"
        mensaje += "Atendido por: " + self.usuario.nombres + " " + self.usuario.apellidos + "\n"
        mensaje += "-----------------------------------------------------------------\n\n"
        mensaje += "Placa: " + vehiculo.placa + "\n\n"
        mensaje += "--------------------------------------------\n"
        mensaje += "Hora Entrada: " + tiquete.horaEntrada + "\n"
        mensaje += "Fecha Entrada: " + tiquete.fechaEntrada + "\n"
        mensaje += "Hora Salida: " + tiquete.horaSalida + "\n"
        mensaje += "Fecha Salida: " + tiquete.fechaSalida + "\n"
        mensaje += "Total Tiempo: " + str(tiquete.tiempo) + "\n"
        if tiquete.descuento == True:
            if vehiculo.tipo_vehiculo == "CARRO":
                mensaje += "Descuento: $" + str(self.HORA_CARRO) + "\n"
            else:
                mensaje += "Descuento: $" + str(self.HORA_MOTO) + "\n"
        else:
            mensaje += "Descuento: $0 " + "\n"
        mensaje += "Total a Pagar: $" + str(tiquete.cobro) + "\n"
        mensaje += "-------------------------------------------------------------------\n"
        mensaje += "TIQUETE DE SALIDA DEL VEHICULO"
        return mensaje

    # metodo que permite imprimir la informacion de un tiquete de tipo mensualidad
    # m: mensualidad que se genero al ingresar el vehiculo
    def mostrarTiqueteMensualidad(self, m: Mensualidad):
        sql = "select idTiquete from mensualidad where placa = ('%s') " % (m.vehiculo.placa)
        try:
            with self.conect.cursor() as cursor:
                cursor.execute(sql)
                idTiquete = cursor.fetchone()
        except:
            print("eror")

        fechaActual = datetime.today()
        fechaAux = fechaActual.strftime(self.FORMATO_FECHA)
        mensaje = "TIQUETE DE MENSUALIDAD" + "\n"
        mensaje += self.NOMBRE + "\n"
        mensaje += "Regimen: " + self.REGIMEN + "   " + self.NIT + "\n"
        mensaje += "Direccion: " + self.direccion + "Telefono: " + self.telefono + "\n"
        mensaje += "Fecha: " + fechaAux + "\n"
        mensaje += "Atendido por: " + self.usuario.nombres + "\n"
        mensaje += "------------------------------------------\n\n"
        mensaje += "Placa: " + m.vehiculo.placa + "\n\n"
        mensaje += "--------------------------------------------\n"
        mensaje += "Numero de Factura: " + str(idTiquete) + "\n"
        mensaje += "Fecha Entrada: " + m.fechaEntrada + "\n"
        mensaje += "Fecha Entrada: " + m.fechaSalida + "\n"
        mensaje += "Tipo Vehiculo: " + m.tipo_vehiculo + "\n"
        mensaje += "valor a pagar: " + str(m.valor) + "\n"
        mensaje += "------------------------------------------\n"
        mensaje += "Horario:\n"
        mensaje += self.horario

        return mensaje
