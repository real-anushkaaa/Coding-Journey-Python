# Check if string is palindrome.

s = input("enter the string : ")
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("palindrome")

else:
    print("not palindrome")
