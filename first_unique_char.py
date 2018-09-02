# given a string return the first non-repeating character
# in that string
from collections import OrderedDict

def non_repeat_char(string):
	mapping = OrderedDict()
	for char in string:
		if char in mapping:
			mapping[char] += 1
		else:
			mapping[char] = 1
	for char, count in mapping.items():
		if count == 1:
			return char
	return None
	

if __name__ == '__main__':
	a = "AAFF33LKK"
	x = non_repeat_char(a)
	print(x)

	a = "Z((!P!QAQAGG!Z"
	x = non_repeat_char(a)
	print(x)