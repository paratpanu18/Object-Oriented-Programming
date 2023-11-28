import time

max, max_i, max_j = 0, 0, 0
start = time.time()
for i in range(100000, 10000, -1):
    for j in range(i, 10000, -1):
        if (str(i * j) == str(i * j)[::-1]) and i * j > max:
            max = i * j
            max_i = i
            max_j = j
        elif i < max_i and j < max_j:
            break

print(max)
print('Run time: ', time.time() - start, 's', sep = '')