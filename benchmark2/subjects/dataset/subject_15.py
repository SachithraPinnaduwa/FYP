def createHashTable(size):
    class HashTable:
        def __init__(self, size):
            self.size = size
            self.__buckets = [[] for _ in range(size)]

        def __hash(self, key):
            return hash(key) % self.size

        def insert(self, key, value):
            idx = self.__hash(key)
            self.__buckets[idx].append((key, value))

        def retrieve(self, key):
            idx = self.__hash(key)
            bucket = self.__buckets[idx]
            for k, v in bucket:
                if k == key:
                    return v
            return None  

        def delete(self, key):
            idx = self.__hash(key)
            bucket = self.__buckets[idx]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    return

    return HashTable(size)