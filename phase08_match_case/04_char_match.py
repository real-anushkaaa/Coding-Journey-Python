# Take a character and match:
# 'a' → Apple
# 'b' → Ball
# 'c' → Cat

ch = input("enter the character")

match ch:
    case 'a': print("apple")
    case 'b': print("ball")
    case 'c': print("cat")
    case _: print("invalid character")