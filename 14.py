max = 1e-3
cnt = 0
n = int(input())
while n != 0:
    n = int(input())
    if n > max:
        max = n
    if max == n:
        cnt+=1
        
print(cnt - 1)