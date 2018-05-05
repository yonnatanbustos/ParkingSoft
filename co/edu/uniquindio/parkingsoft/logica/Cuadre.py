from co.edu.uniquindio.parkingsoft.logica import Usuario, Parqueadero


class Cuadre():
    idCuadre: int
    usuario: Usuario
    fecha: str
    valor: int
    parqueadero: Parqueadero

    def __init__(self, parqueadero: Parqueadero, idCuadre, usuario: Usuario, fecha, valor):
        self.parqueadero = parqueadero
        self.idCuadre = idCuadre
        self.usuario = usuario
        self.fecha = fecha
        self.valor = valor

