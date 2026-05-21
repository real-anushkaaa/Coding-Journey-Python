# --------------------------------------------------
# Create function that checks palindrome.
# --------------------------------------------------

def palindrome(word):
    return word == word[::-1]

print(palindrome("abnba"))