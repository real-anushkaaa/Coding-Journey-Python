# Compare lengths of two strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) > len(str2):
    print("First string is longer")

elif len(str2) > len(str1):
    print("Second string is longer")

else:
    print("Both strings have equal length")