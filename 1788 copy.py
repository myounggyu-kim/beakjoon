import sys
input = sys.stdin.readline
n = int(input())
dp = [0,0]
first = 0
second = 1
if n == 0:
    print(0)
    print(0)
elif n == 1:
    print(1)
    print(1)
elif n>0:
    for i in range(2,n+1):
        tem = first + second
        first , second = second, tem
    print(1)
    print(second)
elif n<0:
    first = 1
    second = 0
    #[1 0 음수....]
    for i in range(abs(n)):
        tem = first - second
        first , second = second, tem
    if second >0:
        print(1)
        print(second)
    elif second == 0:
        print(0)
        print(0)
    else:
        print(-1)
        print(abs(second))
