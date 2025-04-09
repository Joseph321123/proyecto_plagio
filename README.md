# Detector de Plagio para Trabajos Estudiantiles

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/Licencia-MIT-green)

Sistema de detección de plagio que utiliza **n-gramas**, **tablas hash**, **Bloom Filters** y **Merge Sort** para identificar similitudes entre documentos.

---

## Características Principales
✅ **Generación automática** de 100+ documentos sintéticos con frases coherentes.  
✅ **Tokenización** en tri-gramas para análisis contextual.  
✅ **Hashing personalizado** para almacenamiento eficiente de n-gramas.  
✅ **Bloom Filters** para reducir consumo de memoria.  
✅ **Similitud de Jaccard** para comparar documentos.  
✅ **Merge Sort** para clasificar resultados.  
✅ **Visualización** de redes de similitud con grafos.  

---

## Estructura del Proyecto
detector-plagio/
├── documentos/          # Documentos generados automáticamente
├── resultados/          # Grafos y reportes generados
├── src/                 # Código fuente
│   ├── bloom_filter.py  # Implementación de Bloom Filter
│   ├── hash_utils.py    # Función hash personalizada
│   ├── preprocessing.py # Limpieza y tokenización
│   ├── similarity.py    # Cálculo de similitud
│   ├── sorting.py       # Merge Sort personalizado
│   └── visualization.py # Generación de grafos
├── document_generator.py # Generador de documentos sintéticos
├── main.py              # Punto de entrada
├── requirements.txt     # Dependencias
└── README.md            # Este archivo

---

## Requisitos
- Python 3.8+
- Dependencias: `matplotlib`, `networkx`, `mmh3`

---

## Instalación
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/detector-plagio.git
cd detector-plagio

# Instalar dependencias
pip install -r requirements.txt