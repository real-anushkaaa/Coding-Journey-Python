# Remove spaces from a string.

s = input("enter the string : ")
result = ""

for ch in s:
    if ch != " ":
        result = result + ch
        
print(result)