def add2list(list1=[int(num) for num in input().split()], list2=[int(num) for num in input().split()]): return [x + y for x,y in zip(list1, list2)]
print(add2list())