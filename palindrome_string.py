# determine if a string is a palindrome

def palindrome_recursive(string):
	print(string)
	if len(string) <= 1:
		return True
	return string[0] == string[-1] and palindrome_recursive(string[1:-1])

a = "Hello"
print(palindrome_recursive(a))
b = "asdkfdsa"
print(palindrome_recursive(b))