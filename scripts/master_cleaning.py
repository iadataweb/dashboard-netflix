# Importa la librer�a pandas con el alias 'pd'
import pandas as pd

def cargar_datos(ruta_archivo):
    # Carga los datos desde un archivo CSV utilizando pandas
    datos = pd.read_csv(ruta_archivo)
    return datos

def renombrar_columnas(datos):
    # Renombrar las columnas del DataFrame
    datos = datos.rename(columns={
        "show_id":"mostrar_id",
        "type":"tipo",
        "title":"t�tulo",
        "cast":"elenco",
        "country":"pa�s",
        "date_added":"fecha_agregada",
        "release_year":"a�o_lanzamiento",
        "rating":"valoraci�n",
        "duration":"duraci�n",
        "listed_in":"listado_en",
        "description":"descripci�n"
    })
    return datos

def crear_detalles(datos):
    # Calcular la cantidad de valores nulos para cada columna del DataFrame 'datos'
    valores_nulos = datos.isna().sum()
    # Calcular la cantidad de valores no nulos para cada columna del DataFrame datos
    valores_aceptable = datos.notna().sum()
    # Crear un nuevo DataFrame 'detalles' con informaci�n sobre los valores nulos y no nulos
    detalles = pd.DataFrame({
        'Columna': valores_nulos.index,
        'Valores Aceptable': valores_aceptable.values,
        'Valores Nulos': valores_nulos.values
    })
    return detalles

def actualizar_detalles(datos, detalles, columna):
    # Obtener la cantidad de valores v�lidos de la columna espec�fica desde 'detalles'
    valor = detalles.loc[detalles['Columna'] == columna, 'Valores Aceptable'].values[0]
    # Calcular la cantidad de nuevos registros v�lidos que no son 'No Disponible'
    nuevos_registro = datos[(datos[columna] != 'No Disponible')].shape[0] - valor
    # Verificar si la columna 'Nuevo Registro V�lido' no existe para crear la columna
    if 'Nuevo Registro V�lido' not in detalles.columns:
        detalles['Nuevo Registro V�lido'] = 0
    # Calcular la cantidad de registros con el valor 'No Disponible'
    valor_no_disponible = datos[datos[columna] == 'No Disponible'].shape[0]
    # Verificar si la columna 'No Disponible' no existe para crear la columna
    if 'No Disponible' not in detalles.columns:
        detalles['No Disponible'] = 0
    # Actualizar la columna 'Nuevo Registro V�lido' para la columna espec�fica en 'detalles'
    detalles.loc[detalles['Columna'] == columna, 'Nuevo Registro V�lido'] = nuevos_registro
    # Actualizar la columna 'No Disponible' para la columna espec�fica en 'detalles'
    detalles.loc[detalles['Columna'] == columna, 'No Disponible'] = valor_no_disponible
    return detalles

def actualizar_nulos(datos, detalles):
    # Calcular la cantidad de valores nulos para cada columna del DataFrame 'datos'
    valores_nulos = datos.isna().sum()
    # Verificar si la columna 'Resultado Nulos' no existe para crear la columna
    if 'Resultado Nulos' not in detalles.columns:
        # Crear nueva columna 'Resultado Nulos' con ceros como valor inicial
        detalles['Resultado Nulos'] = 0
    # Actualizar la columna 'Resultado Nulos' del DataFrame 'detalles'
    for columna in valores_nulos.index:
        if columna in detalles['Columna'].values:
            # Actualizar el valor correspondiente a cada columna en DataFrame 'detalles'
            detalles.loc[detalles['Columna'] == columna, 'Resultado Nulos'] = valores_nulos[columna]
    return detalles

def mostrar_resumen(datos, tipo):
    # Obtener la cantidad de filas y columnas del DataFrame 'datos'
    resumen_tabla = datos.shape
    # Calcular cantidad total de valores nulos en todo el DataFrame
    resumen_nulos_totales = datos.isna().sum().sum()
    # Formatear el resumen inicial y final con el tama�o del DataFrame y total de valores nulos
    resumen = (
        f"{tipo}:\n"
        f"La cantidad de filas y columnas es {resumen_tabla}.\n"
        f"La cantidad total de valores nulos en todo el DataFrame es {resumen_nulos_totales}.\n\n"
    )
    return resumen

def crear_columna_combinada(datos, nueva_columna, columna1, columna2):
    # Combinar dos columnas en una nueva columna separadas por '---'
    datos[nueva_columna] = datos[columna1].astype(str) + '---' + datos[columna2].astype(str)
    return datos

def combinada_new(datos, nueva_columna, columna1, columna2):
    # Combinar dos columnas en una nueva columna separadas por '---'
    datos[nueva_columna] = datos['tipo'].astype(str) + '---' + datos[columna1].astype(str) + '---' + datos[columna2].astype(str)
    return datos

def obtener_combinaciones_frecuentes(datos, campo):
    # Agrupar el DataFrame por el campo especificado y contar la frecuencia de cada combinaci�n
    contar_frecuencia = datos.groupby(campo).size().reset_index(name='count')
    # Filtrar las combinaciones que aparecen m�s de una vez
    contar_frecuencia = contar_frecuencia[contar_frecuencia['count'] > 1]
    # Ordenar por la cantidad de frecuencia en orden descendente
    contar_frecuencia = contar_frecuencia.sort_values(by='count', ascending=False)
    return contar_frecuencia

def limpiar_coma_inicial(columna):
    if pd.notna(columna):
        return columna.strip(', ').strip()  # Quitar comas y espacios al principio y al final
    return columna

