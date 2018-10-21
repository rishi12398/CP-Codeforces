import math
l = list(map(int,input().split()))
g=l[0]
for i in l:
    g = math.gcd(g,i)

print (g)

if g == 1:
for i in range(len(l)):
    
