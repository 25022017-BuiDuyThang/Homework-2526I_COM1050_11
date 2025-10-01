
array = [int(input()) for i in range(4)]
res = array[0]
for i in array :
    if(res < i) : res = i
print(res) 