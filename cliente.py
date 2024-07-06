clientes = []

def registrar_cliente(nombre, apellido, correo):
    global clientes
    nombre_completo = f"{nombre.upper()} {apellido.upper()}"
    nuevo_cliente = {
        'id': len(clientes) + 1,
        'nombre': nombre_completo,
        'correo': correo
    }
    clientes.append(nuevo_cliente)

def listar_clientes():
    global clientes
    if not clientes:
        print("no hay clientes registrados.")
    else:
        print("ID - Nombre - Correo")
        for cliente in clientes:
            print(f"{cliente['id']} - {cliente['nombre']} - {cliente['correo']}")


