import uuid

def generar_id_compra():
    return str(uuid.uuid4().fields[-1])[:6]


