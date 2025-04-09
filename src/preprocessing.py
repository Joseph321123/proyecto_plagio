# src/preprocessing.py
import re
from src.hash_utils import CustomHasher
from src.bloom_filter import BloomFilter

def preprocess_documents(documents, n=2):  # Usar bigramas para mayor similitud
    processed = {}
    bloom = BloomFilter(size=1000000)
    
    for doc_name, content in documents.items():
        cleaned = re.sub(r'[^\w\s]', '', content.lower())
        tokens = cleaned.split()
        
        n_grams = {' '.join(tokens[i:i+n]) for i in range(len(tokens)-n+1)}
        hashed_grams = {hash(n_gram) for n_gram in n_grams}
        
        # Actualizar Bloom Filter
        for gram in n_grams:
            bloom.add(gram)
        
        processed[doc_name] = {
            'hashes': hashed_grams,
            'bloom': bloom
        }
    
    return processed