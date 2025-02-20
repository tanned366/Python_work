# armstrong number
a = int(input("Enter a number: "))
sum = 0
temp = a
power = len(str(a))
while temp > 0:
    dig = temp % 10
    sum += dig ** power
    temp //= 10
if a == sum:
    print(a, "is an Armstrong number")
else:
    print(a, "is not an Armstrong number")
# Output: Enter a number: 153
# 153 is an Armstrong number

# disarium number
a = int(input("Enter a number: "))
sum = 0
temp = a
power = len(str(a))
while temp > 0:
    dig = temp % 10
    sum += dig ** power
    power -= 1
    temp //= 10
if a == sum:
    print(a, "is a Disarium number")
else:
    print(a, "is not a Disarium number")
# Output: Enter a number: 175
# 175 is a Disarium number