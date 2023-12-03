number = [int(num) for num in input().split()]

if len(number) > 10:
    exit() 

number.sort()

if not number[0]:
    for i in number:
        if i and number[i] != 0:
            number.insert(0, number.pop(i))
            break

print("".join([str(num) for num in number]))