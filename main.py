# Importamos las librerías necesarias
from generador_documentos import generar_documentos  # Función para generar los documentos (no se especifica en el código proporcionado)
import os  # Para interactuar con el sistema de archivos
import re  # Para trabajar con expresiones regulares
import itertools  # Para generar combinaciones de elementos
import networkx as nx  # Para trabajar con grafos
import matplotlib.pyplot as plt  # Para graficar los datos (en este caso, un grafo)
from datetime import datetime  # Para obtener la fecha y hora actuales

# =============================
# Función hash personalizada
# =============================
def custom_hash(ngram):
    # Definimos parámetros para el cálculo del hash
    base = 257  # Base para el cálculo (número primo)
    mod = 1000000007  # Módulo grande para evitar overflow
    h = 0  # Valor inicial del hash
    # Recorrer cada carácter del n-grama y calcular su valor hash
    for c in ngram:
        h = (h * base + ord(c)) % mod  # Fórmula para el cálculo del hash
    return h  # Devolvemos el valor del hash del n-grama

# =============================
# Tokenización y n-gramas
# =============================
def limpiar_texto(texto):
    # Limpiamos el texto, convirtiéndolo a minúsculas
    texto = texto.lower()
    # Eliminar caracteres no alfabéticos ni espacios
    texto = re.sub(r"[^a-záéíóúüñ\s]", "", texto)
    return texto  # Devolvemos el texto limpio

# =============================
# Tokenización y n-gramas
# =============================
def obtener_ngrams(texto, n=2):
    # Dividimos el texto en palabras
    palabras = texto.split()
    # Generamos los n-gramas (combinaciones de n palabras consecutivas)
    ngrams = [" ".join(palabras[i:i+n]) for i in range(len(palabras)-n+1)]
    
    # Creamos un diccionario para almacenar los n-gramas y sus valores hash
    hash_table = {}
    
    # Calculamos el hash para cada n-grama y lo almacenamos en el diccionario
    for ng in ngrams:
        hash_value = custom_hash(ng)  # Calculamos el hash del n-grama
        hash_table[ng] = hash_value  # Guardamos el n-grama y su valor hash
    
    # Imprimimos la tabla hash (n-grama -> hash)
    print("\nTabla Hash de n-gramas:")
    for ng, hash_value in hash_table.items():
        print(f"{ng} -> {hash_value}")
    
    # Devolvemos solo los valores hash como conjunto (para evitar duplicados)
    return set(hash_table.values())


# =============================
# Cálculo de Similitud Jaccard
# =============================
def similitud_jaccard(ngrams_a, ngrams_b):
    # Calculamos la intersección entre los dos conjuntos de n-gramas
    interseccion = ngrams_a & ngrams_b
    # Calculamos la unión entre los dos conjuntos de n-gramas
    union = ngrams_a | ngrams_b
    # Si no hay elementos en la unión, devolvemos una similitud de 0 (no hay similitud)
    if not union:
        return 0.0
    # La similitud de Jaccard es el tamaño de la intersección dividido entre el tamaño de la unión
    return len(interseccion) / len(union)

def clasificar_porcentaje(p):
    # Esta función toma un valor de similitud (p) y devuelve una clasificación en forma de emoji
    if p == 1.0:
        return "🟢 100%"  # 100% de similitud
    elif p >= 0.8:
        return "🟢 80–99%"  # 80-99% de similitud
    elif p >= 0.6:
        return "🟡 60–79%"  # 60-79% de similitud
    elif p >= 0.4:
        return "🟠 40–59%"  # 40-59% de similitud
    elif p >= 0.2:
        return "🔴 20–39%"  # 20-39% de similitud
    elif p >= 0.1:
        return "🔴 10–19%"  # 10-19% de similitud
    else:
        return "⚫ 0–9%"  # 0-9% de similitud

# =============================
# Merge Sort personalizado
# =============================
def merge_sort(lista):
    # Si la lista tiene un solo elemento o está vacía, ya está ordenada
    if len(lista) <= 1:
        return lista
    # Dividimos la lista en dos mitades
    medio = len(lista) // 2
    # Recursivamente ordenamos las dos mitades
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    # Combinamos las dos mitades ordenadas
    return merge(izq, der)

