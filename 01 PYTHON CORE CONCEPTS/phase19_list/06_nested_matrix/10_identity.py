# Check identity matrix.

matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

identity = True

for i in range(3):

    for j in range(3):

        if i == j and matrix[i][j] != 1:
            identity = False

        elif i != j and matrix[i][j] != 0:
            identity = False

if identity:
    print("Identity Matrix")

else:
    print("Not Identity Matrix")