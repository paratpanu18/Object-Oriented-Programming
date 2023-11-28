number = int(input('Enter number: '))
sum = 0

if number > 0:
    for i in range(4):
        sum += number
        number = int(str(number) + str(number)[0])
    print(sum)