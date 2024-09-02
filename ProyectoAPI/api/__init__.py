import pandas as pd
from sodapy import Socrata

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Función que consulta datos de una API y los retorna en un DataFrame
Recibe: 
 - `limite_registros` (int): El número máximo de registros que se desean obtener de la API.
 - `nombre_departamento` (str): El nombre del departamento por el cual se quiere filtrar los datos.
Retorna: 
 - Un DataFrame de Pandas que contiene los datos obtenidos de la API filtrados por las columnas especificadas.
"""
def consultar_datos(limite_registros, nombre_departamento):
    # Se crea un cliente de la API utilizando la librería Socrata
    client = Socrata("www.datos.gov.co", None)

    # Se definen las columnas que se desean obtener de la API
    requested_columns = 'ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom'

    # Se realiza la consulta a la API especificando el límite de registros y el nombre del departamento
    results = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=nombre_departamento, select=requested_columns)

    # Se convierten los resultados obtenidos en un DataFrame de Pandas
    results_df = pd.DataFrame.from_records(results)

    # Se retorna el DataFrame con los datos consultados
    return results_df

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
