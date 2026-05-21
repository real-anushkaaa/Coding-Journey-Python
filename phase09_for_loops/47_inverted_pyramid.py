# Print inverted pyramid.
# *******
#  *****
#   ***
#    *

for i in range(4,0,-1):

    for j in range(4-i):
        print(" ", end="")

    for k in range(2*i-1):
        print("*", end="")

    print()