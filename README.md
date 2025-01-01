# Descripción del proyecto
## Análisis de las matriculaciones de vehículos y su correlación con Google Trends
Este proyecto tiene como objetivo analizar los datos de las matriculaciones diarias de vehículos 
([Microdatos de Matriculaciones de Vehículos (diarios)de DGT](https://www.dgt.es/menusecundario/dgt-en-cifras/dgt-en-cifras-resultados/dgt-en-cifras-detalle/Microdatos-de-Matriculaciones-de-Vehiculos-diarios/), que incluyen información sobre los vehículos que se incorporan al Registro de Vehículos junto con sus características técnicas. Parece razonable asumir que estos datos reflejan vehículos nuevos, ya que se basan en las primeras matriculaciones que se realizan en el Registro de Vehículos. Sin embargo, sería ideal confirmarlo revisando la fuente oficial o la documentación de donde provienen estos datos. En este caso, utilizo los datos disponibles como referencia para el análisis.🚗🚙
El propósito principal es evaluar si existe una correlación entre las matriculaciones de vehículos (ventas de automóviles) y los datos de interés de búsqueda en 🔍 **Google Trends.**

## Sobre los datos obtenidos
Nos proporcionan archivos en formato .txt correspondientes a los días desde el **2 de diciembre hasta el 26 de diciembre**, incluyendo todos los días excepto los fines de semana. Esto es lógico, ya que la DGT no opera durante los fines de semana.

Un ejemplo de la estructura del archivo.

![](https://github.com/user-attachments/assets/f7bb77cf-70b9-450e-9c54-514f435b98b2)


Al iniciar el análisis de los archivos con Python, me encontré con varias dificultades que tuve que resolver paso a paso:

**Columnas de diferentes tamaños y formatos:**
Los archivos .txt no tenían encabezados y la distribución de las columnas variaba significativamente entre algunos días.
Fue necesario calcular manualmente la anchura de las columnas para estructurar correctamente los datos.

**Formato de fechas:**
Las fechas estaban en un formato que dificultaba su procesamiento. Fue necesario normalizarlas para que fueran reconocidas correctamente por Python como objetos de tipo datetime.
📚
**Duplicados y limpieza de datos:**
Identifiqué muchas filas duplicadas, y tuve que decidir si mantenerlas como representaciones válidas de ventas múltiples o eliminarlas para un análisis más limpio.

**Prefijos y datos adicionales en columnas:**
En algunas columnas, como la de localidades, nombre de marca u modelo, había prefijos alfanuméricos que necesitaban ser eliminados para obtener el nombre correcto.

***Para este proyecto, se han utilizado las siguientes bibliotecas de Python:***😊📚✨

✔️**pandas**
   
Para leer, procesar y analizar datos de archivos Excel y archivos de texto.
Funciones principales: read_excel, concat, groupby, value_counts, to_excel.

✔️**os**
   
Para trabajar con el sistema de archivos, buscar y procesar archivos en una carpeta.

✔️**re**

Para procesar cadenas y eliminar prefijos o caracteres innecesarios utilizando expresiones regulares.

✔️**pytrends**

Para interactuar con la API de Google Trends y obtener datos sobre el interés de búsqueda.

✔️**plotly** (si fue utilizada para gráficos)📈
   
Para crear visualizaciones de datos interactivas.

✔️**openpyxl**
   
Para leer y escribir datos en formato Excel.



