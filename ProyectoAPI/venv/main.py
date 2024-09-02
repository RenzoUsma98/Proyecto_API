from ui import pedir_datos
from ui import formatear_datos
from api import consultar_datos


def main():
    """
    Función principal que ejecuta el flujo del programa.

    - Primero, solicita los datos de entrada al usuario (cantidad de registros y nombre del departamento).
    - Luego, consulta los datos desde la API con base en la entrada del usuario.
    - Finalmente, formatea y muestra los datos consultados en un formato legible.
    """

    # Solicita al usuario la cantidad de registros y el nombre del departamento.
    cantidad_registros, nombre_departamento = pedir_datos()

    # Consulta los datos desde la API con los parámetros proporcionados por el usuario.
    results_df = consultar_datos(cantidad_registros, nombre_departamento)

    # Formatea y muestra los datos obtenidos de la API.
    formatear_datos(results_df)


# Este bloque asegura que la función main() se ejecute solo si este archivo se ejecuta directamente,
# y no si se importa como un módulo en otro script.
if __name__ == "__main__":
    main()
