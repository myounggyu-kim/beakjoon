T = int(input())
for _ in range(T):
    a , b = map(int,input().split())
    a = a % 10
    if a==0:
        print(10)
    elif a==2:
        if b%4==1:
            print(2)
        elif b%4==2:
            print(4)
        elif b%4==3:
            print(8)
        else: #나머지0
            print(6)
    elif a==3:
        if b%4==1:
            print(3)
        elif b%4==2:
            print(9)
        elif b%4==3:
            print(7)
        else: #나머지0
            print(1)
    elif a==4:
        if b%2==1:
            print(4)
        else: #나머지0
            print(6)
    elif a==7:
        if b%4==1:
            print(7)
        elif b%4==2:
            print(9)
        elif b%4==3:
            print(3)
        else: #나머지0
            print(1)
    elif a==8:
        if b%4==1:
            print(8)
        elif b%4==2:
            print(4)
        elif b%4==3:
            print(2)
        else: #나머지0
            print(6)
    elif a==9:
        if b%2==1:
            print(9)
        else: #나머지0
            print(1)
    else: #1,5,6인 경우
        print(a) #자기 자신리턴