def string_hash(s):
    return sum(ord(c) for c in s)

class StringHashDict:
    def __init__(self):
        self.data = {}

    def add(self, key):
        self.data[key] = string_hash(key)

    def search(self, key):
        return self.data.get(key, None)

d = StringHashDict()
d.add("orange")
d.add("banana")
d.add("cherry")

print(d.search("banana"))
print(d.search("orange"))

