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

**Duplicados y limpieza de datos:**
Identifiqué muchas filas duplicadas, y tuve que decidir si mantenerlas como representaciones válidas de ventas múltiples o eliminarlas para un análisis más limpio.

**Prefijos y datos adicionales en columnas:**
En algunas columnas, como la de localidades, nombre de marca u modelo, había prefijos alfanuméricos que necesitaban ser eliminados para obtener el nombre correcto.




***Para este proyecto, se han utilizado las siguientes bibliotecas de Python:*** 😊📚✨

✔️**pandas**
   
Para leer, procesar y analizar datos de archivos Excel y archivos de texto.
Funciones principales: read_excel, concat, groupby, value_counts, to_excel.

✔️**os**
   
Para trabajar con el sistema de archivos, buscar y procesar archivos en una carpeta.

✔️**requests**

Para realizar solicitudes HTTP y descargar archivos desde la web

✔️**BeautifulSoup**

Para analizar y extraer información de documentos HTML.

✔️**zipfile**

Para trabajar con archivos ZIP, como descomprimirlos y extraer su contenido

✔️**re**

Para procesar cadenas y eliminar prefijos o caracteres innecesarios utilizando expresiones regulares.

✔️**pytrends**

Para interactuar con la API de Google Trends y obtener datos sobre el interés de búsqueda.

✔️**plotly** (si fue utilizada para gráficos)📈
   
Para crear visualizaciones de datos interactivas.

✔️**openpyxl**
   
Para leer y escribir datos en formato Excel.

# Pasos de implementación:

- Dado que los archivos están en formato ZIP, primero los descomprimiré para extraerlos y tener acceso a ellos. 
Luego los organizaré para trabajar con ellos directamente desde mi ordenador.
[Ejemplo de Codigo Python](https://github.com/elena210910/dgt_google-trands/blob/main/dgt_zip.py)

- Ahora que los datos están disponibles, los convertimos al formato Excel, ya que trabajar con ellos en su formato original es complicado debido
a que los datos no están estructurados.
[Este código](https://github.com/elena210910/dgt_google-trands/blob/main/dgt_txt_to_exsel.py) automatiza el proceso de conversión de archivos TXT a formato Excel.
Que hace el codigo: Se crea una carpeta separada que contiene todos los archivos convertidos en formato Excel, los datos se limpian de metadatos innecesarios para garantizar su calidad,
se define la anchura de las columnas clave para estructurar correctamente la información, cada archivo TXT se convierte en un archivo Excel independiente, conservando el nombre original del archivo.

- Dado que no contamos con una gran cantidad de datos, he decidido realizar algunas modificaciones manuales en los archivos Excel. 
Estas modificaciones incluyen: 
Cambiar el formato de las fechas directamente en Excel para garantizar su correcta interpretación durante el análisis.
Aunque este cambio también se puede realizar mediante código, opté por hacerlo manualmente en esta ocasión.

  Eliminar las columnas que no son relevantes para el análisis y conservar únicamente aquellas que serán utilizadas en las etapas posteriores.

Ejemplo de resultado obtenido:

![](https://github.com/elena210910/dgt_google-trands/blob/main/foto_xlxs.PNG)


- La siguiente etapa incluye la limpieza de datos directamente a través del código en Python. El análisis también se llevará a cabo en este entorno.
Para ello, utilizaré la biblioteca **pandas**, que me permitirá crear un **DataFrame** con el que trabajaré posteriormente durante el análisis.
[Este código realiza las siguientes tareas:](https://github.com/elena210910/dgt_google-trands/blob/main/df_create.py)
Carga de datos de los archivos creados anteriormente, asigna los nombres a las columnas, limpia las columnas de texto eliminando prefijos innecesarios y espacios, normaliza las cadenas convirtiéndolas a mayúsculas, identifica las 5 marcas más populares por cantidad registrada,
encuentra los 3 modelos más vendidos de la marca TOYOTA, analiza las 3 regiones principales con más ventas para cada uno de estos modelos.

![](https://github.com/elena210910/dgt_google-trands/blob/main/table_df.PNG)


**NOTA:** No eliminé los duplicados porque podrían representar ventas legítimas registradas múltiples veces en el mismo día o en la misma ubicación. En lugar de asumir que todas las filas duplicadas son errores, preferí conservarlos para reflejar mejor la realidad de los datos originales y evitar eliminar información potencialmente válida. Esto es especialmente importante cuando no se dispone de un identificador único para cada registro.

![Ejemplo deresultado](https://github.com/elena210910/dgt_google-trands/blob/main/df_screen.PNG)




- En esta etapa analizaremos la evaluación del interés de búsqueda en **Google Trends.**✨

Google Trends asigna una puntuación que varía de 0 a 100, donde un valor más alto indica un mayor interés de búsqueda en relación con los demás términos evaluados en el mismo período.

A partir de esta evaluación, construiremos gráficos 📈 combinando los datos de nuestro DataFrame con los resultados de Google Trends. Nos centraremos en el análisis de las marcas con mayor cantidad de vehículos matriculados, como Toyota, que ocupa el primer lugar, y Renault, que ocupa el segundo. Además, incluiremos la marca KIA, que no logró posicionarse entre las Top 5 marcas de vehículos matriculados, para observar cómo se compara su interés de búsqueda con el número de matriculaciones.
[Este código](https://github.com/elena210910/dgt_google-trands/blob/main/google_data.py)utiliza Google Trends para obtener el interés de búsqueda en España de las palabras clave seleccionadas (Toyota, Renault, Kia) durante el período del 2 al 26 de diciembre de 2024, coincidiendo con los datos de matriculaciones. Es importante destacar que las letras mayúsculas o minúsculas no afectan el resultado de las búsquedas.
[Aqui tenemos un ejemplo de codigo para construir grafico interactivo](https://github.com/elena210910/dgt_google-trands/blob/main/chart.py)

😊✅✨[Definitivamente Podemos observar el resultado final](https://sparkling-conkies-21fc82.netlify.app/) ⬅️




