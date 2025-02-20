import math
def gcd(a,b):
    if b==0:
        return a;
    return gcd(b, a%b)

a = int(input("Enter a no: "))
b = int(input("Enter another no: "))
c = math.gcd(a,b)
d = gcd(a,b)
print(f"GCD of {a} and {b} is: {c}")
print("GCD of {} and {} is: {}".format(a,b,d))

# Method 2

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
while num2  != 0:
    rem = num1 % num2
    num1 = num2
    num2 = rem
print(num1, num2)
print(f"GCD is {num1}")