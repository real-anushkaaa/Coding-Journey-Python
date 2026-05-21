# Check whether entered word is short or long.

word = input("Enter a word: ")

if len(word) <= 4:
    print("Short Word")

else:
    print("Long Word")