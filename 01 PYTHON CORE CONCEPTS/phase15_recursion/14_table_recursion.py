# Find table of a number using recursion

def table(num, i=1):
    if i > 10:
        return
    
    print(num , "X" , i , "=" , num*i)
    table(num,i+1)

table(5)