import os
import time
from src.preprocessing import preprocess_documents
from src.similarity import calculate_jaccard_similarity
from src.sorting import merge_sort
from src.visualization import generate_similarity_graph
from document_generator import generate_documents

def main():
    start_time = time.time()
    
    # Paso 1: Generar documentos sintéticos
    print("Generando 100 documentos...")
    generate_documents(num_docs=100)
    
    # Paso 2: Cargar documentos (con manejo de codificación)
    docs_dir = 'documentos'
    documents = {}
    try:
        for filename in os.listdir(docs_dir):
            with open(os.path.join(docs_dir, filename), 'r', 
                    encoding='utf-8', 
                    errors='replace') as f:  # Ignorar bytes inválidos
                documents[filename] = f.read().strip()  # Eliminar espacios extras
    except Exception as e:
        print(f"Error al cargar documentos: {e}")
        return
    
    # Paso 3: Preprocesamiento con hashing y Bloom Filters
    print("\nPreprocesando documentos...")
    processed_docs = preprocess_documents(documents, n=3)
    
    # Paso 4: Mostrar información de hashes y Bloom Filters
    print("\n=== HASHES Y BLOOM FILTERS ===")
    for doc_name, data in processed_docs.items():
        print(f"\nDocumento: {doc_name}")
        print(f"Cantidad de hashes: {len(data['hashes'])}")
        print(f"Bits activos en Bloom Filter: {sum(data['bloom'].bit_array)}")  # Conteo de bits True
    
    # Paso 5: Calcular similitudes entre todos los pares
    print("\nCalculando similitudes...")
    similarities = []
    for doc1 in processed_docs:
        for doc2 in processed_docs:
            if doc1 < doc2:  # Evitar duplicados
                sim = calculate_jaccard_similarity(
                    processed_docs[doc1]['hashes'],
                    processed_docs[doc2]['hashes']
                )
                similarities.append((doc1, doc2, sim))
    
    # Paso 6: Ordenar con Merge Sort personalizado
    print("\nOrdenando resultados...")
    sorted_sims = merge_sort(similarities, key=lambda x: -x[2])
    
    # Paso 7: Mostrar top 5
    print("\nTop 5 pares más similares:")
    for pair in sorted_sims[:5]:
        print(f"- {pair[0]} y {pair[1]}: {pair[2]:.2f}")
    
    # Paso 8: Generar visualización
    print("\nGenerando gráfico de similitudes...")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    sorted_sims = merge_sort(similarities, key=lambda x: -x[2])
    generate_similarity_graph(sorted_sims, filename=f"similitudes_{timestamp}.png")
    
    print(f"\nTiempo total: {time.time() - start_time:.2f} segundos")

if __name__ == "__main__":
    main()