from co.edu.uniquindio.parkingsoft.logica import Parqueadero, Vehiculo
from co.edu.uniquindio.parkingsoft.LogicaUI import Principal


class Prueba():

    def correr(self):
        c = Vehiculo.Vehiculo('1', 0)
        a = Vehiculo.Vehiculo('2', 0)
        b = Vehiculo.Vehiculo('3', 1)
        prueba = Vehiculo.Vehiculo('ALZATEL', 0)
        parq = Parqueadero.Parqueadero('PQ Uniquindio', 12, [], [500, 1000])

        principal = Principal.Principal(parq)
        principal.ingresoVehiculo(prueba, parq)
        principal.salidaVehiculo(prueba, parq)

        principal.ingresoVehiculo(b, parq)
        principal.ingresoVehiculo(a, parq)
        principal.ingresoVehiculo(c, parq)
        principal.salidaVehiculo(b, parq)

        principal.cierreDeCaja()


if __name__ == '__main__':
    pp = Prueba()
    pp.correr()
