# convert a roman numeral to an int
# e.g.:
# XI = 11
# IV = 4
# LIX = 59

vals = {'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1}
    
def roman_numeral(roman):
    value = 0
    last = -1
    for num in reversed(roman):
        curr = vals[num]
        if curr < last:
            value -= curr
        else:
            value += curr
        last = curr
    return value


if __name__ == '__main__':
    a = 'MCMXCIX'
    b = roman_numeral(a)
    print(b)