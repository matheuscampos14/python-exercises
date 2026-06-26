class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self, text):
        unicode = 0
        for letter in text:
            unicode += ord(letter)
        return unicode
    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value
    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            return
        elif key not in self.collection[hashed_key]:
            return
        self.collection[hashed_key].pop(key)
    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            return None
        elif key not in self.collection[hashed_key]:
            return None
        return self.collection[hashed_key][key]

teste = HashTable()
teste.add('fcc', 'coding')
#teste.add('cfc', 'chemical')
print(teste.lookup('cfc'))