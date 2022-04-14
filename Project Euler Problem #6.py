sum = 0
sum2 = 0
square = 0

for i in range(1,101):
    sum += i**2
    sum2 += i
    square = sum2 **2

print(square - sum)
