class Contact:

    """
    Atributos:
    datos: Lista que contiene los valores de los atributos del contacto (nombre, apellido, organización, teléfono, dirección).
    
    Métodos:
    __init__: Inicializa el contacto con los atributos necesarios y los almacena en una lista.
    obtener_datos: Retorna la lista con los datos del contacto.

    """

    def __init__(self, nombre, apellido, organizacion, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.organizacion = organizacion
        self.telefono = telefono
        self.direccion = direccion
    
    def obtener_datos(self):
        return [self.nombre, self.apellido, self.organizacion, self.telefono, self.direccion]