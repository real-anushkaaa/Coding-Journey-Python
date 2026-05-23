# Compare two marks and print which is higher.

m1 = int(input("enter the marks"))
m2 = int(input("enter the marks"))

if m1 > m2:
    print("First has higher marks")
elif m2 > m1:
    print("Second has higher marks")
else:
    print("Both have equal marks")