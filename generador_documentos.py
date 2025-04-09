# Importamos las librerías necesarias
import os  # Para interactuar con el sistema de archivos
import random  # Para generar números aleatorios
import string  # Para generar cadenas de caracteres aleatorios (en este caso, letras)

# =============================
# Función para generar un documento con un porcentaje de plagio
# =============================
def generar_documento(plagio_porcentaje, base_texto):
    # Copiamos la lista de palabras base para evitar modificar la lista original
    palabras = base_texto.copy()
    total_palabras = len(palabras)  # Número total de palabras en el texto base
    # Calculamos cuántas palabras deben ser reemplazadas para alcanzar el porcentaje de plagio
    reemplazar = int(total_palabras * (100 - plagio_porcentaje) / 100)
    
    # Generamos una lista de índices aleatorios para las palabras que vamos a reemplazar
    indices = random.sample(range(total_palabras), reemplazar)
    
    # Reemplazamos las palabras seleccionadas con cadenas aleatorias de 5 letras
    for idx in indices:
        palabras[idx] = ''.join(random.choices(string.ascii_lowercase, k=5))
    
    # Devolvemos el texto generado, uniendo las palabras en una cadena separada por espacios
    return ' '.join(palabras)

# =============================
# Función para generar todos los documentos con cantidades aleatorias
# =============================
def generar_documentos():
    # Lista de niveles de plagio que queremos generar (0%, 10%, 20%, 40%, 60%, 80%, 100%)
    niveles_plagio = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # Total de documentos a generar
    total_archivos = 150
    
    # Generamos una lista con números aleatorios entre 1 y un valor máximo para cada nivel (el total se ajustará al final)
    cantidades = [random.randint(1, total_archivos // len(niveles_plagio)) for _ in range(len(niveles_plagio))]

    # Ajustamos la suma de las cantidades a 150, redistribuyendo el sobrante
    sobrante = total_archivos - sum(cantidades)
    
    # Distribuir el sobrante aleatoriamente entre las cantidades ya generadas
    while sobrante != 0:
        for i in range(len(cantidades)):
            if sobrante > 0:
                cantidades[i] += 1
                sobrante -= 1
            elif sobrante < 0:
                if cantidades[i] > 1:  # Evitamos que un nivel de plagio tenga 0 archivos
                    cantidades[i] -= 1
                    sobrante += 1

    # Texto base con 200 palabras (se repite la frase 'Lorem ipsum' para crear un texto largo)
    base_texto = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua".split() * 20  # 200 palabras
    
    # Creamos el directorio 'documentos' si no existe
    os.makedirs('documentos', exist_ok=True)
    
    contador = 1  # Inicializamos un contador para numerar los documentos generados
    
    # Iteramos sobre los niveles de plagio y las cantidades aleatorias generadas para cada nivel
    for nivel, cantidad in zip(niveles_plagio, cantidades):
        # Generamos la cantidad de documentos correspondiente a cada nivel de plagio
        for _ in range(cantidad):
            # Generamos el contenido del documento con el nivel de plagio y el texto base
            contenido = generar_documento(nivel, base_texto.copy())
            # Generamos el nombre del archivo para cada documento
            nombre = f"doc_{nivel}%_{contador:03d}.txt"
            
            # Guardamos el documento en el directorio 'documentos'
            with open(f"documentos/{nombre}", "w") as f:
                f.write(contenido)
            
            contador += 1  # Incrementamos el contador para el siguiente documento
            # Imprimimos un mensaje indicando que el documento ha sido generado
            print(f"Generado: {nombre} ({nivel}%)")

# =============================
# Punto de entrada principal
# =============================
if __name__ == "__main__":
    generar_documentos()  # Llamamos a la función principal para generar los documentos
