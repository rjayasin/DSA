# build curr word string char by char
# if the curr word is in dict, add to some kind of list
# continue with rest of string
# if reached end of string and curr word is not a string
# then that is not a valid interpretation, return false
# backtrack :::

# words = dictionary of valid words
# string = string to be parsed into words
# curr = word being built out of string
# ind = index of string to be added 
# parsed = [] of words found
def words_in_string(words, string, curr, ind, parsed):
	curr += string[ind]
	ind += 1
	print(curr, ind)
	if ind == len(string):
		if curr not in words:
			if parsed:
				ind -= len(curr)
				curr = parsed.pop()
			else:
				print("no complete phrases")
				return False
		else:
			parsed.append(curr)
			return True
	elif curr in words:
		parsed.append(curr)
		curr = ""
	words_in_string(words, string, curr, ind, parsed)


a = ["tom", "tomorrow", "to", "row"]
x = [] # list of found words
# words_in_string(a, "torowtomorrowtom", "", 0, x)
# print(x)

def words_string(dictionary, string, words):
	size = len(string)
	if size == 0:
		return True
	for x in range(size):
		word = string[:x + 1]
		print(word)
		if word in dictionary and words_string(dictionary, string[x + 1:], words):
			return True
	return False


print(words_string(a, "torowtomorrowtom", x))
print(x)
