def reverse(pattern):
    word = ""
    for char in pattern:
        word = char + word
    return word
pattern = input()
print(reverse(pattern))