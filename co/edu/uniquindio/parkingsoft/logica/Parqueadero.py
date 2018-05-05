import time
from datetime import datetime, timedelta

from PyQt5 import QtGui
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import QTableWidgetItem

from co.edu.uniquindio.parkingsoft.excepciones.VehiculoYaExiste import VehiculoYaExiste
from co.edu.uniquindio.parkingsoft.logica import Usuario, FacturaDia, Vehiculo, Mensualidad


# clase que modela un objeto tipo parqueadero.
class Parqueadero():
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
    NOMBRE: str = "EL PARQUEADERO EL ÑINO JAIR"
    direccion: str = "Calle 18 #17-47"
    telefono: str = "Armenia"
    horario: str = "Lunes a Sabado 7:30am-7:30pm\n" \
                   "Domingos y Festivos 8am-2:30pm"
    NIT: str = "1038405474-5"
    REGIMEN: str = "SIMPLIFICADO"

    db: QSqlDatabase
    tiquete: FacturaDia
    vehiculo: Vehiculo
    usuario: Usuario

    # constructor de la clase
    def __init__(self, db: QSqlDatabase):
        self.lista_vehiculos = []
        self.listaUsuarios = []
        self.listaFacturas = []
        self.listaMensualidades = []
        self.db = db
        self.tiquete = None
        self.vehiculo = None
        self.usuario = None
        print(self.db.databaseName())
        self.consultas()

    def consultas(self):
        estado = self.db.open()
        if estado:
            sql = "SELECT * FROM usuario"
            query = QSqlQuery(sql)
            while query.next():
                cedula = query.value(1)
                print("cedula ", cedula)
                nombres = query.value(2)
                apellidos = query.value(3)
                nombre_usuario = query.value(4)
                password = query.value(5)
                tipo = query.value(6)
                usuario = Usuario.Usuario(cedula, nombres, apellidos, nombre_usuario, password, tipo)
                self.listaUsuarios.append(usuario)

            sql = "SELECT * FROM vehiculo"
            query = QSqlQuery(sql)
            while query.next():
                placa = query.value(1)
                tipoVehiculo = query.value(2)
                idTiquete = query.value(3)
                cancelado = query.value(4)
                if cancelado == 0:
                    vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                    vehiculo.idTiquete = idTiquete
                    self.lista_vehiculos.append(vehiculo)

            sql = "SELECT * FROM tiquete"
            query = QSqlQuery(sql)
            while query.next():
                idTiquete = query.value(0)
                horaEntrada = query.value(1)
                fechaEntrada = query.value(2)
                horaSalida = query.value(3)
                fechaSalida = query.value(4)
                tiempo = query.value(5)
                cobro = query.value(6)
                descuento = query.value(7)
                cancelado = query.value(8)
                if cancelado == 0:
                    tiquete = FacturaDia.FacturaDia(self, idTiquete, horaEntrada, fechaEntrada)
                    tiquete.horaSalida = horaSalida
                    tiquete.fechaSalida = fechaSalida
                    tiquete.tiempo = tiempo
                    tiquete.cobro = cobro
                    tiquete.descuento = descuento
                    self.listaFacturas.append(tiquete)

            sql = "SELECT * FROM mensualidad"
            query = QSqlQuery(sql)
            while query.next():
                estado = int(query.value(1))
                placa = str(query.value(2))
                tipoVehiculo = str(query.value(3))
                vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                propietario = str(query.value(4))
                telefono = str(query.value(5))
                fechaEntrada = str(query.value(7))
                fechaSalida = str(query.value(8))
                mensualidad = Mensualidad.Mensualidad(self, vehiculo, propietario, telefono, fechaEntrada,
                                                      fechaSalida, estado)

                self.listaMensualidades.append(mensualidad)


        else:
            print("no se conecto base de datos")
        self.db.close()

    def registrarUsuario(self, cedula, nombres, apellidos, nombre_usuario, password, tipo):

        if self.buscarUsuario(nombre_usuario) == None:
            if self.buscarUsuarioCedula(cedula) == None:
                nuevoUsuario = Usuario.Usuario(cedula, nombres, apellidos, nombre_usuario, password, tipo)
                self.listaUsuarios.append(nuevoUsuario)
                return True
            else:
                return False
        else:
            return False

    def buscarUsuarioCedula(self, cedula):

        for u in self.listaUsuarios:
            if u.cedula == cedula:
                return u
        return None

    def iniciarSesion(self, nombreUsuario, password):
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

    def ingresoVehicular(self, placa: str, tipoVehiculo: str):
        self.db.open()
        mensaje = "None"
        if len(placa) >= 5:
            vehiculo = self.buscarVehiculo(placa)

            if vehiculo is None:

                vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                factura = self.registrarFactura()
                vehiculo.setIdTiquete(factura.idTiquete)
                self.lista_vehiculos.append(vehiculo)
                sql = "INSERT INTO vehiculo (placa, tipoVehiculo, idTiquete, cancelado) " \
                      "VALUES (:placa, :tipoVehiculo, :idTiquete, :cancelado)"
                query = QSqlQuery()
                query.prepare(sql)
                query.bindValue(":placa", vehiculo.placa)
                query.bindValue(":tipoVehiculo", vehiculo.tipo_vehiculo)
                query.bindValue(":idTiquete", vehiculo.idTiquete)
                query.bindValue(":cancelado", 0)
                query.exec_()
                mensaje = self.mostrarTiqueteEntrada(vehiculo, factura)
                return mensaje, True
            else:
                raise VehiculoYaExiste()
        else:
            print("Placa < 5")

        self.db.close()
        return mensaje, False

    def obtenerIdTiquete(self):
        self.db.open()
        idTiquete = -1
        sql = "SELECT idTiquete FROM tiquete ORDER BY idTiquete DESC LIMIT 1"
        query = QSqlQuery(sql)
        while query.next():
            idTiquete = int(query.value(0))
        return idTiquete

    def registrarFactura(self):
        horaEntrada = time.strftime(self.FORMATO_HORA)
        fechaEntrada = time.strftime(self.FORMATO_FECHA)
        sql = "INSERT INTO tiquete (horaEntrada, fechaEntrada, cancelado) VALUES (:horaEntrada, :fechaEntrada, :cancelado)"
        query = QSqlQuery()
        query.prepare(sql)
        query.bindValue(":horaEntrada", horaEntrada)
        query.bindValue(":fechaEntrada", fechaEntrada)
        query.bindValue(":cancelado", 0)
        query.exec_()

        idTiquete = self.obtenerIdTiquete()

        factura = FacturaDia.FacturaDia(self, idTiquete, horaEntrada, fechaEntrada)
        self.listaFacturas.append(factura)
        return factura

    # metodo que busca un vehiculo dentro del parqueadero

    def buscarVehiculo(self, placa):
        for p in self.lista_vehiculos:
            if p.placa == placa:
                return p
        return None

    # metodo que permite la salida de un vehiculo

    def salidaVehiculo(self, placa, descuento):
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
                    self.tiquete.descuento = descuento

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
                totalCobro = totalCobro + (self.HORA_CARRO / 2)

            return totalCobro
        else:
            totalCobro = totalCobro * self.HORA_MOTO + (horas * self.HORA_MOTO)
            if minutos > 30:
                totalCobro = totalCobro + self.HORA_MOTO
            else:
                totalCobro = totalCobro + (self.HORA_MOTO / 2)

        return totalCobro

    # Metodo para buscar un tiquete registrado en el parqueadero
    def buscarTiquete(self, idTiquete):
        for t in self.listaFacturas:
            if t.idTiquete == idTiquete:
                return t
        return None

    # Metodo para calcular el total de tiempo transcurrido de un vehiculo
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
    # return 1 - se registro la mensualidad satisfactoriamente
    # retrun 2 - el vehiculo ya esta registrado en la mensualidad
    # return 3 - la placa del vehciulo es menor a 5
    # return 4 - la fecha de salida es menor a la de entrada
    def ingresarMensualida(self, placa, tipoVehiculo, propietario, telefono, fechaEntrada, fechaSalida):
        self.db.open()
        # retornos : 1-primer if, 2-segundo if, 3-tercer if, 0 se cumplio bien el metodo
        # definir la condicion de que la fechaEntrada sea menor a la fechaSalida
        if fechaSalida > fechaEntrada:
            if len(placa) >= 5:
                vehiculo = self.buscarVehiculoMensualida(placa)
                if vehiculo is None:
                    vehiculo = Vehiculo.Vehiculo(placa, tipoVehiculo)
                    mensualida = Mensualidad.Mensualidad(self, vehiculo, propietario, telefono, fechaEntrada,
                                                         fechaSalida, 1)
                    self.listaMensualidades.append(mensualida)

                    sql = "INSERT INTO mensualidad (estado, placa, tipoVehiculo, propietario, telefono, valor, fechaEntrada, fechaSalida)" \
                          "VALUES (:estado, :placa, :tipoVehiculo, :propietario, :telefono, :valor, :fechaEntrada, :fechaSalida)"
                    query = QSqlQuery()
                    query.prepare(sql)
                    query.bindValue(":estado", 1)
                    query.bindValue(":placa", vehiculo.placa)
                    query.bindValue(":tipoVehiculo", vehiculo.tipo_vehiculo)
                    query.bindValue(":propietario", propietario)
                    query.bindValue(":telefono", telefono)
                    if vehiculo.tipo_vehiculo == "CARRO_MENS":
                        query.bindValue(":valor", self.CARRO_MENS)
                    else:
                        query.bindValue(":valor", self.MOTO_MENS)
                    query.bindValue(":fechaEntrada", fechaEntrada)
                    query.bindValue(":fechaSalida", fechaSalida)
                    query.exec_()

                    self.db.close()
                    return 1
                else:
                    return 2
            else:
                return 3
        else:
            return 4

    # Metodo para buscar vehiculos de mensualida en el parqueadero
    def buscarVehiculoMensualida(self, placa):
        for m in self.listaMensualidades:
            if m.placa == placa:
                return m
        return None

    def modificarMensualidad(self, mensualidad: Mensualidad):
        if mensualidad is not None:
            hola = 1

    # Metodo para listar todas las mensualidades del parqueadero
    def actualizarTablaMensualida(self, tabla):
        row = 0
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
            row += 1

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
    def pagarSalida(self, valorIngresado):
        self.db.open()
        mensaje = "None"
        if self.tiquete is not None:
            if valorIngresado >= self.tiquete.cobro:
                self.lista_vehiculos.remove(self.vehiculo)
                sql = "UPDATE vehiculo SET cancelado = 1 WHERE placa =(:placa)"
                query = QSqlQuery()
                query.prepare(sql)
                query.bindValue(":placa", self.vehiculo.placa)
                query.exec_()
                sql = "UPDATE tiquete SET horaSalida =(:horaSalida), fechaSalida =(:fechaSalida), tiempo =(:tiempo)," \
                      "cobro =(:cobro), descuento =(:descuento), cancelado = 1 WHERE idTiquete = (:idTiquete)"
                query.prepare(sql)
                query.bindValue(":horaSalida", self.tiquete.horaSalida)
                query.bindValue(":fechaSalida", self.tiquete.fechaSalida)
                query.bindValue(":tiempo", self.tiquete.tiempo)
                query.bindValue(":cobro", self.tiquete.cobro)
                query.bindValue(":descuento", self.tiquete.descuento)
                query.bindValue(":idTiquete", self.tiquete.idTiquete)
                query.exec_()

                self.db.close()
                mensaje = self.mostrarTiqueteSalida(self.vehiculo, self.tiquete)
                return 1, mensaje
            else:
                self.db.close()
                return 2, mensaje
        else:
            self.db.close()
            return 3, mensaje

    def modificarTarifa(self, horaCarro, horaMoto):
        self.HORA_MOTO = horaMoto
        self.HORA_CARRO = horaCarro

    # Metodo para imprimir la informacion en el tiquete
    def mostrarTiqueteEntrada(self, vehiculo: Vehiculo, tiquete: FacturaDia):
        mensaje = self.NOMBRE + "\n"
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

    def mostrarTiqueteSalida(self, vehiculo: Vehiculo, tiquete: FacturaDia):
        mensaje = self.NOMBRE + "\n"
        mensaje += "Regimen: " + self.REGIMEN + "   " + self.NIT + "\n"
        mensaje += "Direccion: " + self.direccion + "Telefono: " + self.telefono + "\n"
        mensaje += "================================================================\n"
        mensaje += "Numero de Factura: " + str(tiquete.idTiquete) + "\n"
        mensaje += "Hora: " + tiquete.horaSalida + "    " + "Fecha: " + tiquete.fechaSalida + "\n"
        mensaje += "Atendido por: " + self.usuario.nombres + " " + self.usuario.apellidos + "\n"
        mensaje += "-----------------------------------------------------------------\n\n"
        mensaje += "Placa: " + vehiculo.placa + "\n\n"
        mensaje += "--------------------------------------------\n"
        mensaje += "Hora Entrada: " + tiquete.horaEntrada + "\n"
        mensaje += "Fecha Entrada: " + tiquete.fechaEntrada + "\n"
        mensaje += "Hora Salida: " + tiquete.horaSalida + "\n"
        mensaje += "Fecha Salida: " + tiquete.fechaSalida + "\n"
        mensaje += "Total Tiempo: " + str(tiquete.tiempo) + "\n"
        if tiquete.descuento:
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
