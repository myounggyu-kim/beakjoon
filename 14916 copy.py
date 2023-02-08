n = int(input())
count = 0
while n>=10:
    n -= 5
    count +=1
else:
    if n == 1 or n==3:
        count = -1
    elif n==2:
        count += 1
    elif n==4:
        count += 2
    elif n==5:
        count += 1
    elif n==6:
        count += 3
    elif n==7:
        count += 2
    elif n==8:
        count += 4
    elif n==9:
        count += 3
print(count)