def merge(izq, der):
    # Función para combinar dos listas ordenadas
    resultado = []
    while izq and der:
        # Comparamos el tercer elemento de cada tupla (que es la similitud) y añadimos el de mayor similitud
        if izq[0][2] > der[0][2]:
            resultado.append(izq.pop(0))  # Añadimos el primero de la lista izquierda
        else:
            resultado.append(der.pop(0))  # Añadimos el primero de la lista derecha
    # Añadimos el resto de los elementos (si los hay) de la lista izquierda o derecha
    resultado.extend(izq if izq else der)
    return resultado  # Devolvemos la lista combinada y ordenada

# =============================
# Visualización con grafos
# =============================
def visualizar_grafo(similitudes):
    # Creamos un grafo vacío
    G = nx.Graph()
    for doc1, doc2, score in similitudes:
        if score > 0:  # Solo añadimos aristas si la similitud es mayor que 0
            label = f"{round(score * 100)}%"  # Etiqueta con el porcentaje de similitud
            # Añadimos una arista entre los documentos con el peso de la similitud
            G.add_edge(doc1, doc2, weight=score, label=label)

    # Usamos el layout de resorte para posicionar los nodos
    pos = nx.spring_layout(G, seed=42)
    # Extraemos las etiquetas de las aristas
    edge_labels = nx.get_edge_attributes(G, 'label')

    # Dibujamos el grafo con las etiquetas y configuraciones de apariencia
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Similitud entre documentos")  # Título de la gráfica

    # Creamos un directorio 'resultados' si no existe
    os.makedirs("resultados", exist_ok=True)
    # Generamos un nombre único para el archivo de la imagen basándonos en la fecha y hora actual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"resultados/grafo_{timestamp}.png"
    # Guardamos la imagen en el directorio 'resultados'
    plt.savefig(nombre_archivo)
    print(f"\nGrafo guardado como: {nombre_archivo}")  # Imprimimos el nombre del archivo guardado
    plt.show()  # Mostramos el grafo
    plt.close()  # Cerramos la figura

# =============================
# Función principal
# =============================
def main():
    generar_documentos()

    carpeta = "documentos"
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".txt")]
    documentos = {}

    for archivo in archivos:
        with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
            texto = f.read()
            limpio = limpiar_texto(texto)
            
            # Obtener los n-gramas y mostrar la tabla hash
            ngrams = obtener_ngrams(limpio)
            documentos[archivo] = ngrams

    comparaciones = []
    
    # Crear un diccionario para almacenar las comparaciones por nivel de plagio
    documentos_por_plagio = {nivel: [] for nivel in range(0, 101, 10)}  # Claves: 0, 10, 20, ..., 100

    # Comparar los documentos
    for doc1, doc2 in itertools.combinations(documentos.keys(), 2):
        # Extraemos el nivel de plagio del nombre del archivo
        nivel_plagio_1 = int(doc1.split("_")[1].replace("%", ""))
        nivel_plagio_2 = int(doc2.split("_")[1].replace("%", ""))
        
        # Calcular la similitud entre los documentos
        sim = similitud_jaccard(documentos[doc1], documentos[doc2])
        comparaciones.append((doc1, doc2, sim))
        
        # Agrupar las comparaciones por nivel de plagio
        documentos_por_plagio[nivel_plagio_1].append((doc1, doc2, sim))
        documentos_por_plagio[nivel_plagio_2].append((doc1, doc2, sim))

    # Mostrar las comparaciones para cada nivel de plagio específico (10%, 20%, 30%, ...)
    for nivel in range(10, 101, 10):  # Comienza en 10 y termina en 100
        comparaciones_ordenadas = merge_sort(documentos_por_plagio[nivel])  # Ordena las comparaciones

        print(f"\nTop 10 documentos más similares para el {nivel}% de plagio:\n")
        
        # Muestra las 10 comparaciones más similares para el nivel deseado
        for doc1, doc2, sim in comparaciones_ordenadas[:10]:
            clasificacion = clasificar_porcentaje(sim)
            print(f"{doc1} <-> {doc2} | Similitud: {sim:.2%} | {clasificacion}")
        
        # Mostrar el grafo de los 10 documentos más similares de este nivel
        visualizar_grafo(comparaciones_ordenadas[:10])

# Aseguramos que la función main se ejecute solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
