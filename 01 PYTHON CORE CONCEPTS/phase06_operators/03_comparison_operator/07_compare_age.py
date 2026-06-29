# Compare two ages and print result.

age1 = int(input("enter the age"))
age2 = int(input("enter the age"))

if age1 > age2:
    print("First person is older")
elif age2 > age1:
    print("Second person is older")
else:
    print("Both are same age")