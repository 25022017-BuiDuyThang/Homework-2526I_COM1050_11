m,n = map(int, input().split())
a = []
def is_peak(a, i, j, m, n):
    x = a[i][j]
    for r in range(max(0, i-1), min(m, i+2)): # duyệt các ô xung quanh ô [i][j] nhe 
        for c in range(max(0, j-1), min(n, j+2)):
            if (r == i and c == j):
                continue
            if a[r][c] >= x:
                return False
    return True

for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

res = 0
for i in range (m):
    for j in range(n):
        if is_peak(a,i,j,m,n):
            res += 1

print(res)        