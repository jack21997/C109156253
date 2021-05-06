a=int(input("請輸入階乘值:"))
n=i=1
while n <=a:
    n=n*i
    i=i+1
print("超過M為"+str(a)+"的最小階層N值為:"+str(i-1))