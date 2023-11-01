from persona import Persona


class Empleado(Persona):
    contador_empleados= 0

    def init(self, id_empleado, sueldo, nombre, apellido, cedula):
        self._id_empleado = id_empleado
        self._sueldo = sueldo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def str(self):
        return f'Empleado {self.dict.str()}'


if __name__ == 'main':
    e1 = Empleado(nombre='Carlos', apellido='Aviles', sueldo='2000', cedula='173837584', id_empleado=1)
    print(e1)