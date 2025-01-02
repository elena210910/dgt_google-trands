import os
import pandas as pd

# Ruta de la carpeta con los archivos
folder_path = r"D:\dgt"
xlsx_file = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]


dataframes = []

# Leer cada archivo xlsx
for file in xlsx_file:
    # Ruta del archivo xlsx actual
    xlsx_path = os.path.join(folder_path, file)
    
    # Leer el archivo xlsx en un DataFrame de pandas
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

# Quitar espacios adicionales al inicio de las cadenas
comb_df['Localidad de vehiculo'] = comb_df['Localidad de vehiculo'].str.strip()

# Limpieza de la columna "Marca"
comb_df['Marca'] = comb_df['Marca'].str.replace(r'^\d+', '', regex=True).str.strip()

# Limpieza de la columna "Modelo"
comb_df['Modelo'] = comb_df['Modelo'].str.strip().str.upper()

# Verificar duplicados
unique_rows = comb_df.duplicated().sum()
print(f"Número de filas duplicadas: {unique_rows}")
comb_df = comb_df.drop_duplicates()
unique_rows_after = comb_df.duplicated().sum()
print(f"Número de filas duplicadas después de eliminar: {unique_rows_after}")

# Convertir la columna 'Fecha' al formato datetime
comb_df['Fecha'] = pd.to_datetime(comb_df['Fecha'], errors='coerce')

# Obtener las 10 marcas más vendidas
top_brands = comb_df['Marca'].value_counts().head(10)

# Crear una lista para almacenar los resultados
results = []

# Analizar cada marca del top 10
for marca in top_brands.index:
    # Obtener los 3 modelos más vendidos para la marca
    top_modelos = comb_df[comb_df['Marca'] == marca]['Modelo'].value_counts().head(3)

    for modelo, cantidad_modelo in top_modelos.items():
        # Obtener la localidad con más ventas para el modelo
        top_localidad = comb_df[
            (comb_df['Marca'] == marca) & (comb_df['Modelo'] == modelo)
        ]['Localidad de vehiculo'].value_counts().head(1)

        localidad = top_localidad.index[0] if not top_localidad.empty else 'N/A'
        cantidad_localidad = top_localidad.iloc[0] if not top_localidad.empty else 0

        # Agregar los datos a la lista de resultados
        results.append({
            'Top-Marca': marca,
            'Cantidad Marca': top_brands[marca],
            'Top-Modelo': modelo,
            'Cantidad Modelo': cantidad_modelo,
            'Localidad': localidad,
            'Cantidad Localidad': cantidad_localidad
        })

# Crear un DataFrame con los resultados
results_df = pd.DataFrame(results)

# Guardar los resultados en un archivo Excel
output_path = r"D:\dgt\top_ventas_unique.xlsx"
results_df.to_excel(output_path, index=False)
print(f"Resultados guardados en: {output_path}")
