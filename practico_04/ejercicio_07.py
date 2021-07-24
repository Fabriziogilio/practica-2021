"""Base de Datos SQL - Uso de múltiples tablas"""

import sqlite3
import datetime

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona

def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    busqueda = buscar_persona(id_persona)

    if busqueda is not False:

        db = sqlite3.connect("base_datos.db")
        cursor = db.cursor()
        command1 = """SELECT * FROM PersonaPeso WHERE fecha>?;"""
        result = cursor.execute(command1, (fecha))

        if result is None:
            command2 = """INSERT INTO PersonaPeso (id_Persona, fecha, peso) values (?,?,?);"""
            cursor.execute(command2, (id_persona, fecha, peso))
            db.commit()

            ultimo_id = cursor.lastrowid
            db.close()

            return ultimo_id
        return False
    return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
