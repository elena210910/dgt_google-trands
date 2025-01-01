import os
import pandas as pd

# Ruta de la carpeta con los archivos
folder_path = r"D:\dgt"
xlsx_file = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

dataframes = []  # la lista para guardar los q sacamos de xlsx

# Procesar cada archivo xlsx
for file in xlsx_file:
    # Obtener la ruta del archivo xlsx actual
    xlsx_path = os.path.join(folder_path, file)
    
    # Cargar el archivo xlsx en un DataFrame de pandas
    df = pd.read_excel(xlsx_path, engine='openpyxl', header=None)
    
    # Agregar el DataFrame a la lista
    dataframes.append(df)

# Combinar todos los DataFrames en uno
comb_df = pd.concat(dataframes, ignore_index=True) 

# Asignar nombres a las columnas
comb_df.columns = ['Fecha', 'Marca', 'Modelo', 'Num', 'Localidad de vehiculo', 'Fabricante']

# Limpieza de la columna "Localidad de vehiculo"
# Eliminar prefijos (una letra + dígitos al inicio de la cadena)
comb_df['Localidad de vehiculo'] = comb_df['Localidad de vehiculo'].str.replace(r'^[A-Z]\d+', '', regex=True)

# Quitar espacios adicionales al inicio de las cadenas por si existen
comb_df['Localidad de vehiculo'] = comb_df['Localidad de vehiculo'].str.strip()

# Limpieza de la columna "Marca"
comb_df['Marca'] = comb_df['Marca'].str.replace(r'^\d+', '', regex=True).str.strip()

# Limpieza de la columna "Modelo"
comb_df['Modelo'] = comb_df['Modelo'].str.strip().str.upper()

# Verificar duplicados
unique_rows = comb_df.duplicated().sum()
print(f"Número de filas duplicadas: {unique_rows}")

# Convertir la columna 'Fecha' al formato datetime para evitar posibles errores
comb_df['Fecha'] = pd.to_datetime(comb_df['Fecha'], errors='coerce')


# Obtener las 5 marcas más populares
top_brands = comb_df['Marca'].value_counts().head(5)
print("Top 5 marcas de automóviles por cantidad registrada:")
print(top_brands)

# Obtener los modelos más vendidos de TOYOTA (top 3)
toyota_top_modelos = comb_df[comb_df['Marca'] == 'TOYOTA']['Modelo'].value_counts().head(3)
print("Top 3 modelos más vendidos de TOYOTA:")
print(toyota_top_modelos)

# Limpieza de la columna "Localidad de vehiculo"
comb_df['Localidad de vehiculo'] = comb_df['Localidad de vehiculo'].str.strip().str.upper()

# Análisis de regiones para cada modelo del top 3
def analizar_regiones(marca, modelo):
    top_regiones = comb_df[
        (comb_df['Marca'] == marca) & (comb_df['Modelo'] == modelo)
    ]['Localidad de vehiculo'].value_counts().head(3)
    print(f"\nTop 3 regiones con ventas del modelo {modelo} ({marca}):")
    print(top_regiones)

for modelo in toyota_top_modelos.index:
    analizar_regiones('TOYOTA', modelo)
