# Reverse a string using loop.

s = input("enter the string : ")
rev = ""

for ch in s:
    rev = ch + rev
    
print(rev) 