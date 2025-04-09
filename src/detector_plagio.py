# Importamos las librerías necesarias
import os  # Para interactuar con el sistema de archivos
import re  # Para trabajar con expresiones regulares

# =============================
# Clase CustomHash
# =============================
class CustomHash:
    # El constructor toma una semilla para el cálculo del hash
    def __init__(self, seed):
        self.seed = seed  # Guardamos la semilla en el objeto

    # Método __call__ hace que podamos usar una instancia de la clase como una función
    def __call__(self, value):
        # Calculamos el hash de la semilla y el valor (en este caso, lo convertimos a cadena)
        # y luego tomamos el valor módulo 2^32 para obtener un valor de hash más pequeño
        return hash(str(self.seed) + value) % (2**32)

# =============================
# Clase BloomFilter
# =============================
class BloomFilter:
    # El constructor inicializa el filtro de Bloom con un tamaño y las funciones de hash
    def __init__(self, size, hash_functions):
        self.size = size  # Tamaño del arreglo de bits
        self.hash_functions = hash_functions  # Lista de funciones hash a usar
        self.bit_array = [0] * size  # Inicializamos el arreglo de bits con ceros

    # Método para agregar un ítem al filtro de Bloom
    def add(self, item):
        for hf in self.hash_functions:  # Para cada función de hash
            # Calculamos el índice del bit que se debe poner a 1
            idx = hf(item) % self.size
            self.bit_array[idx] = 1  # Marcamos el bit correspondiente a 1

    # Método para comprobar si un ítem está en el filtro de Bloom
    def __contains__(self, item):
        # Verificamos que todas las posiciones de los bits correspondientes a los hash estén a 1
        return all(
            self.bit_array[hf(item) % self.size] 
            for hf in self.hash_functions
        )

# =============================
# Función para cargar los documentos desde un directorio
# =============================
def load_documents(directory):
    documents = []  # Lista para almacenar los documentos cargados
    # Iteramos sobre todos los archivos en el directorio
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Solo consideramos archivos .txt
            # Abrimos y leemos el archivo
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                # Añadimos el nombre del archivo y su contenido a la lista de documentos
                documents.append((filename, f.read()))
    return documents  # Devolvemos la lista de documentos

# =============================
# Función para preprocesar el texto y generar n-gramas
# =============================
def preprocess(text, n=3):
    # Convertimos todo el texto a minúsculas
    text = text.lower()
    # Eliminamos los signos de puntuación con una expresión regular
    text = re.sub(r'[^\w\s]', '', text)
    # Convertimos el texto a una lista de palabras
    words = text.split()
    # Si el texto tiene suficientes palabras para generar n-gramas
    return {
        ' '.join(words[i:i+n])  # Generamos n-gramas (combinaciones de n palabras consecutivas)
        for i in range(len(words)-n+1)
    } if len(words) >= n else set()  # Si no, devolvemos un conjunto vacío

# =============================
# Función para calcular la similitud de Jaccard entre dos conjuntos
# =============================
def jaccard_similarity(set_a, set_b):
    # Calculamos la intersección de los conjuntos
    intersection = len(set_a & set_b)
    # Calculamos la unión de los conjuntos
    union = len(set_a | set_b)
    # Si la unión no es 0 (para evitar división por cero), devolvemos la similitud
    return intersection / union if union != 0 else 0.0

# =============================
# Función para comparar dos documentos
# =============================
def compare_documents(doc1, doc2):
    # Si algún n-grama de doc1 está presente en el filtro Bloom de doc2
    if any(ng in doc2['bloom'] for ng in doc1['ngrams']):
        # Calculamos la similitud de Jaccard entre los n-gramas de ambos documentos
        return jaccard_similarity(doc1['ngrams'], doc2['ngrams'])
    return 0.0  # Si no hay intersección, devolvemos similitud 0

# =============================
# Función de ordenación merge_sort
# =============================
def merge_sort(arr):
    # Si la lista tiene un solo elemento o está vacía, ya está ordenada
    if len(arr) <= 1:
        return arr
    # Encontramos el punto medio de la lista
    mid = len(arr) // 2
    # Recursivamente ordenamos las dos mitades
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Combinamos las dos mitades ordenadas
    return merge(left, right)

# =============================
# Función para combinar dos listas ordenadas
# =============================
def merge(left, right):
    result = []  # Lista para almacenar el resultado final
    i = j = 0  # Índices para recorrer las dos listas
    while i < len(left) and j < len(right):
        # Si el segundo valor de la tupla en la lista 'left' (similitud) es mayor, lo añadimos a 'result'
        if left[i][1] > right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Añadimos el resto de los elementos de 'left' o 'right' que no han sido añadidos
    result.extend(left[i:] + right[j:])
    return result  # Devolvemos la lista combinada y ordenada
