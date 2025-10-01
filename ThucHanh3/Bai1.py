n = int(input())
res = 0
while n > 0 :
    temp = n%10
    res = res*10 + temp
    n //= 10
print(res)