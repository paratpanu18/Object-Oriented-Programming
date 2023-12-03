def count_char_in_string(x, c):
    result = []
    for word in x:
        count = 0
        for char in word:
            if char == c:
                count += 1
        result.append(count)
    return result

x = ['abbc', 'banana', 'bbabbaaa']
c = 'b' 

print(count_char_in_string(x, c))