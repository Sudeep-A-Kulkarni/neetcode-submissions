class MyHashSet:

    def __init__(self):
        self.size = 769          # prime number reduces collisions
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)

        for num in self.buckets[idx]:
            if num == key:
                return

        self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                return

    def contains(self, key: int) -> bool:
        idx = self._hash(key)

        for num in self.buckets[idx]:
            if num == key:
                return True

        return False