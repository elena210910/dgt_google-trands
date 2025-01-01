from pytrends.request import TrendReq
import pandas as pd

# Crear un objeto pytrends
pytrends = TrendReq(hl='es-ES', tz=360, timeout=(10, 25))

# Lista de palabras clave para buscar
keywords = ['Toyota', 'Renault', 'Kia']

# Cargar el interés por estas palabras clave
pytrends.build_payload(keywords, cat=0, timeframe="2024-12-02 2024-12-26", geo='ES')

# Obtener datos históricos sobre el interés
interest_data = pytrends.interest_over_time()

# Verificar los datos
if not interest_data.empty:
    # Eliminar la columna "isPartial" si existe
    if 'isPartial' in interest_data.columns:
        interest_data = interest_data.drop(columns=['isPartial'])

    # Mostrar los datos para verificación
    print(interest_data)

    # Si es necesario, guardar los datos en un archivo CSV
    interest_data.to_csv('interest_toyota_search.csv', index=True)
else:
    print("No hay datos de interés para las palabras clave especificadas.")
