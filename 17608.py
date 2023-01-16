import sys
input = sys.stdin.readline
a = []
for _ in range(int(input())):
    a.append(int(input()))

b = a.pop()
count = 1
for i in range(len(a)):
    c  =a.pop()
    print(b,c)
    if c>b:
        b=c
        count +=1
        
print(count)