a = int(input())
n = 0
b = 1
c = 0
while (n < a):
    n += 1
    b = c + b
    c = b - c
print(c)