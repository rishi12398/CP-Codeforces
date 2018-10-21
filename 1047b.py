n = raw_input()
n = int(n)
l=[]
for i in range(n):
    x,y = raw_input().split()
    x = int(x)
    y = int(y)
    l.append((x,y))

a = l[0][0]+l[0][1]
max = a
for i in range(1,len(l)):
    a = l[i][0] + l[i][1]
    if a > max:
        max = a

print max       