def crear_mapas(datos, valor, clave):
    # Crear una tabla de combinaciones �nicas sin registros nulos - [valor = columna1 y clave = columna2]
    tabla_unique = datos[[valor, clave]].dropna().drop_duplicates().reset_index(drop=True)
    # Crear un diccionario para mapear cada clave a su valor correspondiente
    mapa = tabla_unique.set_index(clave)[valor].to_dict()
    return mapa

def completar_registro(row, columna, clave, mapa):
    # Completar el registro si el valor es nulo
    if pd.isna(row[columna]):
        # Devuelve el valor mapeado o 'No Disponible'
        return mapa.get(row[clave], 'No Disponible')
    # Si el valor no es nulo, devuelve el valor original de la fila
    return row[columna]

def limpiar_registro(datos, columna):
    # Eliminar los registros nulo
    datos = datos.dropna(subset=[columna]).reset_index(drop=True)
    return datos

def limpiar_campo(datos, columna):
    # Eliminar campo
    datos = datos.drop(columns=[columna])
    return datos

# Ruta del archivo CSV
archivo_csv = 'netflix_titles.csv'

# Almacenar res�menes en una lista
resumen = []

# Ejecutar la funci�n para cargar la base de datos
datos = cargar_datos(archivo_csv)

# Reemplazar saltos de l�nea dentro de las celdas por un espacio
datos = datos.replace(r'\n', ' ', regex=True)

# Ejecutar la funci�n para cambiar los nombres de las columnas
datos = renombrar_columnas(datos)

# Ejecutar la funci�n para crear una tabla detalles
detalles = crear_detalles(datos)

# Ejecutar la funci�n para crear resumen
resumen.append(mostrar_resumen(datos, 'Resumen Inicial'))

# Ejecutar la funci�n para crear nueva columna combinada
datos = crear_columna_combinada(datos,'director_elenco','director','elenco')

# Ejecutar la funci�n para crear una tabla que nos permita visualizar las combinaciones frecuentes en orden descendente
combinaciones_frecuentes = obtener_combinaciones_frecuentes(datos, 'director_elenco')

# Ejecutar la funci�n para crear un diccionario que nos permite mapear clave y registrar valor al campo incompleto
mapa_director = crear_mapas(datos, 'director', 'elenco')

# Ejecutar la funci�n para crear un diccionario que nos permite mapear clave y registrar valor al campo incompleto
mapa_elenco = crear_mapas(datos, 'elenco', 'director')

# Ejecutar la funci�n para completar los registros incompletos con el diccionario mapa creado
datos['director'] = datos.apply(completar_registro, axis=1, columna='director', clave='elenco', mapa=mapa_director)

# Ejecutar la funci�n para registrar los cambios en la tabla detalles error
detalles = actualizar_detalles(datos, detalles, 'director')

# Ejecutar la funci�n para completar los registros incompletos con el diccionario mapa creado
datos['elenco'] = datos.apply(completar_registro, axis=1, columna='elenco', clave='director', mapa=mapa_elenco)

# Ejecutar la funci�n para registrar los cambios en la tabla detalles
detalles = actualizar_detalles(datos, detalles, 'elenco')

# Ejecutar la funci�n para limpiar comas y espacios al principio y al final del valor en la columna 'pa�s'
datos['pa�s'] = datos['pa�s'].apply(limpiar_coma_inicial)

# Ejecutar la funci�n para crear un diccionario que nos permite mapear clave y registrar valor al campo incompleto
mapa_pais = crear_mapas(datos, 'pa�s', 'director')

# Ejecutar la funci�n para completar los registros incompletos con el diccionario mapa creado
datos['pa�s'] = datos.apply(completar_registro, axis=1, columna='pa�s', clave='director', mapa=mapa_pais)

# Ejecutar la funci�n para registrar los cambios en la tabla detalles
detalles = actualizar_detalles(datos, detalles, 'pa�s')

# Ejecutar la funci�n para eliminar los registros nulos en un campo espec�fico
datos = limpiar_registro(datos, 'fecha_agregada')

# Ejecutar la funci�n para eliminar los registros nulos en un campo espec�fico
datos = limpiar_registro(datos, 'valoraci�n')

# Ejecutar la funci�n para eliminar los registros nulos en un campo espec�fico
datos = limpiar_registro(datos, 'duraci�n')

# Ejecutar la funci�n para crear nueva columna que nos permita visualizar los resultados nulos actual
detalles = actualizar_nulos(datos, detalles)

# Ejecutar la funci�n para eliminar columna espec�fico
datos = limpiar_campo(datos, 'descripci�n')

# Ejecutar la funci�n para eliminar columna espec�fico
datos = limpiar_campo(datos, 'director_elenco')

# Ejecutar la funci�n para crear resumen
resumen.append(mostrar_resumen(datos, 'Resumen Final'))

# Concatenar los res�menes en un solo string
resumen = "\n".join(resumen)

# Crear una columna 'pa�s_nuevo' con la primera parte de la divisi�n
datos['pa�s_nuevo'] = datos['pa�s'].str.split(',', expand=True)[0]

# Ejecutar la funci�n para eliminar columna espec�fico
datos = limpiar_campo(datos, 'pa�s')

# Cambiar el nombre de la columna
datos = datos.rename(columns={
    "pa�s_nuevo":"pa�s"
})

# Calcular la cantidad de valores nulos del todo el DataFrame
datos.isna().sum().sum()

# Ruta del archivo CSV de salida para datos limpiados
archivo_salida = 'netflix_datos_limpios.csv'

# Guardar el DataFrame 'datos' en un archivo CSV
datos.to_csv(archivo_salida, index=False, encoding='utf-8')

