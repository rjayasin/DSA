# given a list of words, reverse every word in the array
def reverse_words_list(words):
	for x in range(len(words)):
		words[x] = words[x][::-1]


# given a string reverse every word in that string
def reverse_words_string(string):
	l = string.split(" ")
	for x in range(len(l)):
		l[x] = l[x][::-1]
	return " ".join(l)


a = ["Hello", "World", "this", "is", "a", "test"]
print(a)
reverse_words_list(a)
print(a)
print(reverse_words_string("hello words this is a tests"))