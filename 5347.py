import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(int(a*b/math.gcd(a,b)))