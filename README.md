# Proyecto de Detección de Plagio
# Nombre de los integrantes
Jhonatan Alejandro Keeb Baak  
Pedro Joel Diaz Lopez  
Joseph Jesus Aguilar Rodriguez  

# Descripción general del proyecto

Este proyecto permite detectar similitudes entre documentos de texto, simulando y analizando casos de plagio mediante el uso de **n-gramas**, **funciones hash personalizadas** y **visualización de grafos**.  
Su objetivo principal es mostrar de forma clara cuándo dos documentos son similares, y visualizar esas relaciones para facilitar la detección de plagios potenciales. El enfoque se basa en procesamiento de texto y análisis estructurado de datos.

# Instrucciones de instalación y ejecución
 
# Tecnologías utilizadas
Python 3.13
NetworkX
Matplotlib
Manejo de archivos y textos
Función hash 

# Requisitos
Python 3.13
pip

# Instalación de dependencias
bash
pip install networkx matplotlib

### Ejecución del proyecto
bash
cd src
python main.py
(Esto generará los documentos simulados, realizará el análisis de similitud y mostrará una visualización en forma de grafo.)

# Ejemplo de uso
1. El archivo `generador_documentos.py` crea varias copias de un texto base con diferentes niveles de plagio simulados.
2. Luego, `detector_plagio.py` analiza la similitud entre los textos utilizando **n-gramas** y **hashing**.
3. Finalmente, se genera un grafo en el que los nodos representan documentos y los bordes muestran similitudes mayores a un umbral definido.

# Código comentado y organizado en módulos reutilizables

La estructura del proyecto permite modificar fácilmente cada componente:

PROYECTO_PLAGIO/
├── documentos/             # Documentos base y generados
├── resultados/             # Resultados del análisis (ej. imagen del grafo)
├── src/                    # Código fuente
│   ├── main.py             # Script principal
│   ├── generador_documentos.py  # Genera textos con plagio
│   └── detector_plagio.py  # Analiza y compara documentos
└── README.md

Cada script está documentado con comentarios que explican su propósito y funcionamiento, permitiendo su reutilización y extensión.

# Visualizaciones de los resultados

El proyecto genera un **grafo de similitud** con `NetworkX` y `Matplotlib`.  
Cada nodo representa un documento.
Las conexiones indican que hay similitud significativa.
La cercanía o densidad de conexiones facilita la detección de documentos sospechosos.

Ejemplo:  
resultados/similitud_grafo.png
