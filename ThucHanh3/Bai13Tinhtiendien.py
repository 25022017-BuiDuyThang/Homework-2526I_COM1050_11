num = int(input())
bac1 = 1500
bac2 = 2000
bac3 = 3000
if num <= 50: print(num*bac1)
elif num > 50 and num <= 100: print(50*bac1 + (num-50)*bac2)
elif num > 100: print(bac1*50 + bac2 * 50 + (num-100)*bac3)
else: print(num)