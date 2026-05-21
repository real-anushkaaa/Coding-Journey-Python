# Print number pattern:
# 1
# 12
# 123

for i in range(1,4):
    for j in range(1, 1+i):
        print(j, end="")
    print()