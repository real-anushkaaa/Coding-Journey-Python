# Print multiplication table using nested loop.
# 1  2  3 ...
# 2  4  6 ...
# ...


for i in range(1,6):  
    for j in range(1,11):
        print(i*j, end="\t")
    print()