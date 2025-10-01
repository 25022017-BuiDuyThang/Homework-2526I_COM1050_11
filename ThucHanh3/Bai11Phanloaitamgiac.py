def isTria(a,b,c):
    if a + b > c and a + c > b and b + c > a: return True
    return False 

a,b,c = map(int,input().split())
if not isTria(a,b,c) : print("Không phải tam giác") 
else:
    if a == b and b == c: print("Tam giác đều")
    elif a == b and b != c or a == c and b != a or b == c and a!=c: print("Tam giác cân")
    else: print("Tam giác thường")
