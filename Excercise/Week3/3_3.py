plusone = {
    1:2,
    3:4,
    5:6
}

not_plusone = {
    5:6,
    7:8,
    10:11
}

def is_plusone_dictionary(dict):
    previous = list(dict.keys())[0] - 1
    for i in dict.items():
        if i[0] + 1 == i[1] and i[0] == previous + 1:
            previous = i[1]
            continue
        else:
            return False
    return True

print(is_plusone_dictionary(not_plusone))