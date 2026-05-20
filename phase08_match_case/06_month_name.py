# Take a month number and print month name (else → Invalid).

month = int(input("entere the number"))

match month:
    case 1: print("jan")
    case 2: print("feb")
    case 3: print("mar")
    case 4: print("apr")
    case 5: print("may")
    case 6: print("jun")
    case 7: print("jul")
    case 8: print("aug")
    case 9: print("sep")
    case 10: print("oct")
    case 11: print("nov")
    case 12: print("dec")
    case _: print("invalid month")