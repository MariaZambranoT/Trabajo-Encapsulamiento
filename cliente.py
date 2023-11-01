from persona import Persona
class Cliente (Persona):
    contador_cliente = 0

    def init(self, nombre, apellido, fecha_registro, vip):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_registro = fecha_registro
        self._vip = vip
        Cliente.contador_cliente += 1
        self._id_cliente = Cliente.contador_cliente

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def str(self):
        return f'Cliente: {self.dict.str()}'

if __name__ == 'main':
    cli1 = Cliente(nombre='Melanie', apellido='Alvear', fecha_registro='13-10-2023', vip= True)
    print(cli1)
