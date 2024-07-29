# Netflix Dashboard en Power BI

¡Bienvenido a mi proyecto de Dashboard de Netflix en Power BI! Este proyecto utiliza datos extraídos de Kaggle, que han sido limpiados y preparados con Python para crear un dashboard interactivo.

## Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Preparación de Datos](#preparación-de-datos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Fuentes de Datos](#fuentes-de-datos)
- [Scripts de Extracción de Datos](#scripts-de-extracción-de-datos)
- [Contribuciones](#contribuciones)
- [Contacto](#contacto)

## Descripción del Proyecto

Este proyecto ofrece un análisis detallado del contenido de Netflix, permitiendo explorar tendencias, géneros populares, lanzamientos por año, y más. Está diseñado para ayudar a los analistas de datos a obtener información valiosa del contenido de Netflix mediante un enfoque visual e interactivo. El contenido analizado abarca desde 2008 hasta 2021.

## Tecnologías Utilizadas

- **Power BI**: Para la creación de dashboards y visualizaciones interactivas.
- **Python**: Para la limpieza y preparación de los datos.
- **Kaggle**: Fuente de los datos utilizados en el proyecto.

## Preparación de Datos

El proceso de limpieza y preparación de los datos incluyó:

- Renombrar las columnas a español.
- Reemplazar saltos de línea dentro de las celdas por un espacio.
- Completar los registros de la columna `director` basándose en su relación con la columna `elenco`.
- Completar los registros de la columna `país` basándose en su relación con la columna `director`.
- Eliminar registros nulos en las columnas `fecha_agregada`, `valoración` y `duración`.
- Eliminar la columna `descripción` ya que no es necesaria para el análisis.
- Exportar los datos completamente limpios a un archivo CSV para su uso en Power BI.

## Instalación

Para ejecutar este proyecto localmente, sigue los siguientes pasos:

1. Clona este repositorio:
   
   ```bash
   git clone https://github.com/injantedataweb/netflix-dashboard.git
   
## Uso

Explora el dashboard para obtener información sobre:
- Tipos de contenido.
- Títulos, elenco y países asociados.
- Géneros y lanzamientos por año.
- Valoraciones y fechas de agregado del contenido.

## Fuentes de Datos

Este proyecto utiliza datos extraídos de la [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows), específicamente del conjunto de datos Netflix Movies and TV Shows.

## Scripts de Extracción de Datos

- **master_cleaning.py**: Este script se encarga de limpiar y generar un archivo nuevo sin modificar el datos original. La preparación incluye el renombrado de columnas, reemplazo de saltos de línea y eliminación de registros nulos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, siéntete libre de abrir un issue o un pull request en este repositorio.

## Contacto

- **LinkedIn:** [Carlos Injante](https://www.linkedin.com/in/20ismael1999/)

¡Gracias por visitar mi proyecto!
