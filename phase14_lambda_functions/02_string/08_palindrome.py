# ----------------------------------------
# Create lambda function to check palindrome.
# ----------------------------------------

palindrome = lambda text: text == text[::-1]

print(palindrome("anvna"))