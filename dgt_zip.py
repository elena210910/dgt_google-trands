import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# 1. URL del sitio con los archivos
page_url = "https://www.dgt.es/menusecundario/dgt-en-cifras/matraba-listados/matriculaciones-automoviles-diario.html"

# 2. Carpeta para guardar los archivos descomprimidos
download_folder = r"D:\\dgt"
os.makedirs(download_folder, exist_ok=True)  # Crear la carpeta si no existe

# 3. Obtener el HTML de la página
try:
    response = requests.get(page_url)
    response.raise_for_status()  # Verificar errores HTTP
    soup = BeautifulSoup(response.content, "html.parser")  # "html.parser" especifica qué analizador utilizar para procesar el HTML.
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la página: {e}")
    exit(1)

# 4. Buscar todos los enlaces a archivos ZIP
try:
    links = soup.find_all("a", href=True)  # los enlaces estan en etiqueta <a> con el atributo href
    zip_links = [link["href"] for link in links if link["href"].endswith(".zip")]
except Exception as e:
    print(f"Error al analizar los enlaces de la página: {e}")
    exit(1)

# 5. Descargar y descomprimir los archivos
archivos_descargados = 0  # Contador de archivos descargados

#Para cada enlace a un archivo ZIP (zip_link) extrae el nombre del archivo. Crea una ruta completa donde se guardará el archivo.
for zip_link in zip_links:
    filename = zip_link.split("/")[-1] # convertimos en una lista por el carácter"/". índice [-1] selecciona el último elemento de la lista(nombre del archivo)
    file_path = os.path.join(download_folder, filename) # uñon de la ruta de carpeta y el nombre del archivo extraido en una ruta completa

    try:
        # Descargar el archivo ZIP
        print(f"Descargando {filename}...")
        with requests.get(zip_link, stream=True) as r:
            r.raise_for_status()  # Verificar errores HTTP
            with open(file_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Incrementar el contador de archivos descargados
        archivos_descargados += 1

        # Descomprimir el archivo ZIP
        print(f"Descomprimiendo {filename}...")
        with ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(download_folder)

        # Eliminar la carpeta ZIP después de descomprimir, dejamos los archivos
        os.remove(file_path)
        print(f"Eliminado {filename}.")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {filename}: {e}")
    except (OSError, IOError) as e:
        print(f"Error al guardar o descomprimir {filename}: {e}")
    except Exception as e:
        print(f"Error inesperado con {filename}: {e}")

# Imprimir el total de archivos descargados
print(f"Todos los archivos han sido descargados y descomprimidos.")
print(f"Total de archivos descargados: {archivos_descargados}.")
