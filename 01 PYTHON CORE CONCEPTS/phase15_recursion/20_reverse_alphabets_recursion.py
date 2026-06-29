# Print reverse alphabets Z to A using recursion

def reverse_alphabet(ch):

    # Base condition
    if ch < 'A':
        return

    print(ch)

    reverse_alphabet(chr(ord(ch) - 1))


reverse_alphabet('Z')