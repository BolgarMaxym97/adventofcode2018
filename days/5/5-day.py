import string


def refactor_string(original_string):
    previous_char = ''
    while True:
        replaced = False
        for char in original_string:
            if char.lower() == previous_char.lower():
                if (char.islower() and previous_char.isupper()) or (char.isupper() and previous_char.islower()):
                    original_string = original_string.replace(previous_char + char, "")
                    replaced = True
            previous_char = char
        if not replaced:
            break
    return len(original_string)


f = open('../../dist/5.txt', 'r').read()

ascii_lower = string.ascii_lowercase
ascii_upper = string.ascii_uppercase
minLength = len(f)
for i in range(0, len(ascii_lower)):
    preparedString = f
    if ascii_upper[i] in preparedString:
        preparedString = preparedString.replace(ascii_upper[i], '')
    elif ascii_lower[i] in preparedString:
        preparedString = preparedString.replace(ascii_lower[i], '')
    length_refactored_string = refactor_string(preparedString)
    if length_refactored_string < minLength:
        minLength = length_refactored_string

print('part 1 - ', refactor_string(f))
print('part 2 - ', minLength)
