# Take temperature as input and print:
# <20 → Cold
# 20–35 → Normal
# 35 → Hot

temp = int(input("temp : "))

if temp < 20:
    print("cold")

elif temp <= 35:
    print("normal")

else:
    print("hot")