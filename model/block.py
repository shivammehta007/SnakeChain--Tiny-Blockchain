#!/usr/bin/env python
import hashlib as hasher


class Block:
    def __init__(self, index=None, timestamp=None, data=None, previous_hash=None):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def generate_hash(self):
        hash = hasher.sha256()
        hash.update(str(self.index).encode() +
                    str(self.timestamp).encode() +
                    str(self.data).encode() +
                    str(self.previous_hash).encode())
        return hash.hexdigest()



