# Find GCD/HCF (Greatest Common Divisor) using recursion
# Do numbers ko exactly divide karne wala sabse bada common number.
# Euclidean recursion formula : GCD(a,b)=GCD(b,amodb)
def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)

print(gcd(20, 12))