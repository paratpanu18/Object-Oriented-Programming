string = input()

def char_count(string):
    result = {}
    for char in string:
        if char not in result:
            result[char] = 1
        elif char in result:
            result[char] += 1
    return result

print(char_count(string))

