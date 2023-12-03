def add2list(list1, list2):
    return [x + y for x,y in zip(list1, list2)]

list1 = [int(num) for num in input().split()]
list2 = [int(num) for num in input().split()]

print(add2list(list1, list2))