from fastapi import FastAPI
from .routers.clientes import enrutador_clientes
from .routers.bill import enrutador_facturas
from .routers.transactions import enrutador_transacciones
from .database import crear_tablas

aplicacion = FastAPI(lifespan=crear_tablas)

# Enrutador de Clientes
aplicacion.include_router(enrutador_clientes, tags=["clientes"])
# Enrutador de Facturas
aplicacion.include_router(enrutador_facturas, tags=["facturas"])
# Enrutador de Transacciones
aplicacion.include_router(enrutador_transacciones, tags=["transacciones"])
"""
Modelos del proyecto

Transacción
Factura
Factura(
    id,
    fecha,
    cliente,
    valor_total
)
Transacción(
    id,
    descripción,
    factura
)
"""

# Comandos de Git
# git log
# Muestra el historial de cambios.
# git log --oneline
# Muestra el historial resumido en una sola línea.
# git checkout <código_del_commit>
# Permite cambiar a un commit específico.