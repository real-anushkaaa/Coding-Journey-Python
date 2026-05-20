# Take principal, rate, and time as input and calculate simple interest,
# then print whether interest is high (>1000) or low.

p = int(input("enter the principal"))
r = int(input("enter the rate"))
t = int(input("enter the time"))

si = (p*r*t)/100

print(si)

if si > 1000:
    print("high")

else:
    print("low")