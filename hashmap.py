class HashMap:
	def __init__(self, start):
		self.size = start
		self.count = 0
		self.keys = [[] for _ in range(self.size)]
		self.values = [[] for _ in range(self.size)]


	def insert(self, key, value):
		pos = hash(key) % self.size
		self.keys[pos].append(key)
		self.values[pos].append(value)
		self.count += 1


	def get(self, key):
		pos = hash(key) % self.size
		ind = self.keys[pos].index(key)
		return self.values[pos][ind]


	def contains(self, key):
		pos = hash(key) % self.size
		return key in self.keys[pos]


	def remove(self, key):
		pos = hash(key) % self.size
		self.keys[pos] = None
		self.values[pos] = None


	def resize(self):
		# not sure how to handle copying over of keys as hashed index could change
		# meaning old items could be lost

		# simply double the size with empty space
		self.keys.extend([[] for _ in range(self.size)])
		self.values.extend([[] for _ in range(self.size)])
		self.size *= 2


hmap = HashMap(3)
hmap.insert("hello", 1)
hmap.insert("hell", 2)
hmap.insert("hel", 3)
print(hmap.keys)
hmap.resize()
print(hmap.keys)
hmap.insert("hello", 1)
hmap.insert("hell", 2)
hmap.insert("hel", 3)
print(hmap.keys)