# coding: utf-8

# clase que modela los usuarios del sistema, existen dos tipos, administrador y empleado
class Usuario():
    nombres: str  # nombre del usuario
    apellidos : str
    cedula: str  # cedula del usuario
    nombre_usuario : str  # usuario de inicio del usuario
    password: str  # contraseña del usuario
    correo: str  # correo del usuario
    tipo: str  # 1 administrador, 0 empleado

    # Constructor de la clase
    def __init__(self, cedula, nombres, apellidos,  nombre_usuario, password, tipo):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.tipo = tipo
