class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash(self, key):
        return key % 11

    def rehash(self, old_hash):
        return (old_hash + 1) % 11

    def __setitem__(self, key, value):
        ind = self.hash(key)
        print(ind)
        if self.data[ind] is None:
            self.slots[ind] = key
            self.data[ind] = value
        else:
            count = 0
            while count < self.size:
                count += 1
                ind = self.rehash(ind)
                if self.data[ind] is None:
                    self.slots[ind] = key
                    self.data[ind] = value
                    break

    def __getitem__(self, key):
        ind = self.hash(key)
        print(ind)
        if self.slots[ind] == key:
            return self.data[ind]
        else:
            while True:
                ind = self.rehash(ind)
                if self.slots[ind] == key:
                    return self.data[ind]

    def __delitem__(self, key):
        ind = self.hash(key)
        if self.slots[ind] == key:
            self.slots[ind] = None
            self.data[ind] = None
        else:
            count = 0
            while count < self.size:
                count += 1
                ind = self.rehash(ind)
                if self.slots[ind] == key:
                    self.slots[ind] = None
                    self.data[ind] = None
                    return True
            raise KeyError

    def __len__(self):
        return self.size

    def __contains__(self, key):
        ind = hash(key)
        return self.data[ind] is not None

    def __str__(self):
        return '[' + ', '.join([str(i) if i else '__' for i in self.data]) + ']'
