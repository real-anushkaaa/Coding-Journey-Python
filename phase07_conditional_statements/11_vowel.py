# Take a character as input and check whether it is a vowel or consonant.

ch = input("enter the character").lower()

if ch in "aeiou":
    print("vowel")

else:
    print("consonant")