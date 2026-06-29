# Count positive and negative numbers separately.

list = [-1,-4,3,-10,3,5,6,-20]
positive = 0
negative = 0 

for i in list:
    if i > 0:
        positive+=1

    elif i < 0:
        negative+=1

print(positive)
print(negative)