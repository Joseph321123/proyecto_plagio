# src/hash_utils.py
class CustomHasher:
    def __init__(self, size=1000000):
        self.size = size
        
    def hash(self, n_gram):
        # Combinación de suma de ASCII y rotación de bits
        hash_val = 0
        for i, c in enumerate(n_gram):
            hash_val += (ord(c) << (i % 4 * 8))  # Rotación de bits
        return hash_val % self.size