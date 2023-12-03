def count_minus(str):
    return len([num for num in str.split() if int(num) < 0])

print(count_minus(input()))