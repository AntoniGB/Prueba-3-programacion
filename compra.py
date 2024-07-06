from datetime import datetime
from siuu import generar_id_compra

compras = []

def registrar_compra(id_cliente, fecha, monto):
    global compras
    puntos_acumulados = int(monto * 0.01)
    nueva_compra = {
        'id': generar_id_compra(),
        'id_cliente': id_cliente,
        'fecha': fecha,
        'monto': monto,
        'puntos': puntos_acumulados
    }
    compras.append(nueva_compra)

def listar_compras_cliente(id_cliente):
    global compras
    cliente_compras = [compra for compra in compras if compra['id_cliente'] == id_cliente]
    if not cliente_compras:
        print("El cliente no tiene compras registradas.")
    else:
        print("Fecha de Compra - Monto - Total Puntos")
        for compra in cliente_compras:
            print(f"{compra['fecha']} - ${compra['monto']} - {compra['puntos']}")

def generar_resumen_cliente(id_cliente):
    global compras
    cliente = next((cliente for cliente in cliente if cliente['id'] == id_cliente), None)
    if cliente:
        nombre_cliente = cliente['nombre']
        compras_cliente = [compra for compra in compras if compra['id_cliente'] == id_cliente]
        puntos_totales = sum(compra['puntos'] for compra in compras_cliente)
        
        filename = f"RESUMEN_CLIENTE_ID_{id_cliente}.txt"
        with open(filename, 'w') as f:
            f.write(f"ID CLIENTE: {id_cliente}\n")
            f.write(f"NOMBRE CLIENTE: {nombre_cliente}\n")
            f.write("Fecha de Compra  Monto  Total Puntos\n")
            for compra in compras_cliente:
                f.write(f"{compra['fecha']}    ${compra['monto']}    {compra['puntos']}\n")
            f.write(f"PUNTOS TOTALES A CANJEAR: {puntos_totales} pesos\n")
        
        print(f"Se ha generado el resumen del cliente {nombre_cliente} en el archivo {filename}")
    else:
        print("Cliente no encontrado.")



