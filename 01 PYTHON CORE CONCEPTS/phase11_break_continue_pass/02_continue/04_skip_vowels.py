# Take a string and print all characters except vowels. 

s = input("enter the string : ")

for ch in s:
    if ch.lower() in "aeiou":
        continue
    print(ch)