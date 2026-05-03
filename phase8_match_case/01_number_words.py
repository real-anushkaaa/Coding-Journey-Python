# Take a number (1–3) and print:
# 1 → One
# 2 → Two
# 3 → Three

num = int(input("enter the num"))

match num:
    case 1: print("one")
    case 2: print("two")
    case 3: print("three")
    case _: print("invalid case")

