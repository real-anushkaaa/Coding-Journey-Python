# Check if last character is digit.

text = input("enter a string : ")

if text[-1].isdigit():
    print("Last character is a digit")

else:
    print("Last character is not a digit")