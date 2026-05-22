# Print alphabets A to Z using recursion

def print_alphabet(ch):

    # Base condition
    if ch > 'Z':
        return

    print(ch)

    print_alphabet(chr(ord(ch) + 1))


print_alphabet('A')