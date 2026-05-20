# Take a number and check:
# 10 → Ten
# 20 → Twenty
# Default → Other

num = int(input("enter the number"))

match num:
    case 10: print("ten")
    case 20: print("twenty")
    case _: print("other")