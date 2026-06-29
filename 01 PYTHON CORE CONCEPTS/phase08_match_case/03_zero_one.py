# Take a number and print:
# 0 → Zero
# 1 → One
# Otherwise → Invalid

num = int(input("enter the number"))

match num:
    case 0: print("zero")
    case 1: print("one")
    case _: print("invalid case")