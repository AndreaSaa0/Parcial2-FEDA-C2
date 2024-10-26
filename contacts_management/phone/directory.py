from phone.contact import Contact

class Directory:
    """
    Clase Directorio:

    Atributos:
    contactos: Matriz que contiene todos los contactos, incluyendo la primera fila como encabezado.

    Métodos:
    __init__: Inicializa la matriz contactos con la primera fila como encabezado de atributos.
    agregar_contacto: Agrega un nuevo contacto a la matriz.
    listar_contactos: Muestra todos los contactos en la matriz, incluyendo el encabezado.
    """

    def __init__(self):
        self.contacts = []

    def add_contact(self, nombre, apellido, organizacion, telefono, direccion):
        nuevo_contacto = Contact(nombre, apellido, organizacion, telefono, direccion)
        self.contacts.append(nuevo_contacto)

    def list_contacts(self):
        for contact in self.contacts:
            print(contact.obtener_datos())