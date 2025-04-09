# src/bloom_filter.py
import mmh3

class BloomFilter:
    def __init__(self, size=1000000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size

    def add(self, item):
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = True

    def check(self, item):
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            if not self.bit_array[index]:
                return False
        return True

    def update(self, items):
        for item in items:
            self.add(item)