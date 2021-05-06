a= float(input("輸入月租費型式"))
b= float(input("輸入通話時間"))
if(a == 186):
    b= b*0.09
    if(b>a):
        b = b*0.8
        b = ('%.0f'%b)
        print("通話費為：%s"%(b))
    elif(b<a):
        b=b*0.9
        b=('%.0f'%b)
        print("通話費為：%s"%(b))
elif(a == 386):
    b= b*0.08
    if(b>a):
        b=b*0.7
        b=('%.0f'%b)
        print("通話費為：%s"%(b))
    elif(b<a):
        b=b*0.8
        b=('%.0f'%b)
        print("通話費為：%s"%(b))
elif(a== 586):
    b=b*0.07
    if(b>a):
        b=b*0.6
        b=('%.0f'%b)
        print("通話費為：%s"%(b))
    elif(b<a):
        b=b*0.7
        b=('%.0f'%b)
        print("通話費為：%s"%(b))
elif(a== 986):
    b=b*0.06
    if(b>a):
        b=b*0.5
        b=('%.0f'%b)
        print("通話費為：%s"%(b))
    elif(b<a):
        b=b*0.6
        b=('%.0f'%b)
        print("通話費為：%s"%(b))