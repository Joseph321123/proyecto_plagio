# document_generator.py
import os
import random

subjects = ["Estudiante", "Profesor", "Investigador", "Empresa", "Gobierno"]
verbs = ["analizó", "desarrolló", "implementó", "investigó", "presentó"]
objects = ["algoritmo", "modelo", "sistema", "solución", "proyecto"]
adjectives = ["innovador", "eficiente", "complejo", "sostenible", "tecnológico"]
adverbs = ["rápidamente", "eficazmente", "precisamente", "exitosamente"]

def generate_sentence():
    # Genera frases con estructuras variadas
    structure = random.choice([
        f"{random.choice(subjects)} {random.choice(verbs)} un {random.choice(adjectives)} {random.choice(objects)} {random.choice(adverbs)}",
        f"{random.choice(adverbs)} {random.choice(subjects)} {random.choice(verbs)} un {random.choice(objects)} {random.choice(adjectives)}",
        f"{random.choice(subjects)} {random.choice(verbs)} un {random.choice(objects)} {random.choice(adjectives)} {random.choice(adverbs)}"
    ])
    
    # Introduce variabilidad:
    words = structure.split()
    if random.random() < 0.3:
        words.pop(random.randint(0, len(words)-1))  # Elimina una palabra al azar
    return ' '.join(words)

def generate_documents(num_docs=100):
    if not os.path.exists("documentos"):
        os.makedirs("documentos")
        
    # Eliminar documentos anteriores
    for f in os.listdir("documentos"):
        os.remove(os.path.join("documentos", f))
    
    # Generar documentos con niveles de plagio aleatorios
    base_sentences = [generate_sentence() for _ in range(200)]  # Base de frases
    
    for i in range(1, num_docs+1):
        plagiarism_level = random.randint(0, 100)  # Porcentaje de plagio
        
        # Mezclar contenido original y plagiado
        if i == 1:
            # Documento base (100% original)
            sentences = random.sample(base_sentences, 100)
        else:
            # Documentos derivados
            plagiarized = random.sample(base_sentences, int(100 * (plagiarism_level / 100)))
            original = [generate_sentence() for _ in range(100 - len(plagiarized))]
            sentences = plagiarized + original
            random.shuffle(sentences)  # Mezclar para simular mejor el plagio
        
        # Guardar documento
        with open(f"documentos/documento_{i}.txt", "w", encoding='utf-8') as f:
            f.write(f"Porcentaje de plagio: {plagiarism_level}%\n")
            for sentence in sentences:
                f.write(sentence + "\n")
        
        print(f"Generado: documento_{i}.txt ({plagiarism_level}% de plagio)")