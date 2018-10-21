n = input()
n = int(n)
l = list(map(int,input().split()))
l.sort()
area = 0
pi = 3.1415926536
if n%2 == 0:
    for i in range(1,len(l),2):
        area = area + (pi*l[i]*l[i]-pi*l[i-1]*l[i-1])
else:
    area = pi*l[0]*l[0]
    if n==1:
        area = area
    else:
        for i in range(2,len(l),2):
            area = area + (pi*l[i]*l[i]-pi*l[i-1]*l[i-1])

print (area)
