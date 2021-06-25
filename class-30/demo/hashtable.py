from codefellows.dsa.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self._buckets = [None] * size

    def add(self, key, value):
        index = self.hash(key)
        if not self._buckets[index]:
            self._buckets[index] = LinkedList()

        self._buckets[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]

        if not bucket:
            return None

        current = bucket.head

        while current:
            if current.value[0] == key:
                return current.value[1]

        return None

    def contains(self, key):
        # TODO
        pass

    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        sum *= 599

        index = sum % len(self._buckets)

        return index
