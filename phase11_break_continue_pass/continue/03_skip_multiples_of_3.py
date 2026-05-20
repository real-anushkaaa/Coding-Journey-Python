# Print numbers from 1 to 50 except multiples of 3. 

for i in range(1,51):
    if i % 3 == 0:
        continue
    print(i)