# Check if first letter is vowel.

text = input("enter a string : ")

if text[0].lower() in "aeiou":
    print("First letter is a vowel")

else:
    print("First letter is not a vowel")