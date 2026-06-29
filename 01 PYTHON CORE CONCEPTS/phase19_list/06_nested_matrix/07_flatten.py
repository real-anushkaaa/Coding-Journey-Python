# Flatten nested list.

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = []

for row in matrix:

    for item in row:

        flat.append(item)

print(flat)