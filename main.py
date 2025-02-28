# Simple Python implementation of consistent hashing
import hashlib


class ConsistentHash:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(self.replicas):
            print(f"{node}:{i}")
            key = self._hash(f"{node}:{i}")
            self.ring[key] = node
            self.sorted_keys.append(key)
        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            key = self._hash(f"{node}:{i}")
            del self.ring[key]
            self.sorted_keys.remove(key)

    def get_node(self, key):
        if not self.ring:
            return None

        hash_key = self._hash(key)

        # Find the first point in the ring at or after hash_key
        for ring_key in self.sorted_keys:
            if hash_key <= ring_key:
                return self.ring[ring_key]

        # If we've reached here, the hash_key is greater than all
        # keys in the ring, so we wrap around to the first node
        return self.ring[self.sorted_keys[0]]

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)



if __name__ == '__main__':
    consistent_hash = ConsistentHash(nodes=[2,4,7])
    print(consistent_hash.ring)
    print(consistent_hash.get_node('121392825777583946149540442118031181496'))




