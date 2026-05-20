# Take a number and check:
# 1, 3, 5 → Odd group
# 2, 4, 6 → Even group

num = int(input("enter the number"))

match num:
    case 1|3|5: print("odd group")
    case 2|4|6: print("even group")
    case _: print("invalid group")