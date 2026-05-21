# Take age as input and check:
# <18 → Minor
# 18–60 → Adult
# 60 → Senior Citizen

age = int(input("enter the number"))

if age < 18:
    print("minor")

elif age <= 60:
    print("adult")

else:
    print("senior citizen")