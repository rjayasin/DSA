# given a list of words, reverse every word in the array

def reverse_words(words):
	for x in range(len(words)):
		words[x] = words[x][::-1]


a = ["Hello", "World", "this", "is", "a", "test"]
print(a)
reverse_words(a)
print(a)