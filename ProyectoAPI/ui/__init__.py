# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pedir_datos():
    """
    Solicita al usuario la cantidad de registros y el nombre del departamento.

    Retorna:
        - cantidad_registros (int): Número de registros a consultar (máximo 1000).
        - nombre_departamento (str): Nombre del departamento ingresado por el usuario en mayúsculas.
    """
    nombre_departamento = input("Departamento: ").upper()
    cantidad_registros = int(input("Cantidad registros (máximo 1000): "))

    # Limita la cantidad de registros a 1000 si se ingresa un valor mayor
    if cantidad_registros > 1000:
        cantidad_registros = 1000

    return cantidad_registros, nombre_departamento


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def filtrar_datos(results_df):
    """
    Filtra y ajusta el DataFrame para asegurarse de que la columna 'pais_viajo_1_nom' esté presente.

    Recibe:
        - results_df (DataFrame): DataFrame que contiene los datos obtenidos de la API.

    Retorna:
        - results_df (DataFrame): DataFrame con la columna 'pais_viajo_1_nom' añadida si no estaba presente.
    """
    # Verifica si la columna 'pais_viajo_1_nom' está presente en el DataFrame
    if 'pais_viajo_1_nom' in results_df:
        return results_df
    else:
        # Añade la columna 'pais_viajo_1_nom' con valores 'NaN' si no está presente
        results_df['pais_viajo_1_nom'] = 'nan'
        return results_df


def formatear_datos(results_df):
    """
    Formatea y muestra el DataFrame de una manera organizada y legible.

    Recibe:
        - results_df (DataFrame): DataFrame que contiene los datos a formatear.

    Retorna:
        - None: Solo muestra los datos formateados en la consola.
    """
    # Filtra y ajusta los datos para asegurar la presencia de todas las columnas necesarias
    results_filtered = filtrar_datos(results_df)

    # Reorganiza las columnas en el orden especificado
    new_order = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado', 'pais_viajo_1_nom']
    results_filtered = results_filtered[new_order]

    # Renombra las columnas para una mejor presentación
    new_column_names = {'ciudad_municipio_nom': 'Ciudad de ubicación', 'departamento_nom': 'Departamento', 'edad': 'Edad', 'fuente_tipo_contagio': 'Tipo', 'estado': 'Estado', 'pais_viajo_1_nom': 'País de procedencia'}
    results_filtered = results_filtered.rename(columns=new_column_names)

    # Define el formato de impresión de las columnas
    new_format = "{:<5} | {:<27} | {:<20} | {:<5} | {:<15} | {:<10} | {:<20}"

    # Imprime la cabecera de la tabla con las columnas
    print("=" * 121)
    print(new_format.format("     ", "Ciudad de ubicación", "Departamento", "Edad", "Tipo", "Estado", "País de procedencia"))
    print("=" * 121)

    # Imprime cada fila del DataFrame formateada según el formato especificado
    for index, row in results_filtered.iterrows():
        print(
            new_format.format(index + 1, row['Ciudad de ubicación'], row['Departamento'], row['Edad'], row['Tipo'], row['Estado'], row['País de procedencia']))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
