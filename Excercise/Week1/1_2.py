lower, upper = 0, 0
input = input('Enter string: ')

for i in input:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

print(lower, upper, sep = '\n')