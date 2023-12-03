x = [[1, -2, 3], [1, 1, -7], [2, 1, 0]]

def delete_minus(x):
    return [[num for num in list if num >= 0]  for list in x ]

print(delete_minus(x))