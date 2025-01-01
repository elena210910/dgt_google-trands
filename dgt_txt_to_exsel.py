import os
import pandas as pd

# Ruta a la carpeta con los archivos TXT
folder_path = r"D:\dgt"
output_folder = r"D:\dgt\excel"

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Procesar cada archivo TXT en la carpeta
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        
        # Definir la anchura de las primeras columnas necesarias
        colspecs = [
            (0, 9),    # Primera columna (Fecha)
            (9, 31),   # Segunda columna (Marca)
            (31, 68),  # Tercera columna (Modelo)
            (68, 76)   # Cuarta columna (Num, utilizare como numero de identificacion)
        ]

        # Leer las columnas fijas especificadas
        df_fixed = pd.read_fwf(file_path, colspecs=colspecs, encoding="ISO-8859-1")

        # Leer el resto de las columnas automáticamente
        df_remaining = pd.read_fwf(file_path, header=None, encoding="ISO-8859-1").iloc[:, len(colspecs):]

        # Combinar los datos leídos
        df = pd.concat([df_fixed, df_remaining], axis=1)

        # Numerar las columnas
        df.columns = range(df.shape[1])

        # Ruta de salida para el archivo Excel
        output_path = os.path.join(output_folder, file_name.replace('.txt', '.xlsx'))

        # Guardar los datos en formato Excel sin encabezados
        df.to_excel(output_path, index=False, header=False)

        print(f"Archivo procesado y guardado: {output_path}")
