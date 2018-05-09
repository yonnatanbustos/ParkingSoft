import time
from datetime import datetime, timedelta

from PyQt5 import QtGui
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QTableWidgetItem
from pymysql import connect

from co.edu.uniquindio.parkingsoft.excepciones.MensualidadException import MensualidadException
from co.edu.uniquindio.parkingsoft.excepciones.VehiculoYaExiste import VehiculoYaExiste
from co.edu.uniquindio.parkingsoft.logica import Usuario, FacturaDia, Vehiculo, Mensualidad


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
        print(conect.open)
        self.conect = conect
        print(self.conect.open)
        self.tiquete = None
        self.vehiculo = None
        self.usuario = None
        self.consultas()

    def consultas(self):
        try:
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
                    if descuento == True:
                        self.tiquete.descuento = 1
                    else:
                        self.tiquete.descuento = 0

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
    # return -1 - las fechas de entrada y salida, estan por fuera de la fecha actual
    # return 1 - se registro la mensualidad satisfactoriamente
    # retrun 2 - el vehiculo ya esta registrado en la mensualidad
    # return 3 - la placa del vehciulo es menor a 5
    # return 4 - la dias de la mensualidad no se encuentra en el rago de pago (rango de dias: 15-31 dias)
    # return 5 - la fecha de entrada es mayor a la fecha de salida
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
    def buscarVehiculoMensualida(self, placa):
        for m in self.listaMensualidades:
            if m.placa == placa:
                return m
        return None

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

                        sql = "UPDATE tiquete SET horaSalida =('%s'), fechaSalida =('%s'), tiempo =('%s'), cobro =(%i), descuento =(%i), cancelado = 1 WHERE idTiquete = (%i)" % (
                            self.tiquete.horaSalida, self.tiquete.fechaSalida, self.tiquete.tiempo,
                            self.tiquete.cobro,
                            self.tiquete.descuento, self.tiquete.idTiquete)
                        cursor.execute(sql)
                        self.conect.commit()
                        mensaje = self.mostrarTiqueteSalida(self.vehiculo, self.tiquete)
                        return 1, mensaje
                except:
                    self.conect.rollback()
                    return -1, mensaje


            else:
                return 2, mensaje
        else:
            return 3, mensaje

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
                producido = resultado[0]
                estado = True

        except:
            print("Error en el cierre de caja")

        return producido, estado

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
