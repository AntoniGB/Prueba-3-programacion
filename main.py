import cliente
import compra
import siuu

def menu_principal():
    print("\n.-+++++SISTEMA DE PUNTOS CANJEABLES+++++-.")
    print("1. registrar cliente")
    print("2. listar clientes registrados")
    print("3. registrar compra")
    print("4. listar compras de un cliente")
    print("5. enviar Información de puntos acumulados a un cliente")
    print("6. salir")

def registrar_cliente():
    nombre = input("ingrese el nombre del cliente: ")
    apellido = input("ingrese el apellido del cliente: ")
    correo = input("ingrese el correo electrónico del cliente: ")
    cliente.registrar_cliente(nombre, apellido, correo)
    print("cliente registrado correctamente")

def listar_clientes():
    cliente.listar_clientes()

def registrar_compra():
    id_cliente = int(input("ingrese el ID del cliente: "))
    fecha = input("ingrese la fecha de la compra (DD-MM-AAAA): ")
    monto = float(input("ingrese el monto de la compra: $"))
    compra.registrar_compra(id_cliente, fecha, monto)
    print("compra registrada correctamente.")

def listar_compras_cliente():
    id_cliente = int(input("ingrese el ID del cliente: "))
    compra.listar_compras_cliente(id_cliente)

def enviar_resumen_cliente():
    id_cliente = int(input("ingrese el ID del cliente para generar el resumen: "))
    cliente_info = next((c for c in cliente.clientes if c['id'] == id_cliente), None)
    if cliente_info:
        nombre_cliente = cliente_info['nombre']
        compras_cliente = [c for c in compra.compras if c['id_cliente'] == id_cliente]
        puntos_totales = compra.calcular_puntos_totales(id_cliente)
        filename = siuu.escribir_resumen_cliente(id_cliente, nombre_cliente, compras_cliente, puntos_totales)
        print(f"se ha generado el resumen del cliente {nombre_cliente} en el archivo {filename}")
    else:
        print("cliente no se encuentra")

def main():
    while True:
        menu_principal()
        opcion = input("Ingrese la opción deseada: ")
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            listar_clientes()
        elif opcion == '3':
            registrar_compra()
        elif opcion == '4':
            listar_compras_cliente()
        elif opcion == '5':
            enviar_resumen_cliente()
        elif opcion == '6':
            print("saliendo del sistemon...")
            break
        else:
            print("opcion no valida. Porfa intente de nuevo")

if __name__ == "__main__":
    main()


