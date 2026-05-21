# Take marks as input and print grade:
# 90+ → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

marks = int(input("enter the number : "))

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 50:
    print("C")

else:
    print("Fail")