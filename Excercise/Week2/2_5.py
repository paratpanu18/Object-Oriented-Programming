input = input()

def english_only(string1):
    return "".join([str(char) for char in string1 if char.isalpha()])

print(english_only(input))