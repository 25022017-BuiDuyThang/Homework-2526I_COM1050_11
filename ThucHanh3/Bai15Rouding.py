a = float(input("Nhập số thực: "))
phannguyen = int(a)

# Làm tròn xuống (floor)
if a >= 0: 
    val3 = phannguyen
else: 
    if a == phannguyen: 
        val3 = phannguyen
    else: 
        val3 = phannguyen - 1

# Làm tròn lên (ceil)
if a >= 0:
    if a == phannguyen: 
        val1 = phannguyen
    else: 
        val1 = phannguyen + 1
else: 
    val1 = phannguyen

# Làm tròn gần nhất (round)
digit = a - phannguyen

if digit >= 0.5: 
    val2 = phannguyen + 1
elif digit <= -0.5: 
    val2 = phannguyen - 1
else: 
    val2 = phannguyen

# In kết quả
print(val1, val2, val3)
