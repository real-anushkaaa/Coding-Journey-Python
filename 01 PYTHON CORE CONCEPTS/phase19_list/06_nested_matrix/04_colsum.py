# Find column sums.
# Find sum of each column.

list = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

for col in range(3):

    total = 0

    for row in range(3):

        total += list[row][col]

    print(total)