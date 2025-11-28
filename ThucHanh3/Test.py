
def check(c):
    return c >='1' and c <='9'


s = str(input())

res = 0
i = 0
while i < len(s):
    if check(s[i]):
        temp = 0
        while i < len(s) and check(s[i]):
            temp = temp * 10 + int(s[i])
            i += 1
        res += temp
    else:
        i += 1
print(res)