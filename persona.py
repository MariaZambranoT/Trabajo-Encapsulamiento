class Persona:
    contador_personas= 0

    def init(self, nombre:str, apellido:str, cedula:str, correo:str):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._correo = correo

    def str(self):
        return f'Persona {self.dict.str()}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def cedula(self):
        return self.cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def correo(self):
        return self.correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

if __name__ == 'main':
    objPersona1 = Persona(nombre='Karla', apellido='Paz', cedula='0123456789', correo='kperez@mail.com')
    print(objPersona1.str())